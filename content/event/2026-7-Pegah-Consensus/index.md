---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "ConSensus: Multi-Agent Collaboration for Multimodal Sensing"
event: EMIL Summer'26 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "This paper proposes ConSensus, a training-free multi-agent framework that improves multimodal sensor reasoning by decomposing heterogeneous sensor inputs into modality-specific LLM agents and combining their outputs through hybrid fusion."

abstract: "Large language models are increasingly being used to reason over sensor data from the physical world and human physiology. However, multimodal sensing remains challenging because heterogeneous sensors can provide complementary but sometimes noisy, missing, or unreliable information. This paper proposes ConSensus, a training-free multi-agent collaboration framework for multimodal sensing. Instead of giving all sensor features to a single LLM, ConSensus assigns each sensor modality to a specialized modality-aware agent, allowing each agent to generate an independent prediction and rationale. These modality-level interpretations are then aggregated using a hybrid fusion strategy that combines semantic fusion, statistical fusion, and a final hybrid coordinator. The semantic fusion agent reasons over the modality-agent explanations using cross-modal evidence and domain knowledge, while the statistical fusion agent anchors its reasoning to the majority-voted prediction. The hybrid fusion agent then arbitrates between these two reasoning paths to produce the final decision. The authors evaluate ConSensus on five multimodal sensing benchmarks, including affective state recognition, sleep stage classification, kitchen activity recognition, gym exercise recognition, and daily activity recognition. Results show that ConSensus improves average accuracy over the single-agent baseline and achieves comparable performance to multi-agent debate methods while substantially reducing fusion token cost. The study highlights the value of modality-specific reasoning and structured hybrid fusion for efficient and robust LLM-based multimodal sensing."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2026-07-09T12:00:00-07:00
date_end: 2026-07-09T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2026-07-09T14:00:00-07:00

authors: [Pegah Khorasani]
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
url_slides: slides.pdf

url_code: 
url_pdf: https://arxiv.org/abs/2601.06453
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