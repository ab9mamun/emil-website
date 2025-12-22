---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Chronos-2: From Univariate to Universal Forecasting"
event: EMIL Fall'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  Chronos 2 is the first ever multivariate time-series forecasting foundation model. It leverages time attention (across time axis) and group attention (across different signals within group) to predict quantiles instead of point estimates.
abstract: Pretrained time series models have enabled inference-only forecasting systems that produce accurate predictions without task-specific training. However, existing approaches largely focus on univariate forecasting, limiting their applicability in real-world scenarios where multivariate data and covariates play a crucial role. We present Chronos-2, a pretrained model capable of handling univariate, multivariate, and covariate-informed forecasting tasks in a zero-shot manner. Chronos-2 employs a group attention mechanism that facilitates in-context learning (ICL) through efficient information sharing across multiple time series within a group, which may represent sets of related series, variates of a multivariate series, or targets and covariates in a forecasting task. These general capabilities are achieved through training on synthetic datasets that impose diverse multivariate structures on univariate series. Chronos-2 delivers state-of-the-art performance across three comprehensive benchmarks- fev-bench, GIFT-Eval, and Chronos Benchmark II. On fev-bench, which emphasizes multivariate and covariate-informed forecasting, Chronos-2’s universal ICL capabilities lead to substantial improvements over existing models. On tasks involving covariates, it consistently outperforms baselines by a wide margin. Case studies in the energy and retail domains further highlight its practical advantages. The in-context learning capabilities of Chronos-2 establish it as a general-purpose forecasting model that can be used “as is” in real-world forecasting pipelines.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-12-17T12:00:00-07:00
date_end: 2025-12-17T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-12-17T13:40:20-07:00

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
url_slides: Chronos_Chronos2.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2510.15821"
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