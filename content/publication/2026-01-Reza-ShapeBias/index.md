---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Improving Shape Bias in Learnable Geometric Moment Representations"
authors: [Sangmin Jung, Anirudh Rayas, Reza Rahimi Azghan, Hassan Ghasemzadeh, Pavan Turaga]
date: 2026-01-04T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2026-01-04T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "In WACV Workshop on Learning & Exploitation of Latent Space Geometries (LENS), 2026"
publication_short: "LENS"

abstract: "Deep Geometric Moments (DGMs) have been shown to encode shape-aware representations in image features. In this work, we revisit the DGM framework through the lens of ConvNeXt, a modern convolutional network (ConvNet) architecture. By leveraging features extracted from ConvNeXt, we improve classification accuracy while further strengthening the geometric shape-awareness of DGMs. Our results demonstrate that features from modern ConvNet backbones serve as compatible stems for training Deep Geometric Moments, and that the learned representations remain tightly aligned with object geometry while exhibiting robustness to visual perturbations. We quantitatively characterize this shape awareness using geometric metrics such as the Hausdorff distance and the Average Symmetric Surface Distance (ASSD) complemented by Intersection over Union (IoU) to assess regional overlap. Furthermore, we conduct an extensive analysis of the invariance of the learned feature representations under diverse image perturbations, including changes in rotation, brightness, color, and scale. We posit that these shape-aligned features offer significant value not only for traditional computer vision tasks, such as object detection and image segmentation, but also for modern efficient training-free image and video editing methods."

# Summary. An optional shortened abstract.
summary: "This paper revisits Deep Geometric Moments (DGM), a framework for learning shape-aware, geometry-aligned visual representations, by swapping the original ResNet backbone for ConvNeXt, a modern high-performing ConvNet. Using ConvNeXt feature maps as the input “stem” for DGM, the authors show consistent ImageNet-1K accuracy gains over a ResNet34-DGM baseline (up to ~+2.4% depending on ConvNeXt size) while preserving and strengthening DGM’s shape bias."

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

url_pdf: https://drive.google.com/file/d/1FvjL6LQGtYQf0CCGA4RMMisBPHw1qjH3/view?usp=sharing
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
