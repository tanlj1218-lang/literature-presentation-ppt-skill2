# Method Reproduction Guide

## 1. Purpose

The reproducibility appendix should help the audience understand how the analysis could be implemented. It is not automatically a claim of exact replication.

## 2. Code Provenance Labels

Every code file or slide must be labeled as one of:

- **Author code**: verified public code released by the paper authors.
- **Reconstructed code**: created from the paper's reported method.
- **Methodological example**: generic demonstration of the method.
- **User-study adaptation**: modified for the user's own research.

## 3. Minimum Reproduction Package

Include as appropriate:

1. software and version;
2. package and version;
3. expected data shape;
4. variable dictionary;
5. preprocessing steps;
6. missing-data handling;
7. model syntax;
8. parameter annotations;
9. model-fit or stability checks;
10. output extraction;
11. visualization;
12. interpretation notes;
13. common errors;
14. adaptation limits.

## 4. Parameter Explanation Template

For each important parameter, state:

- parameter name;
- location in code;
- mathematical or practical meaning;
- default value;
- value used in the paper, if reported;
- recommended value from methodological literature, if relevant;
- effect of increasing or decreasing it;
- whether the same value is suitable for the user's study.

## 5. Simulation Code

When the paper has no public code:

- use synthetic data;
- make the data-generation assumptions explicit;
- do not tune synthetic data to mimic the exact reported result unless necessary for teaching;
- state that the output is illustrative;
- separate article-derived settings from assumed settings.

## 6. Complex Methods

### 6.1 Network Analysis

Include:

- data screening;
- correlation type;
- regularization;
- tuning parameter;
- layout;
- centrality;
- bridge metrics;
- predictability;
- bootstrap accuracy;
- case-dropping stability;
- comparison tests if used.

### 6.2 Trajectory Models

Include:

- long-format data;
- time variable;
- candidate class solutions;
- polynomial order;
- starting values;
- fit extraction;
- posterior probabilities;
- class-assignment uncertainty;
- predictors/distal outcomes.

### 6.3 Moderation

Include:

- centering;
- interaction term;
- simple slopes;
- Johnson–Neyman region;
- visualization;
- covariate adjustment.

### 6.4 Simulation Intervention

Include:

- baseline network/model;
- perturbation size;
- direction;
- number of runs;
- activation metric;
- ranking method;
- sensitivity to perturbation assumptions.

## 7. Appendix Slide Pattern

Suggested sequence:

1. Data structure.
2. Preprocessing.
3. Core code.
4. Parameter meaning.
5. Output interpretation.
6. Robustness checks.
7. User-study adaptation.
8. Limitations of the demonstration.
