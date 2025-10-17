---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Time-Aware Cross-Attention for Multi-Modal Sensor-Based Blood Glucose Forecasting"
authors: [Aashritha Machiraju,  Ebrahim Farahmand, Shovito Barua Soumma, Asiful Arefeen, Carol Johnston, Hassan Ghasemzadeh]
date: 2025-09-16T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2025-09-16T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE-EMBS International Conference on Body Sensor Networks"
publication_short: "BSN"

abstract: "Accurate blood glucose forecasting enables proactive management of metabolic health, particularly when leveraging data from wearable sensors that capture data about physiological and behavioral health. However, existing models struggle with integrating multimodal time-series data with inconsistent sampling rates. This paper proposes a novel forecasting framework that incorporates a time-aware cross-attention mechanism with an LSTM architecture to predict blood glucose levels using continuous glucose monitoring (CGM) data alongside physiological and behavioral signals, such as heart rate (HR), electrodermal activity, accelerometry, and dietary intake. The proposed method dynamically encodes temporal features without the need for preprocessing and employs gated multi-head cross-attention layers to fuse sensor modalities effectively. We evaluate our approach on a newly constructed dataset involving 12 participants. Our method outperforms the baseline and state-of-the-art GlySim models across multiple prediction horizons ranging from 5 minutes to 90 minutes, achieving up to 17.8% improvement in Root Mean Squared Error (RMSE) values."

# Summary. An optional shortened abstract.
summary: "This paper introduces a multimodal blood glucose forecasting framework that combines time-aware cross-attention with an LSTM to predict glucose levels from continuous glucose monitoring (CGM) data and complementary wearable sensor signals (heart rate, electrodermal activity, accelerometry, and diet)."

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

url_pdf: https://drive.google.com/file/d/1wTxULHCBsBFlws7rwntydb5BQLIdUWpE/view?usp=sharing
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
projects: [mental-health]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
