---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Optimal Policy for Deployment of Machine Learning Models on Energy-Bounded Systems"
authors: [Iman Mirzadeh, Hassan Ghasemzadeh]
date: 2020-04-21
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2020-04-21T00:03:39-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "International Joint Conference on Artificial Intelligence (IJCAI), 2020"
publication_short: ""

abstract: "With the recent advances in both machine learning and embedded systems research, the demand to deploy computational models for real-time execution on edge devices has increased substantially. Without deploying computational models on edge devices, the frequent transmission of sensor data to the cloud results in rapid battery draining due to the energy consumption of wireless data transmission. This rapid power dissipation leads to a considerable reduction in the battery lifetime of the system, therefore jeopardizing the real-world utility of smart devices. It is well-established that for difficult machine learning tasks, models with higher performance often require more computation power and thus are not power-efficient choices for deployment on edge devices. However, the trade-offs between performance and power consumption are not well studied. While numerous methods (e.g., model compression) have been developed to obtain an optimal model, these methods focus on improving the efficiency of a ''single'' model. In an entirely new direction, we introduce an effective method to find a combination of ''multiple''  models that are optimal in terms of power-efficiency and performance by solving an optimization problem in which both performance and power consumption are taken into account. Experimental results demonstrate that on the ImageNet dataset, we can achieve a 20% energy reduction with only 0.3% accuracy drop compared to Squeeze-and-Excitation Networks.  Compared to a pruned convolutional neural network for human activity recognition, while consuming 1.7% less energy, our proposed policy achieves 1.3% higher accuracy."

# Summary. An optional shortened abstract.
summary: " "

tags: ["featured"]
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://www.dropbox.com/s/1gac1vx18nm6yup/IJCAI20_OptDeploy%20%2817%29.pdf?dl=0
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
projects: ["Edge-AI"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
