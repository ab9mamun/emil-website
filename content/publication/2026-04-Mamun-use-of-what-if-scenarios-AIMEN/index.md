---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Use of What-if Scenarios to Help Explain Artificial Intelligence Models for Neonatal Health"
authors: [Abdullah Mamun, Lawrence D. Devoe, Mark I. Evans, David W. Britt, Judith Klein-Seetharaman, Hassan Ghasemzadeh]
date: 2026-04-13T12:00:00-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2026-04-13T12:00:00-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "ACM Transactions on Computing for Healthcare (ACM Health) - April 2026"
publication_short: ""

abstract: "Early detection of intrapartum risks enables timely interventions to prevent or mitigate adverse labor outcomes such as cerebral palsy. However, accurate automated systems to support clinical decision-making during delivery are currently lacking. To address this gap, we propose Artificial Intelligence for Modeling and Explaining Neonatal Health (AIMEN), a deep learning framework that predicts adverse labor outcomes from maternal, fetal, obstetrical, and intrapartum factors while providing interpretable reasoning behind its predictions. AIMEN reveals how specific modifications to input variables could alter predicted outcomes, enhancing clinical insight. To address class imbalance and limited sample size, AIMEN employs Conditional Tabular GAN (CTGAN) for data augmentation. This process includes synthetic data generation, and we investigate in detail properties such as relaxing feature bounds for a subset of training points to explore slightly out-of-range physiological values, and applying silhouette-score-based filtering to increase the separability of synthetic samples. AIMEN uses an ensemble of fully connected neural networks for classification and outperforms state-of-the-art models such as XGBoost, TabNet, DANet, and LightGBM, achieving an average F1 score of 0.784 in predicting high-risk deliveries. Moreover, AIMEN generates counterfactual explanations that identify actionable changes involving only two to three attributes on average. Resources: https://github.com/ab9mamun/AIMEN."

# Summary. An optional shortened abstract.
summary: "We propose Artificial Intelligence for Modeling and Explaining Neonatal Health (AIMEN), a deep learning framework that predicts adverse labor outcomes from risk factors and provides the model's reasoning."

tags: ["featured"]
categories: []
featured: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://dl.acm.org/doi/10.1145/3814951
url_code: https://github.com/ab9mamun/AIMEN
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
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
