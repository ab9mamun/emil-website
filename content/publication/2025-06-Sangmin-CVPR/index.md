---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Guiding Diffusion with Deep Geometric Moments: Balancing Fidelity and Variation"
authors: [Sangmin Jung, Utkarsh Nath, Yezhou Yang, Giulia Pedrielli, Joydeep Biswas, Amy Zhang, Hassan Ghasemzadeh, Pavan Turaga]
date: 2025-05-06T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2025-26-05T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "In CVPR 3rd Workshop on Generative Models for Computer Vision (GMCV), 2025"
publication_short: "CVPR"

abstract: "Text-to-image generation models have achieved remarkable capabilities in synthesizing images, but often struggle to provide fine-grained control over the output. Existing guidance approaches, such as segmentation maps and depth maps, introduce spatial rigidity that restricts the inherent diversity of diffusion models. In this work, we introduce Deep Geometric Moments (DGM) as a novel form of guidance that encapsulates the subject's visual features and nuances through a learned geometric prior. DGMs focus specifically on the subject itself compared to DINO or CLIP features, which suffer from overemphasis on global image features or semantics. Unlike ResNets, which are sensitive to pixel-wise perturbations, DGMs rely on robust geometric moments. Our experiments demonstrate that DGM effectively balance control and diversity in diffusion-based image generation, allowing a flexible control mechanism for steering the diffusion process."

# Summary. An optional shortened abstract.
summary: "This work introduces Deep Geometric Moments (DGM) as a novel, training-free guidance mechanism for text-to-image diffusion models. Unlike existing guidance techniques (e.g., segmentation maps, depth maps, or CLIP features), which impose rigid spatial constraints or rely heavily on global semantics, DGM captures fine-grained, subject-specific visual features through robust geometric representations. The proposed method uses a pretrained DGM model during the diffusion process to steer image generation in a flexible yet identity-preserving manner. Experiments show that DGM achieves a better balance between control and diversity, enabling more nuanced and visually consistent image synthesis without retraining the diffusion model."

tags: ["featured"]
categories: []
featured: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://arxiv.org/pdf/2505.12486
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [Expand-AI]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
