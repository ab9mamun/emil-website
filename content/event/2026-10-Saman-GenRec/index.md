---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "GenRec: An LLM-Backed Recommendation Ranker at Netflix"
event: EMIL Fall'26 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: The work introduces GenRec, an LLM-backed recommendation ranker at Netflix that post-trains an in-house foundation LLM on verbalized user histories and context, replacing thousands of hand-engineered features with context engineering, a catalog-aware scoring head and reward-weighted training. In a large-scale A/B test it beats the mature production ranker on offline and online metrics while using far fewer Phase-2 labeled examples and input signals, served cost-efficiently through prefill-only inference.
abstract: Large language models (LLMs) are reshaping recommender systems by enabling richer modeling of users, content, and context directly in natural language. At Netflix, we are exploring this direction through GenRec, an LLM-backed recommendation ranker built on top of an in-house foundational LLM. GenRec follows a two-phase framework: Phase 1 adapts an open-source LLM to Netflix data, developing deep understanding of the catalog and member behavior while balancing capabilities such as content understanding and instruction following. Phase 2 post-trains this foundation model with recommendation-ranking specific data, labels, and reward signals, aiming to align the ranker with business requirements and long-term member satisfaction. This paper focuses on Phase 2 and the transition from a traditional discriminative ranker with thousands of engineered features to an LLM-backed ranker driven by verbalized user histories and context. We describe our design for input verbalization and context engineering, post-training data construction, reward integration, model architecture, and a cost-constrained serving design based on prefill-only inference approach. We report results from a large-scale A/B test in comparing GenRec against the current production ranker model, where we show that a GenRec model trained with substantially fewer Phase-2 labeled training examples and input signals can achieve statistically significant gains in offline and online metrics. We discuss how LLM-backed recommenders could shift the recommendation paradigm: from feature engineering to context engineering, and from bespoke architectures to shared foundation backbones. We also outline practical lessons for serving such systems under real-world resource constraints.

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
date: 2026-10-07T12:00:00-07:00
date_end: 2026-10-26T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2026-10-13T19:20:00-07:00

authors: [saman-khamesian]
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

url_pdf: https://arxiv.org/abs/2604.14878

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
