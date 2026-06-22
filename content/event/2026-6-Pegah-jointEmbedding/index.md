---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting"
event: EMIL Spring'26 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "This paper proposes a multimodal calorie estimation model that combines continuous glucose monitor (CGM) data and food photographs through a joint embedding framework."

abstract: "Accurate meal intake estimation is important for diet monitoring and diabetes management, but calorie prediction from a single data modality can be limited. CGM-based models capture post-prandial glucose responses, while food image models capture visual information about meal content; however, each modality alone may miss important nutritional information. This paper proposes a multimodal inverse metabolic model that combines CGM data and food photographs for calorie estimation. The model extracts glucose representations using an attention-based Transformer and Gaussian area-under-the-curve (gAUC) features, while food image representations are extracted using a Vision Transformer. These modality-specific embeddings are combined using a late-fusion projector network to generate calorie predictions. The authors evaluate the model on data from 27 participants who wore Freestyle Libre Pro CGMs and consumed breakfasts and lunches with known caloric content. The joint CGM-image embedding achieved the best performance, with an NRMSE of 0.34 and a correlation of 0.52, outperforming CGM-only and image-only baselines. The results suggest that combining multiple views of meals can improve automated diet monitoring technologies."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2026-06-07T12:00:00-07:00
date_end: 2026-06-07T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2026-06-10T14:00:00-07:00

authors: [Pegah Khorasani]
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
url_slides: slides.pdf

url_code: 
url_pdf: https://doi.org/10.1109/BHI58575.2023.10313421
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
