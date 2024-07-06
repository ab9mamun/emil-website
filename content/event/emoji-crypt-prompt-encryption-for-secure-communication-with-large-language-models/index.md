---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "EmojiCrypt: Prompt Encryption for Secure Communication with Large Language Models"
event: EMIL Summer'24 Seminars
event_url:
location: Online (Zoom)
address:
  street:
  city:
  region:
  postcode:
  country:
summary: This presentation discusses a new way to encrypt data with the help of LLMs
abstract: Cloud-based large language models (LLMs) such as ChatGPT have increasingly become integral to daily operations, serving as vital tools across various applications. While these models offer substantial benefits in terms of accessibility and functionality, they also introduce significant privacy concerns: the transmission and storage of user data in cloud infrastructures pose substantial risks of data breaches and unauthorized access to sensitive information, even if the transmission and storage of data is encrypted, the LLM service provider itself still knows the real contents of the data, preventing individuals or entities from confidently using such LLM services. To address these concerns, this paper proposes a simple yet effective mechanism, EmojiCrypt, to protect user privacy. It uses emojis to encrypt the user inputs before sending them to LLM, effectively rendering them indecipherable to human or LLM’s examination while retaining the original intent of the prompt, thus ensuring the model’s performance remains unaffected. We conduct experiments on three tasks, personalized recommendation, sentiment analysis, and tabular data analysis. Experiment results reveal that EmojiCrypt can encrypt personal information within prompts in such a manner that not only prevents the discernment of sensitive data by humans or LLM itself but also maintains or even improves the precision without further tuning, achieving comparable or even better task accuracy than directly prompting the LLM without prompt encryption. These results highlight the practicality of adopting encryption measures that safeguard user privacy without compromising the functional integrity and performance of LLMs. The code and dataset are available at https://github.com/agiresearch/EmojiCrypt

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2024-06-19T12:00:00-07:00
date_end: 2024-06-19T13:00:00-07:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2024-07-05T20:00:00-07:00

authors: [saman-khamesian]
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

url_code:
url_pdf: "https://arxiv.org/abs/2402.05868"
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
