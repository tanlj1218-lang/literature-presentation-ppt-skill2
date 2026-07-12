# 循证文献深度汇报 PPT Skill

这是一个用于将**学术论文 PDF 及其补充材料**转换为约 **45 分钟深度文献汇报 PPT** 的可复用 Skill。

它强调的不是简单摘要，而是：

- 建立完整的科学问题逻辑线；
- 深入解释研究对象、纳排标准、数据收集、质量控制和测量工具；
- 逐步拆解统计分析方法、参数意义和操作流程；
- 将结果图表与科学含义并列呈现；
- 重构讨论逻辑并进行独立方法学评价；
- 形成针对使用者本人研究的具体启示；
- 为复杂方法提供复现代码与参数说明；
- 对所有关键数字、图表和外部信息进行证据追踪；
- 输出风格统一、可继续编辑的 PPTX，而不是整页图片。

## 默认设置

- 汇报时长：约 45 分钟
- 正文页数：38–48 页
- 附录页数：5–15 页
- 页面比例：16:9
- 中文字体：微软雅黑
- 页面结构：顶部导航栏 + 主体内容 + 底部参考文献
- 视觉风格：低饱和度、顶刊式、留白充分、避免多余阴影

## 本地安装

将整个 `literature-presentation-ppt-skill` 文件夹复制到你使用的 Skills 目录中即可。不要只复制 `SKILL.md`，因为该技能还会调用 `guides/`、`templates/`、`checklists/` 和 `prompts/` 中的配套文件。


## 技能包结构

```text
literature-presentation-ppt-skill/
├── SKILL.md
├── README.md
├── guides/
│   ├── study-design-modules.md
│   ├── ppt-design-system.md
│   └── method-reproduction.md
├── templates/
│   ├── 45min-outline.md
│   ├── slide-spec.yaml
│   ├── evidence-tracker.csv
│   └── delivery-manifest.md
├── checklists/
│   ├── academic-qa.md
│   ├── visual-qa.md
│   └── editability-qa.md
├── prompts/
│   └── slide-visual-reference-prompt.md
├── scripts/
│   ├── init_project.py
│   └── validate_project.py
└── examples/
    └── project-config.yaml
```

## 使用方式

### 1. 初始化项目目录

```bash
python scripts/init_project.py /path/to/my-paper-project
```

生成的项目目录包括：

- `inputs/`：论文 PDF、补充材料和模板；
- `working/slide_specs/`：逐页内容规格；
- `working/visual_references/`：生图模型生成的页面视觉参考；
- `working/extracted_assets/`：从 PDF 提取的原图；
- `working/redrawn_assets/`：重新绘制的图标和素材；
- `working/code/`：统计复现代码；
- `working/evidence-tracker.csv`：图表和关键数字来源追踪；
- `outputs/`：最终 PPTX 和交付文件。

### 2. 放入材料

将论文 PDF 和补充材料放入 `inputs/`，并填写 `project-config.yaml`。

### 3. 按 Skill 执行

主执行规则位于 [`SKILL.md`](SKILL.md)。

每一页需要先完成：

1. 页面目的；
2. 唯一核心结论；
3. 证据及来源；
4. 页面布局；
5. 视觉参考图；
6. PPT 原生元素级重建；
7. 学术、视觉和可编辑性检查。

### 4. 验证项目结构

```bash
python scripts/validate_project.py /path/to/my-paper-project
```

## 视觉生成原则

生图模型用于生成：

- 页面视觉设计参考；
- 透明背景图标；
- 复杂装饰或插画素材。

生图模型不得承担：

- 正式论文文字；
- 精确统计数字；
- P 值、置信区间；
- 精确表格；
- 真实结果图表。

最终 PPT 需要使用原生文本框、Shape、表格和图表重建，不能将整张视觉参考图直接作为背景。

## 支持的研究设计

包括但不限于：

- 横断面研究；
- 纵向队列研究；
- 随机对照试验；
- 症状网络分析；
- 交叉滞后网络；
- 轨迹模型；
- 潜在剖面分析；
- 中介与调节分析；
- 调节网络；
- 计算机模拟网络干预；
- 结构方程模型；
- 系统评价与 Meta 分析；
- 质性研究；
- 预测模型与机器学习；
- 混合方法研究。

详细规则见 [`guides/study-design-modules.md`](guides/study-design-modules.md)。

## 最终交付

默认交付：

1. 可编辑 PPTX；
2. 内容分析文档；
3. 复现代码或方法文件；
4. 图表证据追踪表；
5. 参考文献清单；
6. 图片和图表素材文件夹；
7. 未解决问题清单；
8. 完整项目 ZIP。
