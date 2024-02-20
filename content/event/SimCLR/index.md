---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Forecasting the future clinical events of a patient through contrastive learning"
event: EMIL Summer'23 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary:  This study implemented SimCLR on EHR data to detect rare dseases. In general, rare diseases are underrepresentative classes in any clinical dataset. Therefore, using SimCLR (contrastive learning) boosts their classification accuracy.
abstract: Deep learning models for clinical event forecasting (CEF) based on a patient’s medical history have improved significantly over the past decade. However, their transition into practice has been limited, particularly for diseases with very low prevalence In this paper, we introduce CEF-CL, a novel method based on contrastive learning to forecast in the face of a limited number of positive training instances. CEF-CL consists of two primary components- (1) unsupervised contrastive learning for patient representation and (2) supervised transfer learning over the derived representation. We evaluate the new method along with state-of-the-art model architectures trained in a supervised manner with electronic health records data from Vanderbilt University Medical Center and the All of Us Research Program, covering 48 000 and 16 000 patients, respectively. We assess forecasting for over 100 diagnosis codes with respect to their area under the receiver operator characteristic curve (AUROC) and area under the precision-recall curve (AUPRC). We investigate the correlation between forecasting performance improvement and code prevalence via a Wald Test. CEF-CL achieved an average AUROC and AUPRC performance improvement over the state-of-the-art of 8.0%–9.3% and 11.7%–32 0%, respectively. The improvement in AUROC was negatively correlated with the number of positive training instances (P < .001). This investigation indicates that clinical event forecasting can be improved significantly through contrastive representation learning, especially when the number of positive training instances is small.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2023-07-12T12:30:00-07:00
date_end: 2023-07-12T13:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2022-07-12T16:45:20-07:00

authors: [asiful-arefeen]
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
url_slides: CL.pptx

url_code:
url_pdf: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9382392/pdf/ocac086.pdf"
url_video:

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