# Slide Visual Reference Prompt Pattern

Use this prompt to generate a visual design reference, not a final slide.

## Prompt

Create a high-end academic medical/nursing journal-club slide design reference in 16:9 format.

Slide purpose: {{slide_purpose}}
Main takeaway: {{main_takeaway}}
Section: {{section}}
Preferred layout: {{layout}}
Required visual zones: {{visual_zones}}
Theme/topic: {{topic}}
Design system: low-saturation, restrained, controlled whitespace, clear hierarchy, modern evidence-based academic style, no unnecessary shadows, no cartoon look. Use the full slide grid evenly and avoid large unintentional blank regions.
Navigation: include a slim top navigation area with one active section indicated visually, but do not render final readable navigation text.
Footer: reserve a narrow area for references and page number.

Important constraints:
- Do not generate exact article text.
- Do not generate exact statistics, P values, confidence intervals, or table data.
- Do not fabricate scientific charts.
- Use abstract placeholders for text and data zones.
- Keep the layout suitable for later reconstruction with native PowerPoint text boxes, shapes, tables, and charts.
- Ordinary content slides should visually occupy roughly 70–88% of the main content area.
- Distribute content across columns and top/middle/bottom zones; do not concentrate all elements in one corner.
- Reserve a readable reference footer on substantive slides.
- Avoid watermarks, pseudo-text, and garbled characters.

For a separate icon or illustration asset, create it on a transparent background with no text and no white border.
