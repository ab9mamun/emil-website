---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "A large sensor foundation model pretrained on continuous glucose monitor data for diabetes management"
event: EMIL Fall'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This work proposed a transformer decoder-based Large Sensor Model (LSM) pretrained on 1.6 million CGM records from patients with different diabetes types and demonstrates improvement in near-future glucose prediction.

abstract: "Continuous glucose monitoring (CGM) combined with AI offers new opportunities for proactive diabetes management through real-time glucose forecasting. However, most existing models are task-specific and lack generalization across patient populations. Inspired by the autoregressive paradigm of large language models, we introduce CGM-LSM, a Transformer decoder-based Large Sensor Model (LSM) pretrained on 1.6 million CGM records from patients with different diabetes types, ages, and genders. We model patients as sequences of glucose time steps to learn latent knowledge embedded in CGM data and apply it to the prediction of glucose readings for a 2-h horizon. Compared with prior methods, CGM-LSM significantly improves prediction accuracy and robustness: a 48.51% reduction in root mean square error in 1-h horizon forecasting and consistent zero-shot prediction performance across held-out patient groups. We analyze model performance variations across patient subgroups and prediction scenarios and outline key opportunities and challenges for advancing CGM foundation models."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-10-22T12:00:00-07:00
date_end: 2025-10-22T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-02-12T12:30:20-07:00

authors: [shovito-barua-soumma]
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
url_slides: 12-CG-LSM.pdf

url_code:
url_pdf: "https://www.nature.com/articles/s44401-025-00039-y"
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