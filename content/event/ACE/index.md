---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Adversarial Counterfactual Visual Explanations"
event: EMIL Spring'24 Seminars
event_url:
location: Health Futures Center, ASU
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  Adversarial Counterfactual Explanations propose to develop a filter that robustifies a model against adversarial attacks and helps to transform them into counterfactual explanations. 
abstract: Counterfactual explanations and adversarial attacks have a related goal- flipping output labels with minimal perturbations regardless of their characteristics. Yet, adversarial attacks cannot be used directly in a counterfactual explanation perspective, as such perturbations are perceived as noise and not as actionable and understandable image modifications. Building on the robust learning literature, this paper proposes an elegant method to turn adversarial attacks into semantically meaningful perturbations, without modifying the classifiers to explain. The proposed approach hypothesizes that Denoising Diffusion Probabilistic Models are excellent regularizers for avoiding highfrequency and out-of-distribution perturbations when generating adversarial attacks. The paper’s key idea is to build attacks through a diffusion model to polish them. This allows studying the target model regardless of its robustification level. Extensive experimentation shows the advantages of our counterfactual explanation approach over current State-of-the-Art in multiple testbeds.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-04-02T15:00:00-07:00
date_end: 2024-04-02T15:40:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-04-02T18:50:20-07:00

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
url_slides: ACE.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2303.09962"
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