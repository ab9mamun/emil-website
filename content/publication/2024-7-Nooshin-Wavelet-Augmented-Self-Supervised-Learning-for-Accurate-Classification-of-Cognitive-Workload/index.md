---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Wavelet-Augmented Self-Supervised Learning for Accurate Classification of Cognitive Workload"
authors: [Nooshin Taheri Chatrudi, Will Clegern, Robert Hager, Lonnie Nelson, Hassan Ghasemzadeh]
date: 2024-07-31T08:01:35-07:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2024-07-31T08:01:35-07:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "IEEE-EMBS International Conference on Body Sensor Networks: NextGen Health: Sensor Innovation, AI, and Social Responsibility (BSN'24)"
publication_short: "IEEE BSN 2024"

abstract: "Wearable EEG (electroencephalogram) systems have demonstrated potential in epilepsy monitoring, sleep assessment, and determining cognitive workload to improve human decision-making. However, analyzing EEG signals is challenging due to their non-stationary nature and susceptibility to noise. In particular, achieving high accuracy in machine learning tasks requires large amounts of labeled data, which is difficult to obtain due to the time-consuming and labor-intensive nature of data labeling. To address these challenges, we propose a self-supervised learning (SSL) approach for cognitive workload classification using wavelet-based augmentations of EEG signals. First, two augmentations per channel are generated, and their wavelets are computed. The visual representations of these wavelets are then fed to the SSL pretext phase as contrastive pairs to pre- train the model. Finally, the pre-trained model is fine-tuned for workload classification using small amounts of labeled EEG data. Experimental results on the EEG During Mental Arithmetic Tasks (EEGMAT) dataset show that our method outperforms the state-of-the-art supervised models. Notably, our model achieves an accuracy of 99.5% with only 50% of the labeled data, demonstrating the effectiveness of our approach in scenarios with limited labeled data availability. Furthermore, the proposed approach achieves an accuracy of 98.6% in the leave-one-subject-out analysis."

# Summary. An optional shortened abstract.
summary: "We propose a self-supervised learning (SSL) approach for cognitive workload classification using wavelet-based augmentations of EEG signals."

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

url_pdf: "papers/Wavelet-Augmented-Self-Supervised-Learning-for-Accurate-Classification-of-Cognitive-Workload.pdf"
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
