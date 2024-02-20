---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Estimating Average Treatment Effects via Orthogonal Regularization"
event: EMIL Summer'23 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  Conducting a causal inference study with observational data is a difficult endeavor that necessitates a slew of assumptions. One of the most common assumptions is "ignorability," which argues that given a patient (X), the pair of outcomes (Y0, Y1) is independent of the actual treatment received (T). This assumption is used in this paper to develop an AI model for calculating the Average Treatment Effect (ATE).
abstract: "Decision-making often requires accurate estimation of treatment effects from observational data. This is challenging as outcomes of alternative decisions are not observed and have to be estimated. Previous methods estimate outcomes based on unconfoundedness but neglect any constraints that unconfoundedness imposes on the outcomes. In this paper, we propose a novel regularization framework for estimating average treatment effects that exploits unconfoundedness. To this end, we formalize unconfoundedness as an orthogonality constraint, which ensures that the outcomes are orthogonal to the treatment assignment. This orthogonality constraint is then included in the loss function via a regularization. Based on our regularization framework, we develop deep orthogonal networks for unconfounded treatments (DONUT), which learn outcomes that are orthogonal to the treatment assignment. Using a variety of benchmark datasets for estimating average treatment effects, we demonstrate that DONUT outperforms the state-of-the-art substantially."
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2023-09-06T13:30:00-07:00
date_end: 2023-09-06T15:00:00-07:00
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
url_pdf: "https://arxiv.org/pdf/2101.08490.pdf"
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
