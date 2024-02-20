---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Generating Interpretable Counterfactual Explanations By Implicit Minimization of Epistemic and Aleatoric Uncertainties"
event: EMIL Fall'23 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: This article demonstrate a new approach to implement counterfactual explanations (CE) without necessarily employing any generative model. As generative models come with several drawbacks in CE generation, the approach in this paper is based on Epistemic and Aleatoric Uncertainty reduction.
abstract: Counterfactual explanations (CEs) are a practical tool for demonstrating why machine learning classifiers make particular decisions. For CEs to be useful, it is important that they are easy for users to interpret. Existing methods for generating interpretable CEs rely on auxiliary generative models, which may not be suitable for complex datasets, and incur engineering overhead. We introduce a simple and fast method for generating interpretable CEs in a white-box setting without an auxiliary model, by using the predictive uncertainty of the classifier. Our experiments show that our proposed algorithm generates more interpretable CEs, according to IM1 scores, than existing methods. Additionally, our approach allows us to estimate the uncertainty of a CE, which may be important in safety-critical applications, such as those in the medical domain.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2023-11-15T13:50:00-07:00
date_end: 2023-11-15T14:25:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2023-10-15T16:50:20-07:00

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
url_slides: Realistic CFs.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2103.08951"
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