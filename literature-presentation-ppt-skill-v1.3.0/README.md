# 循证文献深度汇报 PPT Skill

这是一个将学术论文 PDF 及补充材料转换为约 45 分钟深度文献汇报 PPT 的可复用 Skill。

## 核心能力

- 建立完整的科学问题逻辑线；
- 主动检索理论、机制、方法和比较研究；
- 按研究设计自动切换方法解析模块；
- 逐步解释方法、参数、结果和实际含义；
- 独立开展方法学评价；
- 将论文做法映射到使用者自己的研究；
- 输出可编辑 PPTX、复现材料、证据追踪表和参考文献清单。

## v1.3.0 的关键变化

本版本把制作流程改为“先完成整套页面逻辑，再逐页生图，再逐页转为可编辑PPT”：

- 正式制作前必须先列出每一页放什么、回答什么问题、核心结论、前后逻辑、证据来源、视觉形式和引用；
- 新增完整内容架构审批门：用户先确认整套页序与每页逻辑，再进入全稿制作；
- 不再只为标题页或4页样稿生图，主稿和附录的每一页都必须生成独立的 image2/image_gen 全页视觉参考；
- 每页的生图提示词必须基于该页的真实科学问题、内容层级和证据形式，不能使用泛化医学背景；
- 生图完成后，必须使用图转PPT流程按元素拆解重建，不能把整张图作为PPT背景；
- 正式文字、图表、表格、引用全部使用PPT原生对象或经核实的论文原图重建；
- 结果页严格采用“一图/一个连贯图组 + 一组解释”，不同结果图或不同问题的图组必须拆页；
- 新增 full-deck blueprint、slide-production manifest、image2-to-editable-PPT 指南与三份专项检查表；
- 最终必须核对：页面规格数 = 生图参考数 = manifest记录数 = PPT页数。

## 默认视觉方向

当用户没有提供新模板时，使用 `assets/default-visual-benchmark/` 中的四张参考图：

- 标题页；
- 引言页；
- 方法页；
- 结果页。

默认风格：暖米白背景、轻量青绿色导航、深青绿色正文、少量珊瑚色强调、强对齐、干净表格、保留有意义的负空间。

## 默认设置

- 汇报时长：约 45 分钟
- 正文页数：通常 38–46 页
- 附录页数：通常 8–18 页
- 页面比例：16:9
- 中文字体：微软雅黑
- 章节过渡页：通常不超过 4 张
- 普通内容页卡片：不超过 3 个
- 每张实质性页面：必须有可见的引用或来源标记

## 安装

将整个 `literature-presentation-ppt-skill` 文件夹复制到 Skills 目录中。不要只复制 `SKILL.md`。

## 技能包结构

```text
literature-presentation-ppt-skill/
├── SKILL.md
├── README.md
├── assets/
│   └── default-visual-benchmark/
├── guides/
│   ├── default-visual-benchmark.md
│   ├── study-design-modules.md
│   ├── ppt-design-system.md
│   ├── image2-to-editable-ppt-workflow.md
│   ├── method-reproduction.md
│   └── evidence-and-theory.md
├── templates/
│   ├── 45min-outline.md
│   ├── style-approval-brief.md
│   ├── slide-spec.yaml
│   ├── full-deck-blueprint.md
│   ├── slide-production-manifest.csv
│   ├── evidence-tracker.csv
│   ├── literature-evidence-matrix.csv
│   └── delivery-manifest.md
├── checklists/
│   ├── storyboard-qa.md
│   ├── per-slide-image2-qa.md
│   ├── image-to-ppt-qa.md
│   ├── academic-qa.md
│   ├── visual-qa.md
│   ├── content-density-qa.md
│   ├── style-approval-qa.md
│   └── editability-qa.md
├── prompts/
│   └── slide-visual-reference-prompt.md
├── scripts/
│   ├── init_project.py
│   └── validate_project.py
└── examples/
    └── project-config.yaml
```

## 使用流程

1. 读取论文、补充材料和用户既往模板；
2. 完成外部理论、方法和讨论文献检索；
3. 先列出整套PPT每一页的内容、逻辑、证据、视觉形式和引用；
4. 制作四张样稿并请用户同时确认内容架构与视觉方向；
5. 为每一页生成独立的 image2/image_gen 全页视觉参考；
6. 逐页进行元素级图转PPT，重建为可编辑对象；
7. 渲染全稿并生成缩略图蒙太奇；
8. 完成故事板、生图覆盖率、图转PPT、学术、视觉、引用和可编辑性检查。

## 初始化项目

```bash
python scripts/init_project.py /path/to/my-paper-project
```

## 验证项目

```bash
python scripts/validate_project.py /path/to/my-paper-project
```
