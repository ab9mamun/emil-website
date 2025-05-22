---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "A General Search-Based Framework for Generating Textual Counterfactual"
event: EMIL Summer'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This paper is a search based but fast counterfactual generation method for textual data. It proposes three operators to conduct the search in an anytime algorithm. Therefore, the more time it gets the better qulaity countefactual it delivers. 
abstract: One of the prominent methods for explaining the decision of a machine-learning classifier is by a counterfactual example. Most current algorithms for generating such examples in the textual domain are based on generative language models. Generative models, however, are trained to minimize a specific loss function in order to fulfill certain requirements for the generated texts. Any change in the requirements may necessitate costly retraining, thus potentially limiting their applicability. In this paper, we present a general search-based framework for generating counterfactual explanations in the textual domain. Our framework is model-agnostic, domainagnostic, anytime, and does not require retraining in order to adapt to changes in the user requirements. We model the task as a search problem in a space where the initial state is the classified text, and the goal state is a text in a given target class. Our framework includes domain-independent modification operators, but can also exploit domain-specific knowledge through specialized operators. The search algorithm attempts to find a text from the target class with minimal userspecified distance from the original classified object.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-05-21T12:00:00-07:00
date_end: 2025-05-21T12:35:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-05-21T16:40:20-07:00

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
url_slides: TCE_search.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2211.00369"
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