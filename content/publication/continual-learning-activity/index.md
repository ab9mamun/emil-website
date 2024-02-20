---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Continual Learning for Activity Recognition"
authors: [Ramesh Sah, Seyed Iman Mirzadeh, Hassan Ghasemzadeh]
date: 2022-04-1T12:22:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-04-01T12:22:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Engineering in Medicine and Biology Conference (EMBC), 2022"
publication_short: "EMBC"

abstract: "The recent success of deep neural networks in
prediction tasks on wearable sensor data is evident. However,
in more practical online learning scenarios, where new data
arrive sequentially, neural networks suffer severely from the
“catastrophic forgetting“ problem. In real-world settings, given
a pre-trained model on the old data, when we collect new
data, it is practically infeasible to re-train the model on
both old and new data because the computational costs will
increase dramatically as more and more data arrive in time.
However, if we fine-tune the model only with the new data
because the new data might be different from the old data,
the neural network parameters will change to fit the new
data. As a result, the new parameters are no longer suitable
for the old data. This phenomenon is known as catastrophic
forgetting, and continual learning research aims to overcome this
problem with minimal computational costs. While most of the
continual learning research focuses on computer vision tasks,
implications of catastrophic forgetting in wearable computing
research and potential avenues to address this problem have
remained unexplored. To address this knowledge gap, we study
continual learning for activity recognition using wearable sensor
data. We show that the catastrophic forgetting problem is a
critical challenge for the real-world deployment of machine
learning models for wearable sensor data. Moreover, we show
that the catastrophic forgetting problem can be alleviated by
employing various training techniques."

# Summary. An optional shortened abstract.
summary: "Continual learning formulation in the context of sensor systems."

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

url_pdf: https://drive.google.com/file/d/1hbaeB0OVxynZj0ih2OmAQsGMbMBBUM0t/view?usp=sharing
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
projects: ["Computational-Autonomy"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
