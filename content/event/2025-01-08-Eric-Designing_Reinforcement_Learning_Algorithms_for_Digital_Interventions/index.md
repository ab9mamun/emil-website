---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Designing Reinforcement Learning Algorithms for Digital Interventions: Pre-Implementation Guidelines"
event: EMIL Spring'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "This presentation examines the extension of the PCS (Predictability, Computability, Stability) framework for Reinforcement Learning (RL) algorithm design in digital interventions. Since RL models must be finalized before deployment, robust pre-implementation planning is critical. A case study on Oralytics, a digital oral health intervention, demonstrates how PCS principles enhance RL design. Using a contextual bandit algorithm with Bayesian Linear Regression (BLR), the system optimized intervention effectiveness while ensuring stability. Results showed that BLR performed best, larger clusters improved learning, and simulations required greater diversity. Overall, PCS offers a systematic approach for RL-driven interventions, balancing personalization, computational feasibility, and stability. Further refinements are needed to enhance adaptability and generalization."
abstract: "Reinforcement Learning (RL) is widely used in digital interventions, but designing effective RL algorithms presents significant challenges. Since RL models must be finalized before deployment, mistakes in the design process can lead to inefficiencies, poor adaptation, and high costs. This presentation introduces an extended PCS (Predictability, Computability, Stability) framework to address these challenges, refining its application for RL to enhance algorithm personalization, efficiency, and robustness. Predictability is redefined as personalization, computability incorporates real-world constraints like timely access to state and reward data, and stability ensures algorithmic consistency across dynamic environments. A case study on Oralytics, a digital oral health intervention, demonstrates the effectiveness of the extended PCS framework in RL design. The intervention leverages a contextual bandit algorithm with Bayesian Linear Regression (BLR), optimizing decision-making based on user engagement patterns. Key design considerations include decision timing, reward selection, computational constraints, and algorithm stability. The study found that BLR outperformed alternative models, larger cluster sizes enhanced learning efficiency, and environmental simulations required increased variability for better generalization. The results emphasize that PCS provides a structured methodology for RL-driven digital interventions, ensuring reliability while addressing real-world constraints such as user heterogeneity, computational limitations, and data variability. While the approach successfully guided RL design for Oralytics, further refinements are needed, particularly in expanding simulation environments and improving generalization to diverse populations. This work demonstrates that PCS can be a valuable tool for RL pre-implementation, enabling effective algorithm design in applied settings."

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
date: 2025-01-08T12:00:00-07:00
date_end: 2025-01-08T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2025-03-06T11:00:00-07:00

authors: [eric-kim]
tags: []

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: Smart
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your talk's folder or a URL.
url_slides: slides.pptx
url_code:
url_pdf: https://arxiv.org/abs/2206.03944
url_video:

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: "slides"

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

