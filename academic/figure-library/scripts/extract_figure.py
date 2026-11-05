#!/usr/bin/env python3
"""Render a visually selected PDF figure as a high-resolution JPEG.

Requires PyMuPDF >= 1.22. Coordinates are PDF points from the top-left of
the displayed page; page numbers are 1-based. This tool does not locate figures.
"""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import tempfile
import urllib.error
import urllib.parse
import urllib.request

try:
    import pymupdf as fitz
except ImportError:
    try:
        import fitz
    except ImportError:
        raise SystemExit("Missing PyMuPDF. Install with: python -m pip install 'PyMuPDF>=1.22'")


def load_pdf(source):
    normalized = source.strip()
    # A common copy/paste error: sentence punctuation after the PDF suffix.
    if normalized.lower().endswith('.pdf.'):
        normalized = normalized[:-1]
    parsed = urllib.parse.urlsplit(normalized)
    if parsed.scheme in ('https', 'http'):
        request = urllib.request.Request(normalized, headers={'User-Agent': 'FigureLibrary/1.0'})
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read()
            resolved = response.url
    elif parsed.scheme:
        raise ValueError('Use a local PDF path or an http/https URL.')
    else:
        path = Path(normalized).expanduser().resolve()
        data = path.read_bytes()
        resolved = str(path)
    if b'%PDF-' not in data[:1024]:
        raise ValueError('The source is not a PDF; it may be an HTML error or login page.')
    return data, normalized, resolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', help='Local PDF path or public PDF URL')
    parser.add_argument('--page', type=int, required=True, help='1-based page number')
    parser.add_argument('--bbox', type=float, nargs=4, metavar=('X0', 'Y0', 'X1', 'Y1'), required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--dpi', type=int, default=400)
    parser.add_argument('--quality', type=int, default=95)
    parser.add_argument('--overwrite', action='store_true', help='Replace an existing reviewed crop')
    args = parser.parse_args()

    try:
        if args.page < 1 or args.dpi < 1 or not 1 <= args.quality <= 100:
            raise ValueError('Page and DPI must be positive; JPEG quality must be 1–100.')
        if not all(math.isfinite(v) for v in args.bbox):
            raise ValueError('Crop coordinates must be finite numbers.')
        x0, y0, x1, y1 = args.bbox
        if x0 >= x1 or y0 >= y1:
            raise ValueError('Crop must have positive width and height.')
        output = args.output.expanduser().resolve()
        if output.suffix.lower() not in ('.jpg', '.jpeg'):
            raise ValueError('Output must use .jpg or .jpeg.')
        if output.exists() and not args.overwrite:
            raise ValueError('Output already exists; use --overwrite for an intentional update.')

        data, normalized, resolved = load_pdf(args.source)
        with fitz.open(stream=data, filetype='pdf') as doc:
            if doc.needs_pass:
                raise ValueError('The PDF is password-protected; supply an accessible PDF.')
            if args.page > len(doc):
                raise ValueError(f'Page {args.page} exceeds the PDF page count ({len(doc)}).')
            page = doc[args.page - 1]
            crop = fitz.Rect(args.bbox)
            if not page.rect.contains(crop):
                raise ValueError(f'Crop is outside the displayed page bounds {list(page.rect)}.')
            # Guard accidental excessive allocations, not normal 400 DPI figures.
            if crop.width * crop.height * (args.dpi / 72) ** 2 > 100_000_000:
                raise ValueError('Crop exceeds 100 megapixels; lower DPI or tighten the crop.')
            pix = page.get_pixmap(dpi=args.dpi, clip=crop, colorspace=fitz.csRGB, alpha=False)
            jpeg = pix.tobytes('jpeg', jpg_quality=args.quality)
            metadata = {
                'source_input': args.source, 'normalized_source': normalized,
                'resolved_source': resolved, 'source_pdf_sha256': hashlib.sha256(data).hexdigest(),
                'page': args.page, 'page_size_points': [page.rect.width, page.rect.height],
                'bbox_pdf_points': args.bbox, 'coordinate_system': 'displayed page, top-left, PDF points',
                'dpi': args.dpi, 'jpeg_quality': args.quality,
                'width_px': pix.width, 'height_px': pix.height,
                'renderer': 'PyMuPDF ' + fitz.VersionBind,
                'output': str(output), 'image_sha256': hashlib.sha256(jpeg).hexdigest(),
            }
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.tmp', delete=False) as handle:
                temporary = handle.name
                handle.write(jpeg)
            os.replace(temporary, output)
        finally:
            if temporary and os.path.exists(temporary):
                os.unlink(temporary)
        print(json.dumps(metadata, ensure_ascii=False, indent=2))
    except (OSError, ValueError, RuntimeError, urllib.error.URLError) as error:
        parser.exit(1, f'Figure extraction failed: {error}\n')


if __name__ == '__main__':
    main()
