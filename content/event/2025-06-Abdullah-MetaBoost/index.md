---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Enhancing Metabolic Syndrome Prediction with Hybrid Data Balancing and Counterfactuals"
event: EMIL Summer'25 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "We introduce MetaBoost, a novel hybrid framework that integrates SMOTE, ADASYN, and CTGAN, optimizing synthetic data generation through weighted averaging and iterative weight tuning to enhance the model’s performance (achieving up to 1.87% accuracy improvement over individual balancing techniques)."
abstract: "Metabolic Syndrome (MetS) is a cluster of interrelated risk factors that significantly increases the risk of cardiovascular diseases and type 2 diabetes. Despite its global prevalence, accurate prediction of MetS remains challenging due to issues such as class imbalance, data scarcity, and methodological inconsistencies in existing studies. In this paper, we address these challenges by systematically evaluating and optimizing machine learning (ML) models for MetS prediction, leveraging advanced data balancing techniques and counterfactual analysis. Multiple ML models, including XGBoost, Random Forest, TabNet, etc., were trained and compared under various data balancing techniques such as random oversampling (ROS), SMOTE, ADASYN, and CTGAN. Additionally, we introduce MetaBoost, a novel hybrid framework that integrates SMOTE, ADASYN, and CTGAN, optimizing synthetic data generation through weighted averaging and iterative weight tuning to enhance the model’s performance (achieving up to a 1.87% accuracy improvement over individual balancing techniques). A comprehensive counterfactual analysis is conducted to quantify the feature-level changes required to shift individuals from high-risk to low-risk categories. The results indicate that blood glucose (50.3%) and triglycerides (46.7%) were the most frequently modified features, highlighting their clinical significance in MetS risk reduction. Additionally, probabilistic analysis shows elevated blood glucose (85.5% likelihood) and triglycerides (74.9% posterior probability) as the strongest predictors. This study not only advances the methodological rigor of MetS prediction but also provides actionable insights for clinicians and researchers, highlighting the potential of ML in mitigating the public health burden of metabolic syndrome."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2025-06-04T12:30:00-07:00
date_end: 2025-06-04T13:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2025-06-20T18:00:00-07:00

authors: [abdullah-mamun]
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

url_code: https://github.com/asusanyamshah/MetaBoost
url_pdf: https://arxiv.org/pdf/2504.06987
url_video: https://www.youtube.com/watch?v=mIZog_q-bh4

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
