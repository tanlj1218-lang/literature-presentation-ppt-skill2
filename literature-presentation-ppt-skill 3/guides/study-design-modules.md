# Study-Design Modules

Activate the modules that match the paper. More than one module may apply.

## 1. Cross-Sectional Study

Explain:

- sampling frame and recruitment;
- representativeness and nonresponse;
- exposure and outcome timing;
- scale reliability in the current sample;
- univariable and multivariable sequence;
- confounder selection;
- collinearity diagnostics;
- model form and link function;
- effect-size interpretation;
- limits on temporal and causal inference.

Appraisal prompts:

- Was convenience sampling used?
- Were important confounders omitted?
- Were continuous variables unnecessarily categorized?
- Was a cross-sectional mediation model interpreted causally?

## 2. Longitudinal Cohort Study

Explain:

- cohort entry;
- follow-up time points and intervals;
- clinical rationale for timing;
- loss to follow-up;
- repeated-measure correlation;
- time-varying versus time-invariant covariates;
- mixed models, GEE, latent growth, or related approaches;
- missing-data assumptions;
- temporal ordering;
- sensitivity to unequal intervals.

Appraisal prompts:

- Are intervals compatible with the selected model?
- Was attrition differential?
- Did the analysis distinguish within-person from between-person effects?

## 3. Randomized Controlled Trial

Explain:

- random-sequence generation;
- allocation concealment;
- blinding;
- comparator;
- intervention components, dose, and fidelity;
- adherence;
- primary and secondary outcomes;
- sample-size assumptions;
- intention-to-treat and per-protocol analyses;
- missing data;
- adverse events;
- absolute and relative effect sizes.

Appraisal prompts:

- Was the trial powered for the reported primary outcome?
- Was multiplicity controlled?
- Was intervention fidelity measured?

## 4. Symptom Network Analysis

Explain:

- nodes and node level: total score, domain, or item;
- network type: Gaussian graphical model, Ising, mixed graphical model, Bayesian, temporal, or other;
- edge meaning;
- preprocessing and variable standardization;
- redundant-node checks such as goldbricker/UVA when used;
- regularization and EBICglasso;
- EBIC tuning parameter gamma;
- layout algorithm;
- strength or expected influence;
- bridge centrality;
- predictability;
- edge-weight accuracy bootstrap;
- case-dropping bootstrap and CS coefficient;
- edge/centrality difference tests;
- network comparison tests;
- limitations of centrality-driven intervention claims.

Interpretation order:

1. Overall structure.
2. Strongest edges.
3. Central nodes.
4. Bridge nodes.
5. Predictability.
6. Accuracy and stability.
7. Clinical meaning.
8. Non-causal limitations.

Key cautions:

- Centrality is not automatically causal importance.
- Small edge differences may not be statistically stable.
- Cross-sectional networks do not provide temporal direction.
- Node redundancy can distort centrality.

## 5. Cross-Lagged or Temporal Network Analysis

Explain:

- number and spacing of waves;
- autoregressive paths;
- cross-lagged paths;
- contemporaneous paths if modeled;
- between-person versus within-person effects;
- baseline adjustment;
- regularization;
- stationarity assumptions;
- unequal interval implications;
- short-term versus long-term path interpretation;
- directionality versus causality.

Appraisal prompts:

- Are intervals equal enough for direct coefficient comparison?
- Does the model separate stable between-person differences?
- Are there enough waves for the chosen temporal model?

## 6. Trajectory Models: GBTM, LCGA, GMM, LGMM

Explain:

- why population heterogeneity is expected;
- number of waves;
- timing and spacing;
- functional form: linear, quadratic, cubic, spline;
- distributional assumption;
- random effects and within-class variance;
- model-estimation strategy and starting values;
- class-number comparison;
- AIC, BIC, adjusted BIC;
- entropy;
- LMR and BLRT;
- average posterior probability;
- odds of correct classification when reported;
- smallest class proportion;
- substantive interpretability;
- predictors of class membership;
- three-step methods, R3STEP, BCH, or related approaches;
- overextraction and local maxima.

Interpretation order:

1. Model selection process.
2. Final class solution.
3. Shape of each trajectory.
4. Class prevalence.
5. Classification quality.
6. Predictors or distal outcomes.
7. Clinical relevance.
8. Uncertainty of class assignment.

## 7. Latent Profile Analysis

Explain:

- indicators and scale level;
- local independence;
- variance/covariance constraints;
- model-estimation strategy;
- class-number fit indices;
- entropy and posterior probability;
- class size;
- naming based on relative patterns rather than arbitrary labels;
- auxiliary variables and three-step methods;
- distinction from longitudinal trajectory models.

## 8. Mediation and Moderation

Explain:

- X, M/W, and Y;
- temporal ordering;
- direct, indirect, total, and interaction effects;
- centering or standardization;
- bootstrap confidence intervals;
- simple slopes;
- Johnson–Neyman region;
- conditional indirect effects;
- confounder control;
- causal limits in observational and cross-sectional data.

## 9. Moderated Network Analysis

Explain:

- main-effect network;
- interaction terms;
- moderator scaling;
- regularization;
- AND versus OR rule;
- interaction-edge interpretation;
- simple-slope or conditional-edge plots;
- Johnson–Neyman analysis when applicable;
- covariates;
- bootstrap or stability assessment;
- multiplicity and overfitting risk.

## 10. Network Intervention Simulation

Explain:

- simulation objective;
- intervention versus prevention simulation;
- node perturbation direction;
- perturbation size and step;
- number of iterations;
- network activation outcome;
- ranking criterion;
- uncertainty or sensitivity analysis;
- whether results are based on cross-sectional or temporal networks;
- difference between simulated influence and proven intervention efficacy.

Mandatory caution slide:

> Simulation identifies theoretically influential targets under model assumptions. It does not replace experimental validation.

## 11. Structural Equation Modeling

Explain:

- measurement and structural models;
- latent variables and indicators;
- model identification;
- estimator;
- handling of non-normal or ordinal data;
- CFI, TLI, RMSEA, SRMR, chi-square;
- standardized paths;
- indirect effects;
- modification indices;
- alternative/equivalent models;
- measurement invariance if longitudinal or multigroup.

## 12. Systematic Review and Meta-Analysis

Explain:

- review question and eligibility;
- databases and search dates;
- screening process;
- data extraction;
- risk-of-bias assessment;
- effect measure;
- fixed versus random effects;
- heterogeneity;
- prediction interval;
- subgroup analysis;
- meta-regression;
- sensitivity analysis;
- small-study effects/publication bias;
- certainty of evidence when assessed.

## 13. Qualitative Study

Explain:

- paradigm and methodology;
- sampling strategy;
- sample size and saturation;
- data-collection format;
- interviewer position and reflexivity;
- coding and theme development;
- multiple coders or consensus;
- credibility, dependability, confirmability, transferability;
- participant quotations and negative cases.

## 14. Prediction Model or Machine Learning

Explain:

- prediction target and intended use;
- candidate predictors;
- sample-size considerations and events per parameter;
- missing-data handling;
- data splitting or resampling;
- feature selection;
- hyperparameter tuning;
- class imbalance;
- discrimination;
- calibration;
- overall performance;
- decision-curve or clinical utility;
- internal and external validation;
- overfitting;
- model interpretability.

## 15. Mixed-Methods Study

Explain:

- mixed-methods design type;
- priority and sequence;
- quantitative component;
- qualitative component;
- integration point;
- joint display;
- how one component informs the other;
- whether integration changed the final inference.
