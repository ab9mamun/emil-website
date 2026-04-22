---
title: "Self-Supervised Learning and Opportunistic Inference for Continuous Monitoring of Freezing of Gait in Parkinson’s Disease"
authors: [Shovito Barua Soumma, Daniel Peterson, Shyamal Mehta, Hassan Ghasemzadeh]
date: 2026-03-24T08:01:35-07:00
doi: "10.1145/3802589"

publishDate: 2026-03-24T08:01:35-07:00
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

publication: "ACM Transactions on Computing for Healthcare (ACM Health) - March 2026"
publication_short: "ACM Health"

abstract: "Parkinson's disease (PD) significantly affects patients’ quality of life through debilitating motor symptoms, such as Freezing of Gait (FoG). Continuous, in-home monitoring of FoG is essential for timely clinical intervention but remains challenging due to high power consumption, annotation cost, and the controlled environments required by current wearables. We introduce LIFT-PD, a novel self-supervised learning (SSL) framework for real-time, patient-independent FoG detection that uniquely utilizes a single waist-worn accelerometer—an approach traditionally considered less optimal due to weaker gait signatures. LIFT-PD leverages SSL on unlabeled data collected from uncontrolled, real-world settings and employs a novel Differential Hopping Windowing Technique (DHWT) to address gait variability and dataset imbalance. Additionally, an opportunistic inference module selectively activates the deep learning model only during patient movement, significantly reducing power consumption and enabling continuous monitoring (>48 hours). Experimental results show that LIFT-PD achieves a 7.25% increase in precision and 4.4% improvement in accuracy compared to supervised and semi-supervised baseline models while requiring approximately 40% fewer labeled training samples. Evaluations across diverse patient characteristics-including severity, medication state, age, and gender-confirm the model's robustness and clinical applicability, positioning LIFT-PD as a practical, energy-efficient, and scalable solution for continuous real-world FoG monitoring in PD."

# Summary. An optional shortened abstract.
summary: "An innovative self-supervised learning framework developed for real-time detection of Freezing of Gait (FoG) in Parkinson's Disease (PD) patients, using a single triaxial accelerometer"

tags: ["featured"]
categories: []
featured: true


url_pdf: https://dl.acm.org/doi/10.1145/3802589
url_code: https://github.com/shovito66/LIFT-PD
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
projects: [Gait-and-Mobility, human-in-the-loop-learning]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

