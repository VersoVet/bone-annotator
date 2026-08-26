# Cost and Quality Assurance in Crowdsourcing Workflows (Extended Abstract)

**Auteurs** : Loïc Hélouët, Zoltan Miklos, Rituraj Singh
**Année** : 2021
**DOI** : 10.3390/e28040377

## Résumé

Despite recent advances in artificial intelligence and machine learning, many tasks still require human contributions. With the growing availability of Internet, it is now possible to hire workers on crowdsourcing marketplaces. Many crowdsourcing platforms have emerged in the last decade: Amazon Mechanical Turk, Figure Eight 2 , Wirk 3 , etc. A platform allows employers to post tasks, that are then realized by workers hired from the crowd in exchange for some incentives [3, 19]. Common tasks include image annotation, surveys, classification, recommendation, sentiment analysis, etc. [7]. The existing platforms support simple, repetitive and independent micro-tasks which require a few minutes to an hour to complete. However, many real-world problems are not simple micro-tasks, but rather complex orchestrations of dependent tasks, that process input data and collect human expertize. Existing platforms provide interfaces to post micro-tasks to a crowd, but cannot handle complex tasks. The

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## HITL method families: required human input, indicative operational cost, core risks, and common failure modes.

| Method Family | Human Input Required | Typical Cost | Key Risks | Common Failure Modes |
| --- | --- | --- | --- | --- |
| Active learning | • Expert/oracle labels • Verification of uncertain samples • Occasional sampling-policy guidance | Medium-high | • Sampling bias • Annotator fatigue • Privacy exposure in queried items | • Myopic query strategy • Query/deployment distribution mismatch • Annotation artifacts and overfitting to ambiguous cases |
| Reinforcement learning from human feedback (RLHF)/preference optimization | • Pairwise preferences and rankings • Critiques and demonstrations • Periodic human policy evaluation | High | • Reward hacking/specification gaming • Norm/preference drift • Inconsistent rater judgments | • Optimization to proxy signals • Truthfulness/helpfulness degradation from over-optimization • Collapse to overly safe but uninformative outputs |
| Interactive machine learning (IML)/human-guided model steering | • Continuous corrections and constraints • Concept labeling • Interactive debugging | Medium-high | • Cognitive overload • Confirmation bias • Inconsistent operator corrections | • Non-stationary guidance • Oscillatory updates • Local patches that degrade global performance |
| Human-in-the-loop data curation and labeling pipelines | • Labeling and adjudication • Guideline and gold-set design • Iterative error analysis/refinement | Medium-high | • Guideline-encoded bias • Low inter-annotator agreement • Sensitive-information leakage | • Label inconsistency/shortcutting • Silent label noise • Dataset shift as annotation policy evolves |
| Disagreement-aware label aggregation and adjudication | • Multi-annotator labels • Annotator metadata and disagreement rationale • Expert adjudication for contested items | Medium | • False consensus from majority voting • Minority-view suppression • Unresolved ambiguity propagation | • Overconfident hard labels for ambiguous items • Escalation bottlenecks • Persistent disagreement loops |
| Post-hoc human validation/escalation (human-on-the-loop) | • Output review and approval/override • Exception handling • Escalation on low-confidence/high-risk cases | Low-medium | • Automation bias/rubber-stamping • Throughput bottlenecks under peak load • Ambiguous accountability | • High-risk misses under time pressure • Inconsistent overrides • Alert fatigue and threshold miscalibration |
| Human-guided prompt workflows for generative AI | • Prompt drafting and refinement • Structured output checking • Selective fact-checking | Low-medium | • Prompt injection • Hallucinations and brittle prompt behavior • Confidentiality leakage through prompts | • Plausible but incorrect outputs • Poor reproducibility • Failure under adversarial inputs |

## Application domains: typical human oversight points, regulatory/standards pressure, evaluation metrics, and common implementation pitfalls.

| Domain | Human Oversight Points | Regulation/Standards Pressure | Common Evaluation Metrics | Common Pitfalls |
| --- | --- | --- | --- | --- |
| Healthcare (clinical decision support, imaging, triage) | • Data curation/labeling • Clinician confirmation or override • Escalation and audit trails | High (patient safety, medical software/device regulation, privacy) | Sensitivity/ specificity, AUROC, calibration (ECE/Brier), subgroup performance, time-to-decision | • Site-level dataset shift • Spurious correlates • Over-trust and weak workflow integration |
| Autonomous systems (robots, drones, AVs) | • Safety-case design and validation • Human takeover/teleoperation • Incident review | High (safety certification varies by subsystem/jurisdiction) | Safety violations, disengagements/takeovers, edge-case robustness, latency, scenario coverage | • Operator over-reliance • Delayed takeover/handover failure • Untested corner cases and reward hacking |
| Cybersecurity (detection, triage, response) | • Alert triage • Analyst feedback loops • Playbook approval and post-incident tuning | Medium-high (compliance and critical-infrastructure requirements) | Precision/recall at low FPR, time-to-detect/respond, analyst workload, false-positive burden | • Alert fatigue • Adversarial adaptation • Feedback loops that overfit to SOC routines |
| Finance (lending, fraud, risk) | • Model governance and audits • Human review of borderline decisions • Adverse-action explanation checks | High (fair lending, consumer protection, auditability) | AUC/KS, expected loss, calibration, fairness metrics, stability/PSI, manual-review rate | • Bias amplification/proxy discrimination • Concept drift • Explanation mismatch and incentive gaming |
| Legal/public sector (decision support) | • Policy design and human adjudication • Appeals and override mechanisms • Transparency documentation/reporting | High (due process, transparency, accountability) | Error rates by group, calibration, procedural fairness, appeal outcomes, documentation completeness | • Legitimacy/opacity concerns • Automation bias from historical outcomes • Unclear accountability ownership |
| Industrial quality/manufacturing inspection | • Acceptance-criteria and labeling design • Human re-check of uncertain items • Root-cause feedback loop | Medium (quality/safety standards vary by product) | Defect detection, false rejects, throughput, inspection cost, drift monitoring | • Evolving defect taxonomy • Inconsistent labels/inspection shortcuts • Sensitivity to material/lighting variation |

## Technical approaches for incorporating human input in HITL AI systems. The table summarizes the primary mechanisms through which human knowledge, feedback, and oversight are integrated into machine learning workflows, along with the type of human contribution required and representative studies from the literature.

| Approach | Mechanism | Human Input Type | Key References |
| --- | --- | --- | --- |
| Active Learning | Strategic selection of informative instances for labeling | Annotations, labels | [19,21] |
| Uncertainty Sampling | Query instances where model confidence is lowest | Correction, validation | [22,23] |

## Trust calibration states in human-AI interaction, associated risks, and interventions for achieving appropriate calibration.

| Trust State | Characteristics | Risks | Interventions |
| --- | --- | --- | --- |
| Over-trust | Excessive reliance; uncritical acceptance; reduced vigilance | Automation bias; error propagation; skill degradation | XAI [20]; error exposure; confidence displays [11] |
| Well-calibrated | Context-aware reliance; appropriate skepticism; adaptive behavior | Optimal state | Continuous calibration; transparent uncertainty [55] |
| Under-trust | Excessive skepticism; rejection of valid outputs | Inefficiency; missed AI benefits; cognitive overload | Demonstrated reliability; transparency [56] |

## Application domains for HITL AI systems with characteristic configurations and challenges. High-risk domains typically require tighter human oversight due to potential consequences of errors, while medium-risk domains may employ more flexible configurations balancing oversight with operational efficiency.

| Domain | Risk Level Typical Loop Config | Key Challenge | Representative Studies |
| --- | --- | --- | --- | --- |
| Healthcare | High | In-the-Loop | Clinical accountability; diagnostic validation | [26,78-80] |
| Autonomous Systems High | On-the-Loop | Real-time safety; human takeover capability | [28,29,39,57] |
| Cybersecurity | High | Along-the-Loop | Scalability; adversarial adaptation | [18,81-83] |
| Finance | High | Over-the-Loop | Regulatory compliance; fraud detection | [45,48,84] |
| Education | Medium | In-the-Loop | Fairness; pedagogical quality; assessment validity | [9,85-87] |
| Manufacturing | Medium | On-the-Loop | Efficiency; quality inspection accuracy | [13,23,41] |

## Open challenges and future research directions in HITL AI. The table summarizes persistent limitations affecting HITL system effectiveness and outlines research directions that may address these challenges across technical, cognitive, organizational, and societal dimensions.

| Challenge | Description | Current Approaches | Future Research Directions |
| --- | --- | --- | --- |
| Scalability of Human Oversight | Human capacity insufficient for AI decision volume at scale | Active learning; tiered oversight; sampling-based audits | Uncertainty quantification; AI self-assessment; team configurations |
| Human Cognitive Limitations | Fatigue, attention lapses, cognitive biases affect oversight quality | Workload management; training programs; interface design | Adaptive systems responding to cognitive state; sustainable work structures |
| Conflicting Human Feedback | Disagreement among annotators and stakeholders | Majority voting; weighted aggregation; quality metrics | Deliberative approaches; disagreement characterization; consensus methods |
| Adversarial Manipulation | Social engineering targeting human components | Technical security measures; access controls | HITL-specific threat models; manipulation detection; procedural safeguards |
| Adaptive Architectures | Fixed configurations may not match varying needs | Predetermined human involvement points | Risk-based dynamic adjustment; self-regulating systems; meta-level oversight |
