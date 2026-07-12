# PPT Design System

## 1. Visual Character

The deck should resemble a polished editorial presentation for medicine, nursing, public health, psychology, or behavioral science:

- warm off-white or very light neutral background;
- low-saturation teal as the principal academic color;
- restrained coral or warm accent for key findings only;
- dark teal or charcoal text;
- clear hierarchy and strong alignment;
- intentional negative space;
- minimal decoration;
- lightweight navigation;
- no cartoon style unless the topic clearly requires it;
- no excessive gradients, heavy shadows, glossy cards, or dashboard-like clutter.

The approved user preference is the first-version editorial style. Use `guides/default-visual-benchmark.md` and the images under `assets/default-visual-benchmark/` when no newer user-approved template is available.

## 2. Design Priority

When layout rules conflict, use this order:

1. academic accuracy;
2. one clear takeaway;
3. projection readability;
4. visual hierarchy;
5. aesthetic consistency;
6. spatial fullness.

Whitespace is permitted when it creates focus. Do not add blocks or screenshots merely to fill space.

## 3. Default Geometry

- Ratio: 16:9.
- Use stable outer margins.
- Reserve a small bottom band for citations and page number.
- Use a lightweight top navigation bar.
- Maintain a coherent grid, but do not force symmetrical columns when the content needs a dominant figure.
- Align major objects to shared guides.
- Keep the slide title and main evidence visually dominant over navigation and decoration.

## 4. Typography

- Chinese: Microsoft YaHei (微软雅黑).
- English/numerals: Microsoft YaHei or a compatible sans-serif font.
- Use no more than three text levels on a normal slide.
- Use bold and accent color only for meaning.

Recommended hierarchy:

- slide title: 26–32 pt;
- conclusion subtitle: 20–24 pt;
- body: 16–20 pt;
- figure annotation: 14–17 pt;
- short references: 9–11 pt, only if still readable after rendering.

Never shrink body text below 16 pt to avoid splitting a slide.

## 5. Color System

Use:

- one principal color;
- one supporting color;
- one accent color;
- neutrals for background and body text.

Default benchmark:

- background: warm off-white;
- principal: muted teal;
- secondary: pale sage or blue-green;
- accent: restrained coral;
- body text: dark teal/charcoal.

Do not assign a unique color to every category. Preserve source-chart colors when they encode meaning.

## 6. Lightweight Navigation

Default labels:

- 文献概况
- 研究背景
- 研究方法
- 研究结果
- 讨论分析
- 研究启示

Rules:

- keep the navigation shallow and visually quiet;
- highlight the active section with a small filled tab, underline, or accent marker;
- do not use a full-height dark banner on every slide;
- navigation must never become the strongest object on the page.

## 7. Five Core Page Archetypes

Choose an archetype deliberately. Do not default to cards.

### 7.1 Editorial Two-Column

Use for background, concepts, discussion, and appraisal.

- one side: argument, evidence, or comparison;
- other side: interpretation, mechanism, or implication;
- unequal widths are allowed when one side is more important.

### 7.2 Large Evidence + Interpretation

Use for results, tables, figures, and models.

- the paper figure/table or a native redraw is the visual anchor;
- interpretation is concise and adjacent;
- the figure may occupy most of the slide when it is the key message.

### 7.3 Full-Width Logical Chain

Use for introduction, theory, mechanisms, and analysis workflow.

- one coherent left-to-right or top-to-bottom sequence;
- avoid isolated cards when a connected argument is more accurate;
- use arrows, bands, or staged headings sparingly.

### 7.4 Comparison Matrix

Use for discussion, methodological appraisal, prior-study comparison, or transfer to the user's research.

- present study;
- prior evidence or standard;
- interpretation;
- implication or improvement.

### 7.5 Single-Conclusion Editorial Page

Use for a pivotal transition, summary, or one major finding.

- one strong conclusion;
- one meaningful visual, key number, or short supporting explanation;
- intentional negative space is allowed.

## 8. Card and Color-Block Policy

- A normal slide should contain no more than three cards.
- Consecutive slides must not repeat the same card grid.
- Do not wrap every sentence in a rounded rectangle.
- A large pale box is permitted only when it represents a complete conceptual unit.
- Do not create visual hierarchy by adding more borders; use position, scale, spacing, and typography first.
- Avoid dashboard aesthetics for narrative academic presentations.

## 9. Section Dividers

- Main deck: normally no more than four divider slides.
- Use navigation, title changes, or a subtle section label for minor transitions.
- Divider slides should not interrupt the argument every few pages.
- A divider must provide a meaningful pause, not inflate page count.

## 10. Figure and Table Readability

- Never place a source table or figure at a size that cannot be read in presentation mode.
- If the original is too dense, choose one:
  1. native redraw;
  2. enlarged crop of the relevant area;
  3. split across slides;
  4. simplified summary with the full source in the appendix.
- Do not place a native reconstruction and a tiny duplicate screenshot of the original on the same slide.
- Do not retain tiny screenshots solely to prove source fidelity.
- Preserve axes, labels, legends, and proportions.
- Use callouts to emphasize the relevant result without hiding context.

## 11. Reference Display System

Every substantive slide needs a visible source marker, but not every slide needs a long footer.

Use a layered system:

1. **In-text marker**: `[1]`, `[2–4]`, or author-year beside the claim when helpful.
2. **Short footer**: 1–2 concise references in readable type.
3. **Source note**: `Source: Deng et al., 2026, Fig. 1` for paper figures/tables.
4. **Full list**: complete references at the end or in the delivery package.

Rules:

- introduction/theory/method/discussion slides normally show short references;
- results slides may use a source note plus in-text citation;
- do not repeat the same full method citation on every consecutive slide when one concise source marker is sufficient;
- the citation must support the exact claim.

## 12. Theory Design

Theory pages are function-driven, not quota-driven.

A theory should appear only if it explains:

- the target phenomenon;
- the variable relationships;
- developmental or clinical differences;
- the study design or analytical method.

Typical structures:

- origin and core proposition;
- construct/pathway map;
- mapping to the paper;
- applicability and limitation;
- integrated conceptual model.

Do not create six theory slides if two complete slides communicate the logic better.

## 13. Visual Reference Generation

Before full production, prepare four editable sample slides:

- title;
- introduction/theory;
- methods;
- results.

If needed, use image generation to explore layout or produce transparent assets. Generated images must not contain formal statistics, exact article text, or fabricated charts. Rebuild the approved design using native PowerPoint elements.

## 14. Native Reconstruction

- Formal text: native text boxes.
- Simple geometry: native shapes.
- Arrows: native connectors when possible.
- Tables: native tables or editable shape groups.
- Charts: native charts when exact data are available.
- Complex paper figures: high-resolution crops when faithful reconstruction is unsafe.
- Keep objects selectable and logically grouped.
- Do not flatten an entire slide into one background image.

## 15. Full-Deck Visual Review

After building the deck:

1. Render every slide.
2. Create a thumbnail montage.
3. Review the deck as a sequence, not only slide by slide.
4. Check for:
   - overuse of cards;
   - repetitive layouts;
   - excessive divider slides;
   - heavy navigation;
   - color drift;
   - decoration stronger than evidence;
   - unreadable figures/tables;
   - sudden changes from the approved samples;
   - excessive density or accidental emptiness.
5. Compare the montage to the approved four-slide sample and the default visual benchmark.
