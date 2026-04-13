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
publication: "ACM Transactions on Computing for Healthcare (ACM Health)"
publication_short: ""

abstract: "Early detection of intrapartum risk enables interventions to potentially prevent or mitigate adverse labor outcomes such as cerebral palsy. Currently, there is no accurate automated system to predict such events to assist with clinical decision-making. To fill this gap, we propose \"Artificial Intelligence (AI) for Modeling and Explaining Neonatal Health\" (AIMEN), a deep learning framework that not only predicts adverse labor outcomes from maternal, fetal, obstetrical, and intrapartum risk factors but also provides the model's reasoning behind the predictions made. The latter can provide insights into what modifications in the input variables of the model could have changed the predicted outcome. We address the challenges of imbalance and small datasets by synthesizing additional training data using Adaptive Synthetic Sampling (ADASYN) and Conditional Tabular Generative Adversarial Networks (CTGAN). AIMEN uses an ensemble of fully-connected neural networks as the backbone for its classification with the data augmentation supported by either ADASYN or CTGAN. AIMEN, supported by CTGAN, outperforms AIMEN supported by ADASYN in classification. AIMEN can predict a high risk for adverse labor outcomes with an average F1 score of 0.784. It also provides counterfactual explanations that can be achieved by changing 2 to 3 attributes on average. Resources available: https://github.com/ab9mamun/AIMEN."

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

url_pdf: https://arxiv.org/pdf/2410.09635
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
