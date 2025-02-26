---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Preserving Causal Constraints in Counterfactual Explanations for Machine Learning Classifiers"
event: EMIL Spring'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This paper introduces new constraints in the optimization method to generate realistic and feasible counterfactual explanations.
abstract: To construct interpretable explanations that are consistent with the original ML model, counterfactual examples—showing how the model’s output changes with small perturbations to the input—have been proposed. This paper extends the work in counterfactual explanations by addressing the challenge of feasibility of such examples. For explanations of ML models in critical domains such as healthcare and finance, counterfactual examples are useful for an end-user only to the extent that perturbation of feature inputs is feasible in the real world. We formulate the problem of feasibility as preserving causal relationships among input features and present a method that uses (partial) structural causal models to generate actionable counterfactuals. When feasibility constraints cannot be easily expressed, we consider an alternative mechanism where people can label generated CF examples on feasibility- whether it is feasible to intervene and realize the candidate CF example from the original input. To learn from this labelled feasibility data, we propose a modified variational auto encoder loss for generating CF examples that optimizes for feasibility as people interact with its output. Our experiments on Bayesian networks and the widely used “Adult-Income” dataset show that our proposed methods can generate counterfactual explanations that better satisfy feasibility constraints than existing methods.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-02-26T12:30:00-07:00
date_end: 2025-02-26T12:55:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-01-15T15:20:20-07:00

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
url_slides: Realistic_CFs2.pptx

url_code:
url_pdf: "https://arxiv.org/pdf/1912.03277"
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