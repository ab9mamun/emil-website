---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "CUDLE: Learning Under Label Scarcity to Detect Cannabis Use in Uncontrolled Environments using Wearables"
authors: [Reza Rahimi Azghan, Nicholas C. Glodosky, Ramesh Kumar Sah, Michael J. Cleveland, Carrie Cuttler, Ryan J. McLaughlin, Hassan Ghasemzadeh]
date: 2024-12-25T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2025-26-02T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Sensors"
publication_short: "Sensors"

abstract: "Wearable sensor systems have demonstrated great potential for real-time, objective monitoring of physiological health to support behavioral interventions. However, obtaining accurate labels in free-living environments remains challenging due to limited human supervision and reliance on self-labeling by patients, complicating data collection and supervised learning. To address this, we introduce CUDLE (Cannabis Use Detection with Label Efficiency), a novel framework that leverages self-supervised learning with real-world wearable sensor data to automatically detect cannabis consumption in free-living environments. CUDLE identifies consumption moments using sensor-derived data through a contrastive learning framework, first learning robust representations via a self-supervised pretext task with data augmentation. These representations are then fine-tuned in a downstream task with a shallow classifier, allowing CUDLE to outperform traditional supervised methods, especially with limited labeled data. To evaluate our approach, we conducted a clinical study with 20 cannabis users, collecting over 500 hours of wearable sensor data and user-reported cannabis use moments through Ecological Momentary Assessment (EMA) methods. Our analysis shows that CUDLE achieves a higher accuracy of 73.4% compared to 71.1% for the supervised approach, with the performance gap widening as the number of labels decreases. Notably, CUDLE not only surpasses the supervised model while using 75% less labels, but also reaches peak performance with far fewer subjects, indicating its efficiency in learning from both limited labels and data. These findings have significant implications for real-world applications, where data collection and annotation are labor-intensive, offering a path to more scalable and practical solutions in computational health."

# Summary. An optional shortened abstract.
summary: "CUDLE is a self-supervised learning framework that improves cannabis use detection from wearable sensor data in real-world settings, outperforming supervised methods while requiring significantly fewer labeled samples."

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

url_pdf: https://drive.google.com/file/d/1urosvaAQli0ls0Xq9goTaVtba5BpiUqh/view?usp=sharing
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
