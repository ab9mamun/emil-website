
---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Similarity of Neural Network Representations Revisited"
event:
event_url:
location:
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "Paper Review: Kornblith, <i> S., Norouzi, M., Lee, H., & Hinton, G.E. (2019). Similarity of Neural Network Representations Revisited. ICML</i>"
abstract: "Recent work has sought to understand the behavior of neural networks by comparing 
representations between layers and between different trained models. We examine methods for 
comparing neural network representations based on canonical correlation analysis (CCA). We show 
that CCA belongs to a family of statistics for measuring multivariate similarity, but that neither
 CCA nor any other statistic that is invariant to invertible linear transformation can measure 
 meaningful similarities between representations of higher dimension than the number of data 
 points. We introduce a similarity index that measures the relationship between representational
  similarity matrices and does not suffer from this limitation. This similarity index is equivalent
   to centered kernel alignment (CKA) and is also closely connected to CCA. Unlike CCA, CKA can 
   reliably identify correspondences between representations in networks trained from different 
   initializations."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2020-01-14T12:00:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2020-01-14

authors: [iman-mirzadeh]
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
url_slides: https://pdfs.semanticscholar.org/7263/20cdbd04804ffa8f3a78c095bd1b55a2a695.pdf

url_code:
url_pdf: "https://arxiv.org/abs/1905.00414"
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
