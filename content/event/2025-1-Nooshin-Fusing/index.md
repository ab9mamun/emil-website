---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Multi-view classification with convolutional neural networks"
event: EMIL Spring'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "This paper investigates the following three strategies: (1) fusing convolutional feature maps at differing network depths; (2) fusion of bottleneck latent representations prior to classification; and (3) score fusion."
abstract: "Humans’ decision making process often relies on utilizing visual information from different views or perspectives. However, in machine-learning-based image classification we typically infer an object’s class from just a single image showing an object. Especially for challenging classification problems, the visual information conveyed by a single image may be insufficient for an accurate decision. We propose a classification scheme that relies on fusing visual information captured through images depicting the same object from multiple perspectives. Convolutional neural networks are used to extract and encode visual features from the multiple views and we propose strategies for fusing these information. More specifically, we investigate the following three strategies: (1) fusing convolutional feature maps at differing network depths; (2) fusion of bottleneck latent representations prior to classification; and (3) score fusion. We systematically evaluate these strategies on three datasets from different domains. Our findings emphasize the benefit of integrating information fusion into the network rather than performing it by post-processing of classification scores. Furthermore, we demonstrate through a case study that already trained networks can be easily extended by the best fusion strategy, outperforming other approaches by large margin."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-01-15T12:00:00-07:00
date_end: 2025-01-15T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2025-01-15T19:34:20-07:00

authors: [nooshin-taheri-chatrudi]
tags: []

# Is this a featured talk? (true/false)
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

# Optional filename of your slides within your talk's folder or a URL.
url_slides: fusing.pdf

url_code:
url_pdf: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0245230
url_video:

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
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
