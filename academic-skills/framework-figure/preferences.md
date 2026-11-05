# Framework Figure · 个人视觉偏好

归属：Wen Yin / 殷文。其他使用者可以借用本库风格，明确创建个人库时使用独立的 `library_root`。

本文件保存有用户反馈依据的偏好。设计流程见 [SKILL.md](SKILL.md)；各图的科学上下文、视觉分析与局部反馈保存在 [references/](references/) 中。

## 已确认的参考选择

2026-11-04，用户明确表示下列四篇是自己挑选的喜欢的论文，并要求将主框架图收录。这确认了参考选择，尚未确认喜欢每张图中的所有视觉细节。

- [CoTyle · Figure 3](references/cotyle-fig3/notes.md)
- [SD-MIA · Figure 1](references/sd-mia-fig1/notes.md)
- [AToken · Figure 2](references/atoken-fig2/notes.md)
- [FGAesQ · Figure 4](references/fgaesq-fig4/notes.md)

2026-11-05，用户明确要求新增以下三篇论文到参考库。确认的是收录选择，具体主框架图由 AI 根据论文内容定位；尚无新的局部审美反馈。

- [BehaviorVLA · Figure 2](references/behaviorvla-fig2/notes.md)
- [C²R · Figure 2](references/c2r-fig2/notes.md)
- [XR-1 · Figure 2](references/xr1-fig2/notes.md)

## 已确认的共性视觉偏好

目前尚无具体的共性视觉规则。字体、色值、圆角、线宽和固定布局未被用户指定为后续默认。

新增规则时记录偏好描述、适用条件、反馈日期和依据。依据可以是用户明确的长期要求，或多个参考记录中的已确认反馈。单图局部意见保存在该图记录中。

## 待确认的偏好假设

以下来自已收录图片的视觉观察，不能当作用户已确认的要求：

- **具体样例嵌入方法流程**：首批四图均将真实图像或文本样例与模块、箭头结合；新增的 [BehaviorVLA](references/behaviorvla-fig2/notes.md)、[C²R](references/c2r-fig2/notes.md) 和 [XR-1](references/xr1-fig2/notes.md) 也使用任务帧或数据缩略图。待确认用户是否喜欢这种具体化表达，及其适用场景。
- **颜色与语义分组对应**：[CoTyle](references/cotyle-fig3/notes.md)、[AToken](references/atoken-fig2/notes.md)、[FGAesQ](references/fgaesq-fig4/notes.md) 都使用颜色帮助识别模块或信息类别，但色值和字体并不统一。待确认是否偏好这种分组方式。
- **有层次的整体与局部表达**：[CoTyle](references/cotyle-fig3/notes.md) 区分训练阶段与推理，[FGAesQ](references/fgaesq-fig4/notes.md) 使用上层总览与下层模块展开，[SD-MIA](references/sd-mia-fig1/notes.md) 使用上下机制对照。新增的 [BehaviorVLA](references/behaviorvla-fig2/notes.md) 将总览与双模块展开对应，[XR-1](references/xr1-fig2/notes.md) 用上大下双栏展示三个训练阶段；[C²R](references/c2r-fig2/notes.md) 则采用紧凑横向双目标布局。这些是可选表达方式，尚不能固定成所有图的版式。

## 修订说明

- 2026-11-05：新增 BehaviorVLA、C²R、XR-1 三条参考，更新相关视觉观察；两篇 OpenReview 来源采用已核对身份的 PMLR 官方 PDF。未新增已确认共性规则。

- 2026-11-04：收录首批四条正向参考；记录三个待确认观察，未将观察提升为共性视觉规则。维护流程迁移至独立 `figure-library` 技能。

用户修正偏好时，更新有效规则并简短记录日期、变化和原因。当前任务的临时样式选择不写入共性偏好。
