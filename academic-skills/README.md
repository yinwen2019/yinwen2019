# Academic Skills · 学术技能

面向论文研究与写作的个人 Skill 集合，目前聚焦科研绘图。将绘图偏好、参考库维护和图形设计拆开，按任务选择使用，并随实际反馈持续更新。

## 技能导航

| 文件夹 | 状态 | 用途 | 主要交付 |
| --- | --- | --- | --- |
| [plot](plot/SKILL.md) | 可用 | 用 Python 绘制或调整论文中的定量图，如曲线、柱状图、分布图、消融实验和嵌入可视化 | 可运行绘图代码，默认导出矢量 PDF |
| [figure-library](figure-library/SKILL.md) | 可用，已验证论文链接入库流程 | 从论文链接、PDF 或图片建立和维护个人框架图参考库 | 高清参考图、科学上下文、视觉分析与偏好记录 |
| [framework-figure](framework-figure/SKILL.md) | 可用，提示词工作流初版 | 根据当前论文方法，借鉴参考库设计 framework、pipeline 或 architecture 图 | 中文设计说明、完整英文生图提示词、参考图片列表 |
| [intro-figure](intro-figure/) | 规划中，仅目录占位 | 根据背景、动机和核心思想设计 conceptual 或 teaser 图 | 拟提供设计说明、英文提示词与参考图；尚无可调用的 SKILL.md |

## 如何选择

- **已有实验数据或绘图代码，需要画论文统计图**：使用 `plot`。
- **想把喜欢的论文图加入参考库，或更新长期偏好**：使用 `figure-library`。
- **已有当前论文的背景和方法，需要设计主框架图**：使用 `framework-figure`；直接复用已有库时，无需先运行维护技能。
- **需要 Intro 动机图**：等待 `intro-figure` 的参考库和工作流完成。

下面的示例路径均以本仓库根目录为起点。在能读取仓库文件的 AI 工具中，让 AI 先阅读对应的 `SKILL.md`，再提供任务材料即可。复制技能到其他位置时，应保留其所需的参考数据和脚本，或明确指定自己的参考库路径。

## 已可用技能的使用方法

### plot：Python 科研绘图偏好

**提供**：数据或现有 Python 代码、图要表达的结论、指标含义，以及单栏/双栏尺寸等要求。

**得到**：适配现有数据流程的绘图代码，应用字体、配色、坐标轴、图例和导出偏好。运行后默认得到矢量 PDF；图形和误差范围必须依据真实数据。

```text
请读取 academic-skills/plot/SKILL.md。
根据我提供的数据和代码绘制双指标超参数敏感性图。
保留现有统计计算逻辑，说明必要的显示调整，并给出可运行代码和 PDF 输出。
```

绘图代码需要 Python 及所使用的 Matplotlib、Seaborn 等依赖。这个技能主要规定视觉风格，具体图形仍由数据与表达目标决定。

### figure-library：初始化与更新参考库

**提供**：论文链接、PDF 或原始图片；可附喜欢/不喜欢的细节。建立个人库时，还需给出保存目录。

**得到**：每张参考图对应一个目录，保存图片及 `notes.md`，记录来源、科学上下文、视觉分析和用户偏好。PDF 默认截取为 400 DPI、质量 95 的 JPG，并记录图号、页码与裁剪位置。

向本仓库的默认库添加参考：

```text
请读取 academic-skills/figure-library/SKILL.md。
将以下论文的主框架图加入 academic-skills/framework-figure/ 参考库：
（粘贴论文链接）
请截取高清图片，整理科学上下文和视觉分析；我喜欢的具体细节是……
```

创建自己的库时，将上面的目标换成独立目录，例如 `my-figure-library/`，并明确要求初始化；之后让设计技能使用同一个 `library_root`。更新偏好时，可以明确说：“将这个反馈保存为该参考库的长期偏好”。

维护技能使用 [extract_figure.py](figure-library/scripts/extract_figure.py) 裁图，需要 Python 和 `PyMuPDF>=1.22`。AI 先阅读论文并查看页面来选择图与裁剪区域，脚本负责渲染；导出后仍需查看图片。

### framework-figure：主框架图设计与提示词

**提供**：当前论文的背景、方法、输入输出、关键模块与连接、训练和推理的区别，以及想强调的创新点。影响方法含义的缺失信息会先澄清。

**得到**：中文设计说明、完整英文提示词，以及实际需要附给生图工具的参考图片列表。

```text
请读取 academic-skills/framework-figure/SKILL.md。
使用同目录下的参考库，根据下面的论文背景和方法设计主框架图：
（粘贴背景与方法）
请给出中文设计说明、完整英文生图提示词和参考图片列表，并解释各图借鉴了什么。
```

使用自己的库时，在请求中补充 `library_root` 的实际目录。技能每次读取最新偏好及全部简短分析记录，通常选取 2–4 张互补参考；只有一张或暂无合适参考时也可继续设计，并说明依据。

当前交付到提示词为止。实际生图时，把英文提示词和列出的参考图片一并提供给支持参考图输入的生图模型；仅粘贴图片路径不会传入图片。生图后还需核对文字和连线。直接生图与可编辑终稿留作后续扩展。

## 当前参考库

默认库保存在 [framework-figure/](framework-figure/)：共性偏好见 [preferences.md](framework-figure/preferences.md)，每张图和分析记录在 [references/](framework-figure/references/) 下。

首批已收录 [CoTyle · Fig. 3](framework-figure/references/cotyle-fig3/notes.md)、[SD-MIA · Fig. 1](framework-figure/references/sd-mia-fig1/notes.md)、[AToken · Fig. 2](framework-figure/references/atoken-fig2/notes.md)、[FGAesQ · Fig. 4](framework-figure/references/fgaesq-fig4/notes.md)。图片宽约 2,600–2,700 像素，并附来源与裁图信息。

这四篇是作者已选中的正向参考，具体审美细节尚待反馈确认。其他使用者可以直接借用本库；作者偏好仍保留原归属。建立自己的偏好库时，使用独立目录。

## 后续规划

`intro-figure` 将围绕“问题与动机 → 核心思想 → 任务或能力展示”建立工作流，先积累 conceptual / teaser 正向图例，再整理偏好与提示词要求。当前仅保留目录，尚未实现。

现有参考库继续采用全库阅读；待规模确实影响效率后，再决定是否分类或引入检索工具。
