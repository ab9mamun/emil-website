---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Learning Linear Causal Representations from Interventions under General Nonlinear Mixing"
event: EMIL Spring'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  "This paper proposes a contrastive learning based approach to solve the problem of causal representation learning, under the assumption of linear-gaussian representation, and a non-linear mixing function"
abstract: "We study the problem of learning causal representations from unknown, latent interventions in a general setting, where the latent distribution is Gaussian but the mixing function is completely general. We prove strong identifiability results given unknown single-node interventions, i.e., without having access to the intervention targets. This generalizes prior works which have focused on weaker classes, such as linear maps or paired counterfactual data. This is also the first instance of identifiability from non-paired interventions for deep neural network embeddings and general causal structures. Our proof relies on carefully uncovering the highdimensional geometric structure present in the data distribution after a non-linear density transformation, which we capture by analyzing quadratic forms of precision matrices of the latent distributions. Finally, we propose a contrastive algorithm to identify the latent variables in practice and evaluate its performance on various tasks."
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-03-12T13:30:00-07:00
date_end: 2024-03-12T15:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2022-06-14T17:50:20-07:00

authors: [reza-rahimi-azghan]
tags: []

# Is this a featured event? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
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

# Optional filename of your slides within your event's folder or a URL.
url_slides: pres.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2306.02235"
url_video:

# Markdown Slides (optional).
#   Associate this event with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
