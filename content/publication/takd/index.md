---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Improved Knowledge Distillation via Teacher Assistant"
subtitle: ""
abstract: "Despite the fact that deep neural networks are powerful models and achieve appealing results on many tasks, they are too gigantic to be deployed on edge devices like smart-phones or embedded sensor nodes. There has been efforts to compress these networks, and a popular method is knowledge distillation, where a large (teacher) pre-trained network is used to train a smaller ( student) network. However, in this paper, we show that the student network performance degrades when the gap between student and teacher is large. Given a fixed student network, one cannot employ an arbitrarily large teacher, or in other words, a teacher can effectively transfer its knowledge to students up to a certain size, not smaller. To alleviate this shortcoming, we introduce multi-step knowledge distillation which employs an intermediate-sized network (teacher assistant) to bridge the gap between the student and the teacher. Moreover, we study the effect of teacher assistant size and extend the framework to multi-step distillation. Theoretical analysis and extensive experiments on CIFAR-10, CIFAR-100 and ImageNet datasets and on CNN and ResNet architectures substantiate the effectiveness of our proposed approach."

summary: " "
authors: [Iman Mirzadeh, Mehrdad Farajtabar, Ang Li, Hassan Ghasemzadeh]
tags: ["featured"]
categories: []
date: 2019-11-10T19:06:19-08:00
lastmod: 2019-11-10T19:06:19-08:00
featured: true
draft: false
publication: AAAI Conference on Artificial Intelligence (AAAI), 2020
publication_types: ["1"]

url_pdf: https://arxiv.org/abs/1902.03393
url_code: https://github.com/imirzadeh/Teacher-Assistant-Knowledge-Distillation
url_video: https://www.youtube.com/watch?v=ueUAtFLtukM
image: "takd-main.png"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: "smart"
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["Edge-AI"]
---
