---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations"
event: EMIL Fall'23 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: An introduction to counterfactual explanations using the novel approach developed by Microsoft Corporation, India.
abstract: Post-hoc explanations of machine learning models are crucial for people to understand and act on algorithmic predictions. An intriguing class of explanations is through counterfactuals, hypothetical examples that show people how to obtain a different prediction. We posit that effective counterfactual explanations should satisfy two properties- feasibility of the counterfactual actions given user context and constraints, and diversity among the counterfactuals presented. To this end, we propose a framework for generating and evaluating a diverse set of counterfactual explanations based on determinantal point processes. To evaluate the actionability of counterfactuals, we provide metrics that enable comparison of counterfactual-based methods to other local explanation methods. We further address necessary tradeoffs and point to causal implications in optimizing for counterfactuals. Our experiments on four real-world datasets show that our framework can generate a set of counterfactuals that are diverse and well approximate local decision boundaries, outperforming prior approaches to generating diverse counterfactuals.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2023-08-31T13:30:00-07:00
date_end: 2023-08-31T14:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2022-09-04T16:50:20-07:00

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
url_slides: CF.pptx

url_code:
url_pdf: "https://arxiv.org/pdf/1905.07697.pdf"
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