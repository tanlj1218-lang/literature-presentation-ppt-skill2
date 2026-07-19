---
name: literature-presentation-ppt
description: Create a rigorous, citation-rich, visually refined, editable 45-minute academic literature presentation from a paper PDF and optional supplementary materials. Use for deep journal-club presentations that require a complete slide-by-slide scientific storyboard, explicit logic for every page, a mandatory full-deck content-architecture approval gate, one image2/image_gen full-slide visual reference for every slide, element-level image-to-PPT reconstruction, detailed introduction and theory, extensive literature verification, methods and parameter explanation, one-figure-one-interpretation results, critical appraisal, reproducibility materials, evidence tracking, and specific implications for the user's own research.
---

# Literature Presentation PPT Skill

## 1. Purpose

Use this skill to transform one academic paper, with or without supplementary materials, into a high-quality, fully editable PowerPoint presentation for an approximately 45-minute literature report.

The presentation must do more than summarize the article. It must:

1. Reconstruct the scientific problem as one coherent line of reasoning.
2. Explain the study design, instruments, data collection, quality control, and statistical methods in sufficient depth for an academic audience.
3. Present results step by step and translate statistical findings into scientific and clinical meaning.
4. Reorganize the discussion around the research questions, prior evidence, mechanisms, strengths, limitations, and methodological concerns.
5. Identify concrete implications for the user's own research rather than offering generic suggestions.
6. Produce a coherent, editable PPTX rather than a collection of flattened slide images.
7. Preserve evidence traceability for every important number, figure, table, and external claim.
8. Provide reproducibility materials for complex analytical methods.
9. Produce a complete page-by-page blueprint before any full-deck visual production begins.
10. Generate an individual image2/image_gen visual reference for every slide after the blueprint is approved.
11. Reconstruct every generated slide reference into a high-quality editable PPTX through element-level image-to-PPT conversion rather than using flattened slide backgrounds.

## 2. Default Scope

Unless the user specifies otherwise:

- Presentation length: approximately 45 minutes.
- Main deck: usually 38–46 slides; expand or contract according to article complexity.
- Appendix: usually 8–18 slides.
- Slide ratio: 16:9 widescreen.
- Chinese font: Microsoft YaHei (微软雅黑).
- Overall style: restrained editorial-academic design, low-saturation, high readability, intentional whitespace, and light navigation.
- Navigation: a lightweight persistent top navigation bar that supports orientation without competing with the slide title or evidence.
- References: every substantive slide must contain a visible citation or source marker, but the form may vary: concise in-text numbering, a short readable footer, or a figure/table source note. Full references are collected at the end. Title, divider, and roadmap slides are the normal exceptions.
- Section-divider slides: no more than four in the main deck unless the user explicitly requests more.
- Primary language: follow the user's language; for Chinese presentations, preserve original English terminology for scales, models, software packages, and key statistical indices.

### Quality Priority

When rules conflict, apply this priority order:

1. academic accuracy and evidence fidelity;
2. one clear message and information hierarchy;
3. projection readability and audience comprehension;
4. visual elegance and consistency with the approved benchmark;
5. page fill or decorative completeness.

Whitespace is not an error. Only accidental, structurally meaningless whitespace is a problem. Never add boxes, icons, screenshots, or text solely to make a page look full.

## 3. Required Inputs

Minimum input:

- The full paper PDF.

Optional inputs:

- Supplementary materials.
- Study protocol.
- Statistical analysis plan.
- Trial or study registration.
- Public analysis code.
- Data dictionary.
- Scale manuals or original questionnaires.
- Previous presentation templates.
- Images or decks the user wants to imitate.
- The user's own study protocol, manuscript, code, or research aims.

When only the main PDF is supplied, inspect the article for references to supplementary material, protocol, registration, public code, or data repositories. Retrieve public materials when available and necessary.

## 4. Non-Negotiable Academic Rules

1. Never invent methods, parameters, author biographies, sample details, or study procedures.
2. Clearly distinguish what the paper reports from what is supplied by external methodological literature.
3. Do not claim that reconstructed code is the authors' original code unless it is actually public and verified.
4. Do not claim full replication without the original data and code.
5. Do not convert association into causation.
6. Do not describe simulation-based intervention results as proven clinical efficacy.
7. Do not alter data, effect sizes, confidence intervals, P values, or figure proportions for visual convenience.
8. If information is missing, write “未报告” or “无法核实” rather than guessing.
9. If the main text and supplement conflict, report the discrepancy.
10. Every external claim that materially changes interpretation must be supported by a source.
11. Journal impact factor and ranking information must include the year/version and source; if authoritative verification is unavailable, mark it for institutional verification.
12. Visual polish must never reduce interpretability or hide limitations.

## 5. Companion Files

Use these files with this skill:

- `guides/study-design-modules.md`: design-specific analysis modules.
- `guides/ppt-design-system.md`: visual system, page archetypes, citation display, and native PowerPoint reconstruction rules.
- `guides/default-visual-benchmark.md`: the approved default editorial-academic visual direction derived from the user's preferred first version.
- `guides/method-reproduction.md`: reproducibility appendix and code requirements.
- `guides/evidence-and-theory.md`: external literature search, theory reconstruction, and slide-level citation rules.
- `templates/45min-outline.md`: default 45-minute deck structure.
- `templates/slide-spec.yaml`: per-slide planning schema.
- `templates/evidence-tracker.csv`: source-tracking template.
- `templates/delivery-manifest.md`: final deliverables manifest.
- `checklists/academic-qa.md`: academic quality review.
- `checklists/visual-qa.md`: visual and layout review.
- `checklists/editability-qa.md`: PPT editability review.
- `checklists/content-density-qa.md`: visual balance, hierarchy, anti-cardification, citation, and projection-readability review.
- `checklists/style-approval-qa.md`: four-slide sample and user-approval gate.
- `prompts/slide-visual-reference-prompt.md`: page-specific image2/image_gen prompt pattern for full-slide academic visual references.
- `guides/image2-to-editable-ppt-workflow.md`: mandatory per-slide generation and element-level image-to-PPT reconstruction protocol.
- `templates/full-deck-blueprint.md`: required page-by-page content architecture and logic map.
- `templates/slide-production-manifest.csv`: tracks slide specification, image2 reference, reconstruction, and QA status for every page.
- `templates/style-approval-brief.md`: required style-review package before full production.
- `checklists/storyboard-qa.md`: page-by-page logic and scientific-storyboard review.
- `checklists/per-slide-image2-qa.md`: verifies that every slide has a generated academic visual reference.
- `checklists/image-to-ppt-qa.md`: checks element-level reconstruction fidelity and editability.
- `assets/default-visual-benchmark/`: four reference slides for title, introduction, methods, and results.

## 6. End-to-End Workflow

### Phase A. Intake and Material Audit

1. Read the full PDF, not only the abstract.
2. Inspect all tables, figures, appendices, footnotes, and supplementary references.
3. Record:
   - title;
   - journal;
   - publication date and online date;
   - DOI;
   - first and corresponding authors;
   - affiliations;
   - funding;
   - registration;
   - study country/region;
   - study design;
   - sample size;
   - research questions or hypotheses;
   - main methods;
   - main outcomes;
   - limitations.
4. Identify missing materials and retrieve public supplements if required.
5. Check for corrections, retractions, or updated versions.
6. Identify the paper's study design and activate the relevant module in `guides/study-design-modules.md`.
7. If the user provided an earlier PPT or reference image, analyze it before designing the new deck.

### Phase A2. Approved Visual Benchmark and Style Gate

Before building the full deck:

1. Inspect any user-approved older deck or reference images. If the user has said that an earlier version looked better, that version becomes the primary visual benchmark.
2. If no user template is supplied, use `guides/default-visual-benchmark.md` and the four images in `assets/default-visual-benchmark/`.
3. Prepare two coherent visual directions only when there is genuine uncertainty. Do not present many superficial theme variations.
4. Build four editable sample slides:
   - title page;
   - introduction/theory page;
   - methods page;
   - results page.
5. Render the four samples and provide them for user approval using `templates/style-approval-brief.md`.
6. Do not construct the full deck until the user approves one direction, unless the user explicitly waives the review stage.
7. After approval, lock the design tokens: background, title hierarchy, navigation weight, color palette, card policy, figure treatment, citation style, spacing, and page archetypes.
8. Later content revisions must preserve the approved visual system. Increasing detail must not trigger an unapproved redesign.

The first-version editorial style is the default benchmark: warm off-white background, lightweight teal navigation, dark teal text, restrained coral accent, strong alignment, clean tables, and generous but intentional negative space.

### Phase B. External Verification and Methodological Supplementation

Verify current, unstable, or article-external information, including:

- latest verifiable journal impact factor and its year;
- JCR quartile and year;
- Chinese Academy of Sciences journal partition and version, when verifiable;
- official journal cover;
- author profile and institutional affiliation, using article and official sources;
- scale development, structure, scoring, interpretation, reliability, and validity;
- software/package behavior and parameter definitions;
- methodological standards and recommended diagnostics;
- related studies used to interpret conflicting or convergent findings.

For technical questions, prefer primary sources such as official documentation, original methods papers, scale manuals, and reporting papers.

### Phase B2. Evidence Search Plan and Theory Audit

Before storyboarding, create an explicit evidence-search plan following `guides/evidence-and-theory.md`. At minimum:

1. Identify the scientific concepts, theories, mechanisms, measurement issues, and methods that require external support.
2. Search for a balanced evidence set that includes:
   - the original or seminal theory source;
   - recent systematic reviews or meta-analyses;
   - recent high-quality empirical studies;
   - original methods papers and official software or scale documentation;
   - authoritative burden or guideline sources when relevant.
3. Do not merely reuse references listed by the target paper without checking what they actually support.
4. Record search terms, databases or websites, date searched, source type, and the exact claim each source supports.
5. Build a theory-evidence map before designing the introduction.

For a typical 45-minute deep report, the external evidence set should usually contain at least 12–20 carefully selected sources, in addition to the target paper. Complex theory or method papers may require more. Quality and relevance take priority over numerical quotas.

### Phase B3. Theoretical Foundation Reconstruction

When the paper invokes or implies a theory, framework, model, or complex-system perspective, create a dedicated theoretical-foundation section rather than mentioning the theory in one sentence. Use a function-driven rather than quota-driven approach. A simple paper may require 2–3 theory slides; a genuinely multi-theory paper may require 4–6. Do not split a theory merely to reach a page count. Each theory must explain a specific part of the paper:

1. **Origin and core propositions**: who proposed the theory, when, and what problem it addresses.
2. **Core constructs and relationships**: define the constructs and show the direction of their relationships.
3. **Mechanism or pathway**: explain how the theory predicts the observed phenomenon.
4. **Mapping to the paper**: map each construct to the paper's variables, population, design, and analytical method.
5. **Applicability and limits**: explain what the theory can and cannot justify in this paper.
6. **Alternative or complementary theories**: include them when they materially change interpretation.

A theory slide must cite the original theory source and at least one later application, review, or critique. Every theory included must answer: what it explains in this paper, which variables or developmental mechanisms it maps to, why it supports the study design or analysis, and what it cannot justify.

### Phase C. Scientific Narrative Reconstruction

Build the introduction as one continuous logical chain:

1. **Clinical or scientific importance**: why the problem matters.
2. **Current knowledge**: what is already known.
3. **Evidence gap**: what remains unresolved and why prior approaches are insufficient.
4. **Study entry point**: why this design and method are appropriate.
5. **Research question or hypothesis**: what the study directly tests.

The final transition should be expressible as:

> Because an important clinical/scientific problem remains insufficiently resolved by prior evidence, this study uses a specific design and analytical approach to answer a clearly defined question.

Do not create a fragmented list of background facts. Each slide in the introduction must advance the same line of reasoning.

For a 45-minute report, the introduction and theoretical foundation usually occupy 7–11 slides and 9–12 minutes, but the exact number is determined by the scientific logic rather than a quota. A typical sequence is:

1. burden and clinical significance;
2. target population and developmental or clinical context;
3. core concepts and definitions;
4. theoretical foundation;
5. theory-to-variable mapping;
6. current evidence;
7. limitations of dominant approaches;
8. methodological gap;
9. specific research gap;
10. study response and innovation;
11. conceptual model or analytical pathway;
12. aims, questions, or hypotheses.

Every introduction slide must contain evidence. Use 2–4 concise references per slide when multiple claims are made, and avoid unsupported statements such as “this problem is important” or “few studies have examined this issue.”

### Phase C2. Mandatory Full-Deck Page Blueprint Gate

Before generating any full-deck slide images or building the PPTX, create a complete page-by-page content architecture using `templates/full-deck-blueprint.md`. This is mandatory.

For **every slide**, including title, roadmap, section divider, references, and appendix pages, specify:

1. slide number and section;
2. conclusion-style slide title;
3. the single scientific question the page answers;
4. the one-sentence main takeaway;
5. exact logical role in the deck: what the previous page established, what this page adds, and what the next page will ask;
6. exact on-slide content blocks, including claims, definitions, numbers, annotations, and cautions;
7. evidence source for every claim and the precise PDF page, table, figure, or external reference;
8. academic visual form and why that form fits the logic;
9. whether the page uses a paper figure, native chart, native table, conceptual model, process diagram, comparison matrix, or generated illustration;
10. the planned image2/image_gen full-slide prompt;
11. the image-to-PPT reconstruction plan, including which elements must be native and editable;
12. reference display plan;
13. projection-readability plan;
14. known uncertainties or information that must be labelled “未报告/无法核实.”

The blueprint must read as a coherent scientific argument, not a list of section names. Every page must connect to the page before and after it. Generic titles such as “背景1,” “结果2,” or “讨论” are not sufficient unless followed by a clear conclusion.

#### Mandatory user-facing approval

Before full production:

1. Present the full page list with each slide's title, purpose, content, and logic.
2. Present the four editable style samples and their image2 references.
3. Ask the user to approve both the **content architecture** and the **visual direction**.
4. Do not generate the remaining full-deck image references until approval, unless the user explicitly waives this gate.

After approval, lock the page order, scientific storyline, and visual system. Later additions should be inserted deliberately rather than appended as unrelated pages.

### Phase D. 45-Minute Storyboard

Use `templates/45min-outline.md` and adjust to the article.

Default timing:

| Section | Time | Approximate slides |
|---|---:|---:|
| Title and article profile | 3 min | 3–4 |
| Abstract and roadmap | 2 min | 2 |
| Introduction, theory, and gap | 9–12 min | 7–11 |
| Methods | 10–12 min | 8–12 |
| Results | 12–15 min | 11–15 |
| Discussion and appraisal | 7–9 min | 6–9 |
| Summary | 2 min | 1–2 |
| Implications for user's research | 3–5 min | 3–5 |

Rules:

- Do not force every paper into the same number of slides.
- Give the largest share to methods and results when the paper is analytically complex.
- Move full code, data structures, long model diagnostics, and extended tables to the appendix.
- Use conclusion-style titles rather than generic labels such as “结果1”.
- Main-deck depth is not measured by page count. Do not create extra divider pages or split one argument into several weak pages merely to increase length.
- Use no more than four section-divider slides in the main deck.
- A sparse slide should be revised only when the whitespace is accidental or the reasoning is incomplete. Improve the evidence, enlarge a genuinely useful figure, clarify the mechanism, or merge with an adjacent step. Do not add decorative boxes or tiny screenshots.
- Split a slide when it carries more than one dominant conclusion, when the reading path is unclear, or when body and reference text become unreadable in projection.
- Preserve the approved sample style throughout the deck.

### Phase E. Slide-by-Slide Academic Content Specification

After the full-deck blueprint is approved, create one specification file per slide using `templates/slide-spec.yaml`. The specification is the source of truth for both image generation and PowerPoint reconstruction.

Every slide must define:

- section and slide number;
- conclusion-style title;
- slide purpose and audience question;
- one dominant scientific takeaway;
- previous-slide premise, current-slide contribution, and next-slide transition;
- exact formal text to appear in the final PPTX;
- key numbers, definitions, assumptions, cautions, and interpretation;
- evidence and exact source location;
- selected academic page archetype;
- reading path and information hierarchy;
- source figure/table plan;
- image2/image_gen full-slide prompt;
- generated-asset plan;
- native reconstruction plan;
- reference and source-note plan;
- projection-readability and editability checks.

No slide may move to image generation until its specification is complete. A slide is incomplete when it only states a topic without defining its scientific claim, evidence, and connection to adjacent pages.

### Phase F. Mandatory Per-Slide Image2/Image_Gen Visual Production

The approved blueprint must be visualized **page by page**. Generating only the title page, only four sample pages, or only repeated archetypes is not sufficient.

For every slide in the main deck and appendix:

1. Read the final slide specification.
2. Summarize the scientific content, page logic, and information hierarchy.
3. Write a page-specific image2/image_gen prompt using `prompts/slide-visual-reference-prompt.md`.
4. Generate one complete 16:9 full-slide visual reference for that specific page.
5. Save it with a stable sequence name such as `slide-001-image2-reference.png`.
6. If the page needs complex illustrations, mechanisms, icons, or decorative scientific assets, generate them as separate transparent-background files.
7. Record the prompt, generated file, revision number, and approval status in `templates/slide-production-manifest.csv`.
8. Revise the image when the layout does not clearly express the page's scientific logic.

#### Requirements for the generated full-slide reference

- It must represent the **actual page-specific argument**, not a generic medical background.
- It must follow the approved academic visual system: restrained, editorial, evidence-led, low-saturation, and projection-readable.
- It must show the intended position, relative size, hierarchy, and relationship of title, evidence, interpretation, citations, navigation, and visual assets.
- It may use short validated labels, but generated text is never treated as authoritative.
- Exact formal text is taken from the slide specification and rebuilt natively.
- Exact statistics, P values, confidence intervals, tables, and scientific charts must not be invented by image generation.
- On a result slide, the generated reference should reserve the correct visual anchor for the original figure/table or a native redraw. The final PPTX must use the verified source evidence.
- Generated images must not introduce fake microscopes, DNA, hospital scenes, patients, or decorative icons unrelated to the article's logic.
- A reference page, appendix page, or divider page still requires its own image2 reference so that the entire deck is designed as one coherent sequence.

#### Results-specific generation rule

Use **one figure or one coherent figure panel per slide, followed by one interpretation block**. Multi-panel figures must be split when the panels answer different questions. The page image should make this hierarchy visible:

> one dominant evidence object → how to read it → one conclusion → scientific/clinical meaning → limitation.

Do not generate result pages that stack several unrelated figures, tables, and interpretations.

### Phase G. Image-to-PPT Element-Level Reconstruction

After each page's image2 reference is approved, use the image-to-PPT workflow in `guides/image2-to-editable-ppt-workflow.md`.

The full-slide generated image is a **design blueprint**, never the final flattened slide. Reconstruct it element by element:

1. Set the PPT page size to match the 16:9 reference and establish a coordinate map.
2. Recreate all formal text using native PowerPoint text boxes in Microsoft YaHei.
3. Recreate backgrounds, panels, lines, arrows, labels, navigation, and simple diagrams with native shapes.
4. Recreate tables with native PowerPoint tables or editable shape groups.
5. Recreate charts with native chart objects when exact data are recoverable.
6. Insert verified high-resolution crops from the paper only for complex original figures that cannot be redrawn safely.
7. Use separately generated transparent assets for complex illustrations or icons.
8. Preserve the reference image's position, scale, whitespace, alignment, angle, and visual hierarchy while correcting any image-generation text errors.
9. Do not use the full-slide image as a background or single uneditable picture.
10. Group objects logically and keep every feasible element editable.
11. Add exact citations and source notes from the slide specification.
12. Render the rebuilt slide and compare it side by side with the image2 reference.
13. Correct content errors, misalignment, overflow, clipping, visual drift, and layer-order problems before moving to the next slide.

A slide is complete only when the generated reference exists, the editable reconstruction exists, and both pass the production manifest and QA checks.

### Phase H. Results Presentation

Organize results in the order the research question is answered, usually:

1. participant flow;
2. sample characteristics;
3. variable distributions or measurement properties;
4. primary analysis;
5. secondary analysis;
6. subgroup analysis;
7. sensitivity or robustness analysis;
8. supplementary analysis.

Default result-slide structure:

- **One slide = one source figure, one coherent panel, one native table, or one analytical conclusion.**
- **Evidence area**: one original or reconstructed figure/table/model that is large enough to read in projection.
- **Interpretation area**: one adjacent explanation that teaches the audience how to read the evidence and what it means.

If an original figure contains multiple panels that answer different questions, split those panels across separate slides. Do not place Fig. 2, Fig. 3, and Fig. 4 on the same slide merely because they appear on one PDF page.

The interpretation must answer:

1. What is being shown?
2. How should the audience read it?
3. What is the most important result?
4. What is the direction and magnitude?
5. Is it statistically significant?
6. Is it scientifically or clinically meaningful?
7. Which research question does it answer?
8. What can it not establish?

Do not merely rewrite numbers from the table. Translate them into meaning. Do not place both a native reconstruction and an unreadable thumbnail of the original table on the same slide. Use an enlarged crop, native redraw, or appendix source page instead.

### Phase I. Methods Explanation

For each method, explain:

1. the research question it addresses;
2. why it was chosen;
3. required assumptions;
4. input data;
5. preprocessing;
6. analysis steps;
7. software and package;
8. important parameters;
9. how model quality or fit is evaluated;
10. how the output is interpreted;
11. advantages over simpler alternatives;
12. limitations and common misinterpretations;
13. whether the article reported enough detail.

If the article omits parameter settings, supplement with methodological literature, but explicitly state that the recommendation is external and not necessarily the authors' actual setting.

Use the relevant module in `guides/study-design-modules.md`.

### Phase J. Instruments and Measures

For each scale, instrument, assay, or biomarker, report as applicable:

- full name and abbreviation;
- developer and year;
- target population;
- domains;
- item count;
- response options;
- scoring procedure;
- score range;
- direction of interpretation;
- cutoffs;
- reliability and validity;
- reliability in the present study;
- measurement timing;
- role in the model.

For biomarkers, also report:

- specimen type;
- collection timing;
- fasting status if relevant;
- assay method;
- unit;
- batch handling;
- transformation or standardization;
- reference range if applicable.

For instruments with specialized scoring, such as PROMIS, EORTC, FACT, or MDASI, verify the official scoring method rather than inferring a simple total.

### Phase K. Discussion Reconstruction

Do not translate the discussion paragraph by paragraph. Reorganize it into:

1. main finding;
2. research question answered;
3. agreement with prior studies;
4. disagreement with prior studies;
5. possible explanation or mechanism;
6. clinical significance;
7. theoretical significance;
8. methodological significance;
9. limitations;
10. future research.

Distinguish:

- explanations stated by the authors;
- explanations supported by external literature;
- reasoned presenter interpretation.

Each discussion slide must include visible citations for the comparison study, mechanism, or methodological claim being presented. A statement that a finding is “consistent with previous research” must name and cite the relevant study or review. A mechanism slide should normally draw on the target paper plus 2–4 external sources, but display only the most relevant short citations on-slide; list the full references later.

### Phase L. Methodological Appraisal and Questions

Include a separate section titled “方法学评价与思考” or equivalent.

Evaluate:

- fit between research question and design;
- sampling and representativeness;
- adequacy of sample size for model complexity;
- appropriateness of measurement timing and interval;
- instrument validity;
- missing-data handling;
- attrition;
- confounder control;
- multiple testing;
- effect-size reporting;
- model diagnostics;
- stability and robustness;
- overfitting;
- external validation;
- causal overinterpretation;
- clinical translatability.

Generate at least 3–5 substantive questions. For each question, state:

1. what the issue is;
2. why it matters;
3. how it could be improved or tested.

### Phase M. Implications for the User's Research

Use the fixed mapping framework below. Avoid generic statements.

For each relevant item, present:

> What the paper did → what problem it solved → what value it has for the user's research → what adjustment is needed before adoption.

Map the paper to:

1. research question;
2. theoretical framework;
3. target population;
4. inclusion/exclusion criteria;
5. measurement time points;
6. instruments and scoring;
7. variables and covariates;
8. biomarkers;
9. statistical method;
10. parameter settings;
11. robustness checks;
12. result visualization;
13. manuscript structure;
14. potential standalone paper ideas;
15. aspects that should not be copied directly.

When the user's current research materials are available, ground this section in those materials rather than general memory.

### Phase N. Reproducibility Appendix

For complex analyses, create an appendix following `guides/method-reproduction.md`.

Include as appropriate:

- data structure;
- variable naming;
- mock data;
- preprocessing;
- missing-data handling;
- model code;
- parameter annotations;
- fit evaluation;
- result extraction;
- visualization;
- stability or sensitivity checks;
- common errors;
- adaptation notes for the user's study.

Label code as one of:

- verified author code;
- reconstructed from the article;
- methodological example;
- adapted for the user's study.

### Phase O. Evidence Tracking

Create and maintain `templates/evidence-tracker.csv` for all major slide content.

Track at minimum:

- PPT slide number;
- slide title;
- content type;
- source type;
- source file or URL title;
- PDF page;
- original table/figure number;
- extraction method;
- whether altered or annotated;
- whether data were estimated;
- verification status;
- notes.

Priority for figures and tables:

1. Native chart when exact data are recoverable.
2. Native table when exact table content is recoverable.
3. High-resolution PDF crop when reconstruction would risk error.
4. Never invent exact data from visual appearance.
5. Clearly disclose any visual approximation.

### Phase P. Quality Assurance

Run all required quality reviews:

1. `checklists/storyboard-qa.md`
2. `checklists/style-approval-qa.md`
3. `checklists/per-slide-image2-qa.md`
4. `checklists/image-to-ppt-qa.md`
5. `checklists/academic-qa.md`
6. `checklists/visual-qa.md`
7. `checklists/editability-qa.md`
8. `checklists/content-density-qa.md`

In addition:

- verify that the number of slide specifications, approved image2 references, production-manifest rows, and final PPT slides is identical;
- reject any page that lacks its own page-specific image2 reference;
- render every slide to an image;
- inspect for overflow, clipping, overlap, unreadable references, low-resolution figures, navigation errors, and inconsistent spacing;
- compare rebuilt charts and tables against the paper;
- verify all key numbers twice;
- create a full-deck thumbnail montage and review rhythm, repetition, color, navigation weight, card overuse, and unreadable figures;
- compare the final montage against the approved four-slide sample and the default visual benchmark;
- reject any slide whose decoration carries more visual weight than its evidence;
- reject tiny figures or tables that cannot be read in normal presentation view;
- ensure references and figure/table labels are correct;
- verify that no full-slide design image is being used as an uneditable background;
- compare each rebuilt slide with its image2 reference for hierarchy, spacing, position, and visual rhythm;
- verify that every result slide follows the one-figure/one-interpretation rule unless a documented exception was approved;
- inspect content-area occupancy and identify sparse or visually imbalanced pages;
- verify that every substantive slide has a readable reference footer;
- verify that introduction, theory, methods, discussion, appraisal, and implication slides include claim-level references;
- confirm that theory claims are supported by original and contemporary sources.

## 7. Required Deck Sections

Default main-deck sections:

1. Title slide.
2. Article profile.
3. Journal and author information.
4. Roadmap.
5. Structured abstract.
6. Introduction and background.
7. Theoretical foundation.
8. Theory-to-variable and theory-to-method mapping.
9. Current evidence.
10. Evidence and methodological gap.
11. Research aim or hypotheses.
12. Study design.
13. Participants and setting.
14. Inclusion and exclusion criteria.
15. Sample-size rationale.
16. Data collection process.
17. Quality control.
18. Instruments and measures.
19. Statistical analysis.
20. Results.
21. Discussion.
22. Methodological appraisal.
23. Limitations.
24. Summary.
25. Implications for the user's research.
26. References.
27. Reproducibility appendix.

Sections may be merged or split based on the paper, but the substantive content must not be omitted.

## 8. Article Profile Requirements

Include:

- article title;
- Chinese translation when useful;
- journal name;
- official journal cover;
- impact factor and year;
- JCR quartile and year;
- Chinese Academy of Sciences partition and version, when verifiable;
- publication date;
- online publication date;
- volume, issue, pages or article number;
- DOI;
- first author;
- corresponding author;
- affiliations;
- country/region;
- funding;
- registration.

Author information must come from the article or official institutional sources. Do not infer biography from names.

## 9. Template Learning

When the user supplies an existing deck or reference image:

1. Extract the design system before creating new slides:
   - ratio;
   - margins;
   - title position;
   - navigation height;
   - font sizes;
   - color palette;
   - chart style;
   - table style;
   - footer and references;
   - section-divider style;
   - result-slide pattern.
2. Preserve the user's established visual habits where possible.
3. Repair obvious defects such as crowding, tiny text, inconsistent alignment, and unnecessary decoration.
4. Follow this priority:
   - explicit user-approved template;
   - previously approved deck, especially when the user has stated that it looked better;
   - supplied reference images;
   - default visual benchmark in this skill;
   - a new journal-like design system only when none of the above exists.
5. Content expansion must be an incremental update within the approved style. Do not replace the visual system unless the user explicitly approves a redesign.

## 10. Final Deliverables

Unless the user asks for fewer files, provide:

1. Editable `.pptx` presentation.
2. Approved full-deck page blueprint showing what every page contains and how every page connects logically.
3. Four-slide style sample and approval brief.
4. A complete folder of page-specific image2/image_gen full-slide visual references, one for every slide.
5. Slide-production manifest linking each specification, generated image, reconstructed slide, and QA status.
6. Full-deck thumbnail montage.
7. Content-analysis document.
8. Reproducibility code or method file.
9. Evidence-tracker table.
10. Reference list.
11. Extracted, generated, and redrawn asset folders.
12. Unresolved-issues list.
13. Delivery manifest using `templates/delivery-manifest.md`.

Package the complete project as a folder and optional `.zip` archive.

## 11. Definition of Done

The task is complete only when:

- the deck can support an approximately 45-minute presentation;
- the introduction forms one coherent scientific argument and is sufficiently detailed for a 45-minute report;
- the theoretical foundation is reconstructed with original, contemporary, and critical sources;
- the full page-by-page content architecture was listed and approved before full production, unless explicitly waived;
- the four-slide visual sample was approved before full production, unless explicitly waived;
- every slide has its own page-specific image2/image_gen full-slide visual reference;
- every generated reference has been reconstructed element by element into editable PowerPoint objects;
- the final deck remains consistent with the approved sample and visual benchmark;
- substantive slides use intentional negative space and are not mechanically filled;
- every substantive slide contains a readable citation or source marker;
- methods are explained in sufficient depth;
- results are presented sequentially, normally one figure or one coherent panel per slide with one adjacent interpretation, and are not merely copied;
- the discussion answers the research questions and compares prior evidence;
- a separate methodological appraisal is included;
- implications are specific to the user's research;
- complex methods have a reproducibility appendix;
- all major figures and data have traceable sources;
- the visual system is consistent, lightweight, and not over-cardified;
- no tiny figure or table remains unreadable in projection;
- no more than four divider slides are used unless approved;
- a full-deck montage was reviewed for repetition, rhythm, navigation weight, and color drift;
- text, shapes, tables, and charts are editable where feasible;
- all quality-control checklists have been completed;
- no critical factual uncertainty is hidden.
