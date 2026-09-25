---
title: "GlyRAG: Context-Aware Retrieval-Augmented Framework for Blood Glucose Forecasting"
abstract: >-
  Accurate blood glucose forecasting using continuous glucose monitoring (CGM) data can support the early prediction of dysglycemic risk. However, current neural-network-based forecasting models treat CGM data as a purely numerical sequence without integrating the contextual information contained in CGM signal morphology. Recently, large language models (LLMs) have shown promise for time-series forecasting, yet their role as agentic context extractors in diabetes care remains largely unexplored.

  In this study, we bridge glucose forecasting and LLM-based contextualization by developing GlyRAG, a context-aware, retrieval-augmented forecasting framework that uses an LLM as a contextualization agent to summarize glucose morphology directly from a timed CGM window. The generated CGM-only narrative is embedded and fused with patch-based glucose representations, while a retrieval module incorporates similar historical training episodes through cross-attention.

  We evaluate GlyRAG on the OhioT1DM and AZT1D datasets for 5-, 30-, and 60-minute forecasting horizons. Compared with strong CGM-only baselines, GPT-4 GlyRAG significantly improves long-horizon root mean square error (RMSE) over PatchTST on both datasets. For example, RMSE decreases from 13.8 to 10.6 at 30 minutes and from 23.1 to 20.2 at 60 minutes on OhioT1DM. LLaMA 3.1 produces smaller but significant long-horizon gains, suggesting that the contextualization pipeline is not limited to GPT-4.

  Clinical error-grid analyses further show that approximately 85 percent of predictions fall within the clinically acceptable Clarke Error Grid Zones A and B. These results suggest that CGM-derived linguistic context and case-based retrieval can improve long-horizon glucose forecasting without requiring additional sensing modalities.
slides: ""
url_pdf: "https://arxiv.org/pdf/2601.05353"
publication_types:
  - "2"
authors: [Shovito Barua Soumma, Hassan Ghasemzadeh]
doi: ""
publication: "IEEE Journal of Biomedical and Health Informatics (IEEE JBHI), September 2026"
featured: false
tags: ["featured"]
categories: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
summary: "GlyRAG combines LLM-generated context, patch-based CGM representations, and retrieval of similar historical episodes to improve long-horizon blood glucose forecasting."
url_dataset: null
url_project: null
publication_short: ""
url_source: "https://arxiv.org/abs/2601.05353"
url_video: null
projects: ["Metabolic-Health", "expand-ai"]
date: 2026-09-25T00:00:00-07:00
url_slides: null
publishDate: 2026-09-25T00:00:00-07:00
url_poster: null
url_code: ""
---
