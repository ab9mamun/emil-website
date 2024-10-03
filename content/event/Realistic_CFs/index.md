---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Realistic Counterfactual Explanations with Learned Relations"
event: EMIL Fall'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This paper proposes a DAG-GNN based VAE to reflect the inter-feature relationships in the produced counterfactuals.
abstract: Many existing methods of counterfactual explanations ignore the intrinsic relationships between data attributes and thus fail to generate realistic counterfactuals. Moreover, the existing models that account for relationships require domain knowledge, which limits their applicability in complex real-world applications. In this paper, we propose a novel approach to realistic counterfactual explanations that preserve the relationships and minimise experts' interventions. The model directly learns the relationships by a variational auto-encoder with minimal domain knowledge and then learns to perturb the latent space accordingly. We conduct extensive experiments on both synthetic and real-world datasets. The experimental results demonstrate that the proposed model learns relationships from the data and preserves these relationships in generated counterfactuals. In particular, it outperforms other methods in terms of Mahalanobis distance, and the constraint feasibility score.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-10-02T12:30:00-07:00
date_end: 2024-10-02T13:10:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-10-02T18:50:20-07:00

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
url_slides: Realistic_CFs.pptx

url_code:
url_pdf: "https://arxiv.org/abs/2202.07356"
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