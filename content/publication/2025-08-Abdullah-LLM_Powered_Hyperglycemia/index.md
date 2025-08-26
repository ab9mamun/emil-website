---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "LLM-Powered Prediction of Hyperglycemia and Discovery of Behavioral Treatment Pathways from Wearables and Diet"
authors: [Abdullah Mamun, Asiful Arefeen, Susan B. Racette, Dorothy D. Sears, Corrie M. Whisner, Matthew P. Buman, Hassan Ghasemzadeh]
date: 2025-08-24T11:59:00-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2025-08-24T11:59:00-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "Sensors Journal"
publication_short: ""

abstract: "Postprandial hyperglycemia, marked by the blood glucose level exceeding the normal range after consuming a meal, is a critical indicator of progression toward type 2 diabetes in people with prediabetes and in healthy individuals. A key metric for understanding blood glucose dynamics after eating is the postprandial Area Under the Curve (AUC). Predicting postprandial AUC in advance based on a person's lifestyle factors, such as diet and physical activity level, and explaining the factors that affect postprandial blood glucose could allow an individual to adjust their behavioral choices accordingly to maintain normal glucose levels. In this work, we develop an explainable machine learning solution, GlucoLens, that takes sensor-driven inputs and utilizes advanced data processing, large language models, and trainable machine learning models to estimate postprandial AUC and predict hyperglycemia from diet, physical activity, and recent glucose patterns. We use data obtained using wearables in a five-week clinical trial of 10 adults who worked full-time to develop and evaluate the proposed computational model that integrates wearable sensing, multimodal data, and machine learning. Our machine learning model takes multimodal data from wearable activity and glucose monitoring sensors, along with food and work logs, and provides an interpretable prediction of the postprandial glucose patterns. GlucoLens achieves a normalized root mean squared error (NRMSE) of 0.123 in its best configuration. On average, the proposed technology provides a 16\% better predictive performance compared to the comparison models. Additionally, our technique predicts hyperglycemia with an accuracy of 79\% and an F1 score of 0.749 and recommends different treatment options to help avoid hyperglycemia through diverse counterfactual explanations. With systematic experiments and discussion supported by established prior research, we show that our method is generalizable and consistent with clinical understanding."

# Summary. An optional shortened abstract.
summary: "In this study, we developed an explainable machine learning solution, GlucoLens, that takes sensor-driven inputs and uses advanced data processing, large language models, and trainable machine learning models to predict postprandial AUC and hyperglycemia from diet, physical activity, and recent glucose patterns."

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
url_code: https://github.com/ab9mamun/GlucoLens
url_dataset:
url_poster:
url_project:
url_slides: slides.pdf
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
