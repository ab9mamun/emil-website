---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "From Indicators to Insights: Diversity-Optimized for Medical Series-Text Decoding via LLMs"
event: EMIL Spring'26 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This paper introduces InDiGO, a framework for integrating clinical indicators into prompt-based modeling of medical time series with LLMs.

abstract: "Medical time-series analysis differs fundamentally from general ones by requiring specialized domain knowledge to interpret complex signals and clinical context. Large language models (LLMs) hold great promise for augmenting medical time-series analysis by complementing raw series with rich contextual knowledge drawn from biomedical literature and clinical guidelines. However, realizing this potential depends on precise and meaningful prompts that guide the LLM to key information. Yet, determining what constitutes effective prompt content remains non-trivial—especially in medical settings where signal interpretation often hinges on subtle, expert-defined decision-making indicators. To this end, we propose InDiGO, a knowledge-aware evolutionary learning framework that integrates clinical signals and decision-making indicators through iterative optimization. Across four medical benchmarks, InDiGO consistently outperforms prior methods."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2026-01-21T12:00:00-07:00
date_end: 2026-01-21T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2026-01-21T12:30:20-07:00

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
url_slides: 13-InDiGO.pdf

url_code:
url_pdf: "https://openreview.net/forum?id=aTqfufujj7"
url_video: "https://neurips.cc/virtual/2025/loc/san-diego/poster/117266"

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