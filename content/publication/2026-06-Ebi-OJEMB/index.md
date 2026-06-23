---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Time-Aware Multimodal Sensor Fusion for Blood Glucose Forecasting in Non-Diabetic Adults"
authors: [Aashritha Machiraju, Ebrahim Farahmand,Shovito Barua Soumma, Asiful Arefeen, Reza Rahimi Azhghan, Carol Johnston, Hassan Ghasemzadeh]
date: 2026-06-16T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2026-06-17T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Open Journal of Engineering in Medicine and Biology"
publication_short: "OJEMB"

abstract: "Glucose dysregulation in non-diabetic individuals can precede metabolic disease onset by years, yet most glucose prediction models target diabetic populations with structured insulin records. This article presents Patch Time-Aware Cross-Attention (Patch-TACA), a multimodal transformer-based framework for long-term blood glucose forecasting in healthy individuals. The approach combines patch-based self-supervised pretraining with a time-aware cross-attention mechanism to integrate continuous glucose monitoring (CGM) data with physiological and behavioral measures, such as accelerometry, heart rate, electrodermal activity, and meal macronutrients, without requiring explicit resampling of irregularly sampled signals. Patch-TACA is assessed using data from twelve healthy participants across three laboratory sessions. It achieves an RMSE of 14.26 ± 3.48$ mg/dL at the 90-minute prediction horizon, outperforming GlySim and Gluformer baselines. Moreover, employing a self-supervised method for pre-training reduced RMSE by 7.9% compared to training with random weight initialization, and hyperglycemia prediction accuracy reached 93.9%. These results demonstrate that multimodal sensor fusion with self-supervised learning enables accurate long-horizon glucose forecasting in non-diabetic populations, supporting proactive metabolic health monitoring before clinical disease onset."

# Summary. An optional shortened abstract.
summary: "This paper introduces Patch-TACA, a multimodal transformer that forecasts long-term blood glucose in healthy individuals by fusing CGM data with physiological and behavioral signals via time-aware cross-attention and self-supervised pretraining. On twelve participants, it achieved 14.26 ± 3.48 mg/dL RMSE at a 90-minute horizon and 93.9% hyperglycemia prediction accuracy, outperforming GlySim and Gluformer baselines. The results show that multimodal sensor fusion enables accurate long-horizon glucose forecasting for proactive metabolic health monitoring before disease onset."

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

url_pdf: https://drive.google.com/file/d/1ARy1aYCcbGfGPzO_AcdOPAKYHYd44KAB/view?usp=sharing
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
