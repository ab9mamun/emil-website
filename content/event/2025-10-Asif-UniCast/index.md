---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "UniCast: A Unified Multimodal Prompting Framework for Time Series Forecasting"
event: EMIL Fall'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  Unicast is a timeseries forecasting foundation model. It leverages multi-modal data (visual and textual information) from a timeseries through embedding generators and aligns the output of the embedders to forecasting task using parameter efficient soft prompting.
abstract: Time series forecasting is a foundational task across domains, such as finance, healthcare, and environmental monitoring. While recent advances in Time Series Foundation Models (TSFMs) have demonstrated strong generalisation through large-scale pretraining, existing models operate predominantly in a unimodal setting, ignoring the rich multimodal context, such as visual and textual signals, that often accompanies time series data in real-world scenarios. This paper introduces a novel parameter-efficient multimodal framework, UniCast, that extends TSFMs to jointly leverage time series, vision, and text modalities for enhanced forecasting performance. Our method integrates modality-specific embeddings from pretrained Vision and Text Encoders with a frozen TSFM via soft prompt tuning, enabling efficient adaptation with minimal parameter updates. This design not only preserves the generalisation strength of the foundation model but also enables effective cross-modal interaction. Extensive experiments across diverse time-series forecasting benchmarks demonstrate that UniCast consistently and significantly outperforms all existing TSFM baselines. The findings highlight the critical role of multimodal context in advancing the next generation of general-purpose time series forecasters.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-10-08T12:30:00-07:00
date_end: 2025-10-08T13:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-10-08T13:40:20-07:00

authors: [asiful-arefeen]
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
url_slides: UniCast.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2508.11954"
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