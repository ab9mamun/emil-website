---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "GluBox: Glucose Prediction for Type 1 Diabetes from Multimodal Wearable Sensors using Region-Sensitive Loss and Bayesian Optimization"
authors: [Pegah Khorasani, Ebrahim Farahmand, Abdullah Mamun, Hassan Ghasemzadeh]
date: 2026-06-21T12:00:00-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2026-06-21T12:00:00-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Sensors Journal - June 2026"
publication_short: ""

abstract: "Integrating Artificial Intelligence (AI) into wearable sensor systems for disease prevention and management, such as type 1 diabetes, necessitates the development of forecasting models capable of learning from heterogeneous multimodal data while operating under realistic computational and deployment constraints. A particular growing area of research in this domain is the development of machine learning models that forecast blood glucose levels using wearable sensor data. Such models must effectively map the complex interactions between physiological signals and lifestyle variables to future blood glucose levels. However, existing blood glucose forecasting methods achieve only moderate performance levels on wearable sensing data, limiting their practical effectiveness. To address this challenge, we present GluBox, a multimodal forecasting system that leverages continuous glucose monitoring (CGM) as a core wearable sensing modality, together with behavioral and clinical data that influence blood glucose patterns, to predict long-term blood glucose patterns in individuals with type 1 diabetes while prioritizing clinically consequential errors. GluBox devises a custom weighted loss function that asymmetrically penalizes prediction errors associated with hypoglycemic and hyperglycemic events, explicitly aligning training objectives of the machine learning model with clinical risks of experiencing abnormal blood glucose outcomes. To efficiently tune these loss-weight parameters without exhaustive evaluation of all candidate configurations, we leverage Bayesian optimization, reducing the number of computationally expensive training iterations required to identify clinically effective operating points. We evaluate GluBox on two large-scale datasets comprising over 38,000 hours of data from 34 patients with type 1 diabetes. Results indicate that GluBox outperforms state-of-the-art glucose forecasting models, achieving an RMSE reduction of approximately 14--15\%, with pronounced improvements in clinically critical glycemic ranges."

# Summary. An optional shortened abstract.
summary: "we present GluBox, a multimodal forecasting system that leverages continuous glucose monitoring (CGM) as a core wearable sensing modality, together with behavioral and clinical data that influence blood glucose patterns, to predict long-term blood glucose patterns in individuals with type 1 diabetes while prioritizing clinically consequential errors."

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

url_pdf: 
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
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
