---
title: "Hybrid Attention Model Using Feature Decomposition and Knowledge Distillation for Blood Glucose Forecasting"
authors: [Ebrahim Farahmand, Shovito Barua Soumma, Nooshin Taheri Chatrudi, Hassan Ghasemzadeh]
date: 2026-04-10T08:01:35-07:00
doi: "10.1109/TMC.2026.3683774"

publishDate: 2026-04-24T01:01:35-07:00
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

publication: "IEEE Transactions on Mobile Computing (IEEE TMC) - April 2026"
publication_short: "IEEE TMC"

abstract: "The availability of continuous glucose monitors (CGMs) as over-the-counter commodities has created a unique opportunity to monitor a person's blood glucose levels, forecast blood glucose trajectories, and provide automated interventions to prevent devastating chronic complications that arise from poor glucose control. However, forecasting blood glucose levels (BGL) is challenging because blood glucose changes consistently in response to food intake, medication intake, physical activity, sleep, and stress. It is particularly difficult to accurately predict BGL from multimodal and irregularly sampled mobile sensor data and over long prediction horizons. Furthermore, these forecasting models need to operate in real-time on edge devices to provide in-the-moment interventions. To address these challenges, we propose GlucoNet1, an AI model to forecast blood glucose patterns using sensor data about behavioral and physiological health. GlucoNet devises a feature decompositionbased lightweight transformer model that incorporates patients' behavioral and physiological data (e.g., blood glucose, diet, medication) and transforms sparse and irregular patient data (e.g., diet and medication intake data) into continuous features using a mathematical model, facilitating better integration with the BGL signals. Given the non-linear and non-stationary nature of blood glucose signals, we propose a decomposition method to extract both low-frequency (long-term) and high-frequency (short-term) components from the BGL signals, thus enabling the model to capture complex glucose dynamics for accurate forecasting. To reduce the computational complexity of transformer-based predictions, we propose to employ knowledge distillation (KD) to compress the transformer model. Our comprehensive analysis on two real-world T1D cohorts demonstrates that GlucoNet achieves a 35% improvement in RMSE, a 33% improvement in MAE, and a 62% reduction in the number of parameters over state of the art work such as PatchTST on the OhioT1DM dataset (12 patients), while additional experiments on the AZT1D dataset (25 patients), together with extensive ablation and robustness analyses, further demonstrate its generalizability and stability. These results underscore GlucoNet's potential as a compact and reliable tool for real-world diabetes prevention and management."

# Summary. An optional shortened abstract.
summary: "A hybrid attention framework designed for accurate and efficient blood glucose forecasting using multimodal data using feature decomposition and knowledge distillation"

tags: ["featured"]
categories: []
featured: true


url_pdf: https://ieeexplore.ieee.org/abstract/document/11481169
url_code: https://github.com/shovito66/GlucoNet
url_dataset:
url_poster:
url_project:
url_slides: 
url_source:
url_video: 

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [Metabolic-Health, human-in-the-loop-learning]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

