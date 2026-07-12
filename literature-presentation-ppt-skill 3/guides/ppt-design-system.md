# PPT Design System

## 1. Visual Character

The deck should resemble a polished medical, nursing, public-health, or behavioral-science journal presentation:

- low-saturation colors;
- restrained use of accent color;
- strong hierarchy;
- controlled whitespace;
- minimal decoration;
- no cartoon style unless the paper topic clearly benefits from it;
- no excessive gradients;
- no unnecessary shadows;
- no cluttered infographic language;
- no large unintentional blank areas;
- balanced distribution across the full content grid.

## 2. Default Slide Geometry

- Ratio: 16:9.
- Use a stable outer margin.
- Use a persistent top navigation bar.
- Reserve a small bottom band for references and page number.
- Maintain a consistent grid across all slides.
- Use a 12-column grid or equivalent two-/three-column system.
- For ordinary content slides, target approximately 70–88% use of the main content area.
- No single unintentional blank region should exceed approximately 18% of the slide.
- Title and section-divider slides are exceptions, but even they should feel intentionally composed.

## 3. Typography

- Chinese: Microsoft YaHei (微软雅黑).
- English and numerals: Microsoft YaHei or a compatible sans-serif font.
- Use no more than three text levels on a typical slide.
- Avoid body text that is too small for projection.
- Use bold sparingly for meaning, not decoration.

Recommended hierarchy for a 16:9 academic deck:

- slide title: 26–32 pt;
- conclusion subtitle: 20–24 pt;
- body: 16–20 pt;
- figure annotation: 14–17 pt;
- references: 9–11 pt, only when still readable.

Adjust based on room size and density. Never compensate for sparse content by using oversized decorative text; never compensate for excessive content by reducing body text below 16 pt.

## 4. Color System

Use:

- one main color;
- one supporting color;
- one accent color;
- neutral background and text colors.

Rules:

- Use the accent color to highlight the active navigation item, key result, or critical arrow.
- Do not assign arbitrary colors to every category.
- Preserve original article colors when they encode meaning, unless recoloring can be done without ambiguity.
- For red/green contrasts, provide an additional shape, label, or line style for accessibility.

## 5. Navigation Bar

Default labels:

- 文献概况
- 研究背景
- 研究方法
- 研究结果
- 讨论分析
- 研究启示

The active section should be highlighted. All other items should remain visible but muted.

## 6. Slide Archetypes

### 6.1 Title Slide

- paper title as the main focus;
- journal, year, first author, and presenter as secondary information;
- minimal decoration;
- one topic-relevant visual or geometric motif.

### 6.2 Article Profile

- official journal cover on one side;
- journal metrics and bibliographic data in structured cards;
- author and affiliation block;
- DOI and registration information.

### 6.3 Background Logic Slide

Use a left-to-right or top-to-bottom logical progression:

- burden/problem;
- current knowledge;
- gap;
- study response.

### 6.4 Methods Flow Slide

- timeline, flowchart, or process pipeline;
- clear participant movement;
- measurement points;
- quality-control checkpoints.

### 6.5 Instrument Slide

Use a structured card or table:

- purpose;
- domains/items;
- scoring;
- interpretation;
- reliability;
- timing.

### 6.6 Statistical Method Slide

Use:

- research question;
- input;
- model/process;
- output;
- advantages;
- cautions.

Avoid pages filled with formulas unless the formula is central to understanding.

### 6.7 Results Slide

Default:

- left: evidence;
- right: interpretation.

Use a conclusion-style title and a clearly marked “结果含义” panel.

### 6.8 Discussion Slide

Use comparison columns or a causal/mechanistic chain:

- present study;
- prior study;
- possible reason;
- implication.

### 6.9 Methodological Appraisal Slide

Use three zones:

- strengths;
- concerns;
- improvement.

### 6.10 Implications Slide

Use a mapping structure:

- paper approach;
- transferable value;
- user-study adaptation;
- caution.

## 7. Content Density and Spatial Balance

Every ordinary content slide should contain at least two meaningful content units, such as:

- evidence + interpretation;
- concept + mechanism;
- prior evidence + gap;
- method step + rationale;
- result + comparison;
- finding + clinical meaning.

### Underfilled-slide trigger

A slide must be revised when any of the following occurs:

- less than roughly 60% of the main content area is used;
- all content is concentrated in one quadrant;
- a large empty half-slide remains without an intentional purpose;
- the slide contains only a short sentence and decorative imagery;
- the evidence footer is absent on a substantive slide.

Revision options, in order:

1. add the missing evidence, mechanism, comparison, or interpretation;
2. convert prose to a structured table, timeline, or conceptual diagram;
3. enlarge and annotate a relevant paper figure;
4. merge the slide with the adjacent logical step;
5. only then adjust scale and spacing.

### Overfilled-slide trigger

Split the slide when:

- content use exceeds roughly 90%;
- body text would need to be smaller than 16 pt;
- references would need to be smaller than 9 pt;
- more than one major conclusion competes for attention;
- the audience cannot identify the reading order in three seconds.

### Balance rules

- Align top edges across columns.
- Distribute blocks across top, middle, and bottom zones.
- Use consistent internal padding.
- Avoid a dense left column paired with an almost empty right column.
- Use equal visual weight, not necessarily equal text length.
- Results slides should normally devote 50–65% of the width to evidence and 35–50% to interpretation.

## 8. Image-Generation Reference Workflow

For each slide or slide archetype:

1. Create a content brief.
2. Decide the visual hierarchy.
3. Generate a visual reference image without exact formal text, exact data, or dense tables.
4. Use transparent-background generation for icons and complex decorative assets.
5. Rebuild the slide with native elements.

Do not:

- use the generated full slide as the final background;
- trust generated text or numbers;
- let generated charts replace real data;
- crop icons from unrelated images when they can be generated cleanly.

## 9. Native Reconstruction Rules

- All formal text must be native text boxes.
- Simple geometry must be native shapes.
- Lines and arrows must be native connectors when possible.
- Tables must be native tables or editable shape groups.
- Charts should be native charts when exact data are available.
- Complex article figures may remain as high-resolution source images.
- Keep each object selectable and logically grouped.
- Use consistent object naming when the library supports it.
- Avoid placing a flattened image over editable elements.

## 10. Reference Footer

Use concise references at the bottom of relevant slides:

- first author, journal, year;
- figure/table source when cropped;
- method paper for complex statistical explanation;
- official scale manual or documentation when scoring is explained.

Do not overload every slide with a long bibliography. However, every substantive slide must carry a concise footer; introduction, theory, methods, discussion, appraisal, and implication slides may not omit references.

## 11. Visual QA

Check:

- title alignment;
- navigation state;
- body-text readability;
- image resolution;
- figure distortion;
- consistent margins;
- equal spacing;
- no overlap or clipping;
- no orphaned labels;
- no decorative element competing with data;
- no misleading visual scaling;
- references remain readable;
- no large unintentional blank regions;
- content is balanced across the main grid;
- each substantive slide contains at least two meaningful content units.
