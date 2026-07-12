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

## v1.2.0 的关键变化

本版本修复了 v1.1.0 因“机械填满页面”造成的过度卡片化和视觉退步：

- 删除 70%–88% 页面占用率、18% 留白上限和“每页至少两个内容单元”等硬性规则；
- 明确留白可以是有意设计，禁止为了填满页面添加无意义色块、卡片或小截图；
- 将第一版的米白背景、轻量青绿色导航、珊瑚色强调和编辑式布局设为默认视觉基准；
- 完整制作前必须先交付标题、引言/理论、方法、结果四张样稿并获得用户确认；
- 引入五种核心页面原型，避免所有页面都做成卡片仪表盘；
- 普通页面卡片不超过三个，连续页面不得重复相同卡片结构；
- 引用改为分层呈现：正文标号、简短页脚、图表来源说明和末尾完整文献；
- 理论基础改为功能导向，不再按固定页数凑页；
- 禁止不可读的小图、小表和重复原图缩略图；
- 正文建议 38–46 页，章节过渡页不超过 4 张；
- 最终必须生成全稿缩略图蒙太奇，检查节奏、重复、卡片化、导航重量和视觉一致性。

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
│   ├── method-reproduction.md
│   └── evidence-and-theory.md
├── templates/
│   ├── 45min-outline.md
│   ├── style-approval-brief.md
│   ├── slide-spec.yaml
│   ├── evidence-tracker.csv
│   ├── literature-evidence-matrix.csv
│   └── delivery-manifest.md
├── checklists/
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
3. 先制作四张视觉样稿；
4. 用户确认视觉方向；
5. 锁定设计参数后制作全稿；
6. 渲染全稿并生成缩略图蒙太奇；
7. 完成学术、视觉、引用、可编辑性和证据追踪检查。

## 初始化项目

```bash
python scripts/init_project.py /path/to/my-paper-project
```

## 验证项目

```bash
python scripts/validate_project.py /path/to/my-paper-project
```
