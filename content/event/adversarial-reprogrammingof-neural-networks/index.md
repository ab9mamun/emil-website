
---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Adversarial Reprogramming of Neural Networks"
event:
event_url:
location:
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "Paper Review: <i>Elsayed, G.F., Goodfellow, I.J., & Sohl-Dickstein, J. (2019). Adversarial Reprogramming of Neural Networks. ICLR.</i>"
abstract: "Deep neural networks are susceptible to adversarial attacks. In computer vision, well-crafted  perturbations to images can cause neural networks to make mistakes such as confusing a cat with a  computer. Previous adversarial attacks have been designed to degrade performance of models or cause machine learning models to produce specific outputs chosen ahead of time by the attacker. We  introduce attacks that instead reprogram the target model to perform a task chosen by the attacker  without the attacker needing to specify or compute the desired output for each test-time input.  This attack finds a single adversarial perturbation, that can be added to all test-time inputs to a machine learning model in order to cause the model to perform a task chosen by the  adversary-even if the model was not trained to do this task. These perturbations can thus be considered a program for the new task. We demonstrate adversarial reprogramming on six ImageNet classification models, repurposing these models to perform a counting task, as well as  classification tasks: classification of MNIST and CIFAR-10 examples presented as inputs to theImageNet model"

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2020-01-27T12:00:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2020-01-27

authors: [ramesh-sah]
tags: []

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your talk folder or a URL.
url_slides:

url_code:
url_pdf: "https://arxiv.org/abs/1806.11146"
url_video:

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
