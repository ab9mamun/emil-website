---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Loss landscapes and optimization in over-parameterized non-linear systems and neural networks"
event: EMIL Spring'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  "This paper proposes a framework for better understanding what is happening behind the training of over-parameterized neural nets, for which the objective function is not convex, not even locally"
abstract: "The success of deep learning is due, to a large extent, to the remarkable effectiveness of gradientbased optimization methods applied to large neural networks. The purpose of this work is to propose a modern view and a general mathematical framework for loss landscapes and efficient optimization in over-parameterized machine learning models and systems of non-linear equations, a setting that includes over-parameterized deep neural networks. Our starting observation is that optimization problems corresponding to such systems are generally not convex, even locally. We argue that instead they satisfy PL∗, a variant of the Polyak- Lojasiewicz condition on most (but not all) of the parameter space, which guarantees both the existence of solutions and efficient optimization by (stochastic) gradient descent (SGD/GD). The PL∗ condition of these systems is closely related to the condition number of the tangent kernel associated to a non-linear system showing how a PL∗-based non-linear theory parallels classical analyses of over-parameterized linear equations. We show that wide neural networks satisfy the PL∗ condition, which explains the (S)GD convergence to a global minimum. Finally we propose a relaxation of the PL∗ condition applicable to almost over-parameterized systems."
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-04-09T13:30:00-07:00
date_end: 2024-04-09T15:00:00-07:00
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
url_pdf: "https://arxiv.org/abs/2003.00307"
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
