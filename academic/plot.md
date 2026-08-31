---
name: yinwen-academic-plot-style
description: Apply Yinwen's personal academic visualization style to Python figures made with Matplotlib and Seaborn. Use when creating, restyling, or reviewing research plots, including training curves, grouped bars, distributions, hyperparameter sensitivity panels, ablations, and embedding visualizations. Interpret the figure semantics first, preserve the analysis logic, and adapt the visual encoding instead of forcing a fixed chart template.
---

# Yinwen Academic Plot Style

## Purpose

Apply a compact, publication-oriented visual style after understanding what the figure must communicate.

Treat this file as a style layer, not a plotting workflow. Preserve the user's data loading, preprocessing, statistical choices, and requested chart type unless a correction is necessary. Let an explicit user request override every default below.

Use this priority order:

1. Preserve statistical and semantic correctness.
2. Follow explicit requirements for the current figure.
3. Apply the stable personal defaults in this file.
4. Adapt dimensions and details to the data density and final publication layout.

Infer ordinary styling decisions without asking. Ask a focused question only when an unresolved choice would change the scientific meaning of the figure.

## Visual Identity

Prefer a clean academic-paper appearance:

- Use Matplotlib and Seaborn, selecting whichever gives better control for the requested chart.
- Use `Times New Roman` for English text and mathematical labels when available.
- Keep the composition compact and information-dense without crowding.
- Avoid decorative backgrounds, gradients, rounded bars, heavy fills, and unnecessary titles.
- Omit an in-figure title by default; let the paper caption carry the title unless the user requests one.
- Use complete black axis frames for conventional quantitative plots.
- Use inward ticks and restrained dashed grids.
- Export the final figure as a vector PDF by default.

Start conventional single-panel figures with:

```python
plt.rcParams.update({
    "font.family": "Times New Roman",
    "font.size": 18,
})
```

## Color Semantics

Use the following core palette:

```python
COLORS = {
    "blue": "#3A6EA5",
    "blue_light": "#7EA6D0",
    "blue_pale": "#AFC8E8",
    "orange": "#EE964B",
    "orange_light": "#F4C395",
    "orange_pale": "#F6C89F",
    "purple": "#6A4C93",
}
```

Assign visual channels by meaning:

- Map IQA to blue and IAA to orange when the figure compares these tasks.
- Map a proposed Rank Reward or Two-stage method to purple when color is encoding methods rather than tasks.
- When a figure compares both tasks and methods, use color for task and line style for method: solid for the proposed method and dashed for the baseline.
- Use darker and lighter shades of one hue for stages or related submetrics. Prefer dark for `Final`, primary, or emphasized values and light for `Candidate`, secondary, or contextual values.
- When task semantics do not apply, use blue first, orange second, and purple third while keeping the mapping consistent across related figures.
- Reserve red for a real target, warning threshold, or decision boundary. Use black for a zero baseline.
- For many categorical classes in an embedding plot, use a discretized high-contrast palette such as `Spectral`. Do not imply continuous values when labels are categorical.
- Add marker or line-style differences when a figure must remain interpretable in grayscale. Do not rely on color alone when series are otherwise difficult to distinguish.

Never change the meaning of a color between panels of the same figure or between directly related figures.

## Size And Typography

Choose a compact canvas based on the figure structure:

| Figure | Starting size |
| --- | --- |
| Single-panel training curve | `(7, 5)` |
| Compact KDE distribution | `(7, 3)` |
| Paired or horizontally dense bars | `(8, 4.5)` |
| Two side-by-side sensitivity panels | `(12, 5)` |

Adjust these dimensions when labels, panels, or publication columns require it. Do not mechanically force every figure into `(7, 5)`.

Use this typography hierarchy as a starting point:

- Axis labels: about 20 pt.
- Tick labels: about 14-16 pt.
- Legend: about 13-18 pt, reduced when entries are dense.
- Direct value annotations: about 14 pt.
- Base font: 18 pt for standard figures and about 14 pt for short, compact distribution figures.
- Use bold for the primary result-axis label when emphasis helps, such as `Performance`, `Completion Length`, or `Reward`. Keep descriptive distribution labels regular when bold would add unnecessary weight.
- Avoid 26 pt text unless the user is preparing a presentation rather than a paper figure.

Ensure all labels remain legible after the figure is reduced to its intended paper size.

## Conventional Axes

For ordinary line, bar, and density plots:

- Keep all four spines visible, black, and approximately `1.2` points wide.
- Set major ticks inward with top and right ticks enabled when appropriate.
- Use dashed grids with alpha around `0.35-0.5` and place them behind the data with `zorder=0`.
- Use both-axis grids for trend plots only when they improve reading. Prefer a y-axis-only grid for bar charts.
- Put primary data at `zorder=3` or `zorder=5` so it remains above the grid.
- Use zero margins when the axes should meet meaningful bounds, but do not force zero margins if labels or distributions need breathing room.
- Set axis limits deliberately for fair comparison. Share limits across comparable panels and runs.
- Add a black zero line around `linewidth=1.5` for positive-versus-negative comparisons.
- Truncate an axis only when the scientific comparison benefits, and make the choice visible in the code.

## Training And Trend Curves

- Draw the main line at approximately `linewidth=2.5`.
- Use a rolling mean for dense, noisy training histories when smoothing helps reveal the trend. Select the window from the sampling density; values around 50-75 are common examples, not fixed requirements.
- Keep sparse hyperparameter curves unsmoothed.
- Use `min_periods=1` in rolling calculations so the beginning of a curve is not silently dropped.
- Add a subtle band only when it represents real variability, repeated runs, a documented confidence interval, or a clearly identified descriptive local envelope.
- Use alpha around `0.10-0.15` for ordinary bands. Increase it only when overlap remains readable and the stronger band has semantic purpose.
- Make a baseline band lighter than the proposed-method band when both are shown.
- Do not call a rolling min-max envelope a confidence interval.
- Use identical x ranges and comparable y ranges when curves are intended for direct comparison.

## Bar Charts

- Use black bar edges with `linewidth` around `1.0-1.2`.
- Keep bars within a group visually close and preserve a clear gap between groups.
- Use manual Matplotlib positions when Seaborn cannot provide the required group spacing or ordering.
- Disable Seaborn error bars with `errorbar=None` when each bar is already a single reported value. Show error bars only when supported by repeated observations or supplied uncertainty.
- Use deep and pale shades of the same task color for paired stages.
- Add direct labels when exact counts, percentages, or retention values matter. Use a second line for secondary information when it prevents horizontal crowding.
- Use a visible zero line for diverging bars.
- Treat numeric hyperparameter settings as evenly spaced categories when the goal is discrete setting comparison. Use a line chart when the continuous trend is the scientific claim.

## KDE And Distribution Plots

- Use an outline near `linewidth=1.8` with a same-color fill near `alpha=0.28`.
- Keep overlapping distributions transparent enough to remain distinguishable.
- Treat `bw_adjust=0.9` as a reasonable initial value, then adapt it to sample size and distribution shape.
- Clip a long tail only when justified by the analysis. Never silently alter the displayed distribution for appearance.
- Keep distribution figures vertically compact when the density shape remains readable.

## Hyperparameter Sensitivity Panels

- Use lines with visible markers for discrete settings. Prefer circles and squares for two metrics, with marker size around 8 and line width around 2.5.
- Use `sharey=True` for directly comparable side-by-side panels.
- Keep the same y limits and hide only duplicated right-panel y labels with `tick_params(labelleft=False)`.
- Use mathematical text for parameters such as `r"$\tau_a$"`.
- Never invent a `+/-` band to make a sensitivity plot look richer. Draw uncertainty only from real measurements.

## Embedding And Manifold Plots

Treat UMAP, t-SNE, and manifold figures as geometry-focused exceptions to conventional axis styling:

- Use small points for dense embeddings; `s=6` is a useful starting point.
- Preserve equal aspect with `ax.set_aspect("equal", "box")` when geometric shape matters.
- Hide ticks and labels when embedding coordinates have no interpretable units.
- Use a meaningful geometric boundary, such as a black Poincare-disk circle, when required by the projection.
- Avoid generic grids and annotations that compete with the embedding.
- Keep categorical colors discrete and reproducible.

## Legends And Annotations

- Use a framed legend with a white background by default.
- Use a light gray edge when the legend frame needs separation without a heavy black box.
- Place the legend in genuine whitespace and avoid covering important curves or bars.
- Use two columns when entries are numerous or naturally paired.
- Tune `columnspacing` and `handletextpad` to keep dense legends compact.
- Construct legend handles manually when exact category order, colors, or stage semantics matter.
- Omit the legend for a single self-explanatory series unless it carries information not expressed by the axis labels.
- Highlight a meaningful target line and its matching tick by numeric value, never by a fragile tick-label index.

## Dual Axes

Use a secondary y axis only when the metrics have materially different scales and combining them is necessary. Prefer aligned panels when they communicate the comparison more honestly.

When using `twinx()`:

- Filter each metric into exactly one axis; never draw the secondary metric on both axes.
- Label both axes clearly and make each scale unambiguous.
- Keep color and legend semantics consistent.
- Avoid manipulating axis ranges solely to exaggerate agreement or difference.

## Export

Use vector PDF as the default research output:

```python
fig.tight_layout()
fig.savefig(output_path, bbox_inches="tight", pad_inches=0)
plt.show()
```

Use a very small pad such as `0.02` when multi-panel edges or markers risk clipping. Add `dpi=300` for dense scatter points or other rasterized elements. If the user explicitly requires the PDF page to equal `figsize`, omit `bbox_inches="tight"` instead of contradicting that requirement in a comment.

Use an informative output filename. Keep PDF as the primary artifact unless the user requests PNG, SVG, or another format.

## Scientific Integrity

- Never fabricate uncertainty, variance, confidence intervals, or repeated-run behavior.
- Never silently clip, normalize, rebalance, smooth, or remove data for aesthetics.
- Document any display-only clipping, smoothing, common-step truncation, or axis truncation in code comments.
- Preserve identical comparison windows when fairness requires them.
- Avoid duplicate series, invisible bars outside an axis range, and legends for artists that are not actually displayed.
- Avoid fragile formatting tied to positional indices when a semantic value can be targeted directly.
- Keep category order, hue order, line style, and marker meaning deterministic.
- Correct obvious syntax and plotting errors while preserving the intended analysis.
- Do not copy project paths, run IDs, credentials, or dataset-specific values into reusable style code.

Return runnable plotting code that fits the user's existing data pipeline. Apply these rules with judgment so the resulting figure looks like part of the same paper, not like a rigid template.
