---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "CounterNet: End-to-End Training of Prediction Aware Counterfactual Explanations"
event: EMIL Spring'24 Seminars
event_url:
location: Health Futures Center, ASU
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  CounterNet proposes an end-to-end training of the predictor and explanation generator to solve some key issues associated with post-hoc/model agnostic explainers. 
abstract: This work presents CounterNet, a novel end-to-end learning frame- work which integrates Machine Learning (ML) model training and the generation of corresponding counterfactual (CF) explanations into a single end-to-end pipeline. Counterfactual explanations offer a contrastive case, i.e., they attempt to find the smallest modifica- tion to the feature values of an instance that changes the prediction of the ML model on that instance to a predefined output. Prior techniques for generating CF explanations suffer from two ma- jor limitations- (i) all of them are post-hoc methods designed for use with proprietary ML models — as a result, their procedure for generating CF explanations is uninformed by the training of the ML model, which leads to misalignment between model pre- dictions and explanations; and (ii) most of them rely on solving separate time-intensive optimization problems to find CF expla- nations for each input data point (which negatively impacts their runtime). This work makes a novel departure from the prevalent post-hoc paradigm (of generating CF explanations) by presenting CounterNet, an end-to-end learning framework which integrates predictive model training and the generation of counterfactual (CF) explanations into a single pipeline. Unlike post-hoc methods, CounterNet enables the optimization of the CF explanation gen- eration only once together with the predictive model. We adopt a block-wise coordinate descent procedure which helps in effec- tively training CounterNet’s network. Our extensive experiments on multiple real-world datasets show that CounterNet generates high-quality predictions, and consistently achieves 100% CF valid- ity and low proximity scores (thereby achieving a well-balanced cost-invalidity trade-off) for any new input instance, and runs 3X faster than existing state-of-the-art baselines.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-02-06T15:00:00-07:00
date_end: 2024-02-06T15:40:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-02-06T18:50:20-07:00

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
url_slides: CounterNet.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2109.07557"
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