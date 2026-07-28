---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Gated Adaptation for Continual Learning in Human Activity Recognition"
authors: [Reza Rahimi Azghan, Gautham Krishna Gudur, Mohit Malu, Edison Thomaz, Giulia Pedrielli, Pavan Turaga, Hassan Ghasemzadeh]
date: 2026-07-28T12:00:00-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2026-07-28T12:00:00-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Internet of Things Journal"
publication_short: ""

abstract: "Wearable sensors in Internet of Things (IoT) ecosystems increasingly support applications such as remote health monitoring, elderly care, and smart home automation, all of which rely on robust human activity recognition (HAR). Continual learning systems must balance plasticity (the ability to learn new tasks) with stability (the retention of previously acquired knowledge). However, AI models often exhibit catastrophic forgetting, where learning new tasks degrades performance on earlier ones. This challenge is particularly acute in domain-incremental settings such as HAR, where on-device models must adapt to new subjects with distinct movement characteristics while maintaining accuracy on previously seen subjects without transmitting sensitive data to the cloud. In this work, we propose a parameter-efficient continual learning framework based on channel-wise gated modulation applied to frozen pretrained representations. Our key insight is that adaptation should operate through feature emph{selection} rather than feature emph{generation}: by restricting learned transformations to diagonal scaling of existing features, we preserve the geometric structure of pretrained representations while enabling subject-specific modulation. We provide a theoretical analysis showing that gating implements a bounded diagonal operator that limits representational drift compared to unconstrained linear transformations. Empirically, we demonstrate that freezing the backbone substantially reduces forgetting and that lightweight gates restore the adaptation capacity lost from freezing, achieving both stability and plasticity simultaneously. On the PAMAP2 dataset with 8 sequential subjects, our approach reduces forgetting from 39.7% (trainable backbone) to 16.2% and improves final accuracy from 56.7% to 77.7%, while training less than 2% of model parameters. Our method matches or exceeds standard continual learning baselines without requiring replay buffers or task-specific regularization, confirming that structured diagonal operators provide an effective and efficient mechanism for continual learning under distribution shift."

# Summary. An optional shortened abstract.
summary: "We propose a parameter-efficient continual learning method for wearable human activity recognition. By freezing pretrained features and learning lightweight channel-wise gates, the model adapts to new users while reducing catastrophic forgetting. On PAMAP2, it improved final accuracy from 56.7% to 77.7% and reduced forgetting from 39.7% to 16.2%, while training under 2% of the model’s parameters and requiring no replay buffer."

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

url_pdf: "https://arxiv.org/abs/2603.10046"
url_code: 
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
projects: ["Expand-AI"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
