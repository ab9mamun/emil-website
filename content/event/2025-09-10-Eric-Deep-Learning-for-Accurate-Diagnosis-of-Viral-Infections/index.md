---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Deep Learning for Accurate Diagnosis of Viral Infections through scRNA-seq Analysis: A Comprehensive Benchmark Study"
event: EMIL Fall'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "The presentation reviews a benchmark study evaluating deep learning models for diagnosing viral infections using single-cell RNA sequencing (scRNA-seq) data. The study compared multiple models—including PCA, SAVER, scVI, scGPT, and contrastiveVI—on a large dataset of over 200,000 immune cells from patients with COVID-19, influenza, and dengue. Key challenges addressed were batch effects and reliable classification across diverse experimental conditions. Results showed that contrastiveVI outperformed others in classification accuracy, while scGPT contributed to effective batch harmonization. Evaluation metrics included ARI, NMI, k-nearest neighbor accuracy, and S-score, with UMAP used for visual confirmation. The findings demonstrate the importance of model choice, preprocessing, and batch control in applying scRNA-seq analysis for infection diagnosis."
abstract: "This presentation examines a comprehensive benchmark study of deep learning approaches for diagnosing viral infections through single-cell RNA sequencing (scRNA-seq). Using a dataset of more than 200,000 immune cells across COVID-19, influenza, and dengue, the study tested models including PCA, SAVER, scVI, scGPT, and contrastiveVI. The pipeline incorporated preprocessing, batch control, and dimensionality reduction for robust model evaluation. Performance was assessed using clustering metrics (ARI, NMI), neighborhood consistency (k-NN accuracy), and structural cohesion (S-score). Results indicate contrastiveVI as the most accurate model for infection classification, with scGPT providing strong batch harmonization capabilities. UMAP projections were used to validate clustering visually. These findings underscore the role of batch control and careful model selection in building reliable AI pipelines for infection-specific scRNA-seq diagnostics, offering methodological insights for future biomedical applications."

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
date: 2025-09-10T12:00:00-07:00
date_end: 2025-09-10T12:30:00-07:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2025-09-15T11:00:00-07:00

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
url_pdf: 
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

