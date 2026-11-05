# behaviorvla-fig2 · BehaviorVLA / Figure 2

## 来源与截取

- 论文：**From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model**；Bing Hu、Zaijing Li、Rui Shao、Junda Chen、April Hua Liu、Wei-Shi Zheng、Liqiang Nie。
- 会议与版本：ICML 2026，PMLR 306:45272–45289；本条依据 PMLR 论文集 PDF。[官方条目](https://proceedings.mlr.press/v306/hu26ad.html)。
- 用户原始链接：[OpenReview PDF](https://openreview.net/pdf?id=2NRrsz4nUB)。2026-11-05 访问返回 403/浏览器验证，改用官方论文集；官方条目的 OpenReview 链接指向相同 ID，标题、作者与摘要吻合。未声称两个 PDF 文件逐字相同。
- 实际下载：[PMLR 官方 PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/hu26ad/hu26ad.pdf)。
- 图号与页码：Figure 2，PDF 第 3 页（从 1 开始），页面印刷页码 3。Figure 1 混合动机、架构概览与结果，本次选择更完整的整体方法图 Figure 2。
- 图片：[figure.jpg](figure.jpg)；裁剪框 `[60, 70, 535, 317]`，单位 points，页面左上角为原点；页面大小 612 × 792 points。
- 渲染：PyMuPDF 2.1；400 DPI；JPEG 质量 95；2640 × 1374 px。
- 源 PDF SHA256：`16aec8a3e1c414898029074a2fea627c912ae6aae719da03c201269fcdbf26e5`。
- 图片 SHA256：`2ba307aa3ad16f0fa6ab320eb7aec0db23381c7fd8175536380a187979a3dbba`。
- 上下文依据：摘要与引言（PDF 第 1–2 页）、Figure 2 图注（第 3 页）、§3.1–3.3（第 4–5 页）。
- 最近更新：2026-11-05。已查看完整页面及最终 JPG；总览、两处模块展开、右上图例和边缘连线均完整，未混入图注或正文。

## 科学上下文

- **问题与动机**：VLA 在环境变化下容易退化；短时动作表示难以保持长程行为一致性，静态先验又容易与实际执行进度错位。本文将全局任务结构与局部执行进度分开建模。
- **方法概要**：Visuomotor Behavior Encoder（VBE）用因果 Mamba 和跨模态注意力处理视觉、动作、行为三条流。离线轨迹形成全局行为原型并存入 Memory Bank；推理时，由初始观测与指令检索原型，仅在 episode 开始时检索一次，并保持该原型固定。VBE 根据当前观测和上一动作持续更新局部 phase state。
- **解码关系**：Phase-Conditioned Behavior Decoder（PBD）将全局原型展开为 latent anchors，以当前 phase 作为 Progress Attention 的 query，形成动作先验；Flow Policy 接收结构先验与观测等条件，细化得到动作。不能把原型检索误写成每步更新，也不能把 phase token 画成固定常量。
- **图的范围**：下半部展示观测/语言、记忆检索、VBE、PBD 与 Flow Policy 的关系；上半部展开 VBE，右侧展开 PBD。它不是完整训练日程图，训练阶段与损失需另外依据正文；右下 `O_{t+1}` 图像展示执行后的情境，不能据此把策略理解为图像生成模型。

## 视觉分析

- **布局与阅读顺序**：下半部是整体流程，左侧输入经 VLM 和检索头到中部记忆库，再接右侧解码与动作策略；上方大面积展示编码器细节，右侧窄面板展示解码器细节。先读总览，再沿展开指示线看内部结构，比单纯按页面从上往下读更合理。
- **模块关系与箭头**：实线箭头表达 token/特征流；注意力连接标出 Q、K/V；上方 phase 状态保留递归连接。浅蓝灰虚线连接总览模块与放大面板，属于“展开说明”，不代表新增数据流。记忆库中的圈选机器人示意检索出的行为原型。
- **配色与形状**：视觉流用浅杏色、动作流用浅蓝色、行为与记忆用紫灰色，文本/通用组件用灰色。小立方体贯穿总览和细节，并在右上图例解释 token 类型；浅底色圆角区域与嵌套边框区分层级。
- **字体与层级**：模块标题以无衬线字为主，公式用数学字形；总览关键模块加粗，细节标签较小。整体颜色柔和，但低对比细线与密集 token 在缩小后可能变弱。
- **可迁移**：适合“一个整体系统 + 两个关键创新模块”的结构。可借鉴总览与展开面板的对应、跨面板一致的 token 图例、全局先验与在线状态的区分。面板面积应按当前方法的信息量调整。
- **不宜照搬的细节**：图中 `Retrival Head` 为原图拼写；新图应使用正确术语 `Retrieval Head`。立方体、机器人图标、阴影和圆角是本图样式观察，不是强制规范。

## 用户偏好

- **已确认**：2026-11-05 用户明确要求将该论文加入参考库；Figure 2 由 AI 根据整体方法表达范围选定。尚无针对具体颜色、字体或模块的明确喜好反馈。
- **待确认**：是否喜欢“总览 + 双模块展开”、低饱和配色、立体 token 图例，以及用真实任务帧提供语义锚点。
- **不宜迁移**：VBE/PBD、Mamba 三流、原型记忆、phase 递归及 Flow Policy 属于该论文方法。不能为模仿版式而添加到其他论文中。

## 待补充

- 用户喜欢或不喜欢的具体区域与原因；若后续指定 OpenReview 中不同修订版的图，再核对并更新本条。
