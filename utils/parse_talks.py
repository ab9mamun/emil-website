from datetime import datetime
import re 
import os
from pathlib import Path


author_to_user = {
	"Hassan Ghasemzadeh": "hassan-ghasemzadeh",
	"Seyed Iman Mirzadeh": "iman-mirzadeh",
	"Iman Mirzadeh": "iman-mirzadeh",
	"Ramesh Kr Sah": "ramesh-sah",
	"Ramesh Sah": "ramesh-sah",
	"Parastoo Alinia": "parastoo-alinia",
	"Niloofar Hezarjaribi": "niloofar-hezarjaribi",
	"Seyed Ali Rokni": "seyed-ali-rokni",
	"Ali Rokni": "seyed-ali-rokni",
	"Ramin Fallahzadeh": "ramin-fallahzadeh",
	"Mahdi Pedram": "mahdi-pedram",
	"Yuchao Ma": "yuchao-ma",
	"Marjan Nourollahi": "marjan",
}


# ORDER:
# Title ==> date ==> date => author

template = '''
---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "{}"
event:
event_url:
location: Dana Hall, Washington State University
address:
  street:
  city:
  region:
  postcode:
  country:
summary:
abstract:

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: {}T12:00:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: {}

authors: {}
tags: []

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page folder. 
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

# Optional filename of your slides within your talk folder or a URL.
url_slides:

url_code:
url_pdf:
url_video:

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
'''

def extract_date(line):
	start = line.find('[')
	end = line.find(']')
	return line[start+1:end]

def parse_date(line):
	date_str = extract_date(line)
	date_object = datetime.strptime(date_str, "%m/%d/%Y")
	return date_object.strftime("%Y-%m-%d")

def parse_authors(line):
	result = []
	authors = {}
	match = re.search('\[(.+?)\]', line[2:])
	if match:
		authors = str(match.group(1)).strip().split(',')
		for author in authors:
			author = author.strip()
			if author_to_user.get(author):
				result.append(author_to_user[author])
			else:
				result.append(author)
	# if not result:
		# print(line)
	return re.sub("[']", '', str(result))

def parse_title(line):
			line = line[14:]
			title = line[line.find(']')+1:].strip()
			
			if title[0] == ':':
				title = title[1:].strip()
			# print(title)

			match_1 = re.search('“(.+?)”', title)
			result = None
			if match_1:
				result = match_1.group(1).strip()

			match_2 = re.search('"(.+?)"', title)
			if match_2:
				if result:
					raise Exception("both occured")
				else:
					result = match_2.group(1).strip()
			
			if not match_1 and not match_2:
				result = title
			return result

def import_talks():
	with open('./talks.txt', 'r') as f:
		for line in f.readlines():
			line = line.strip()
			if not line:
				continue
			# parse date
			date = parse_date(line)

			# parse author
			authors = parse_authors(line)


			title = parse_title(line)

			bundle_path = "./content/talk/{}".format(slugify(title))
			markdown_path = os.path.join(bundle_path, "index.md")
			# print(template.format(title, date, date, authors))
			Path(bundle_path).mkdir(parents=True, exist_ok=True)
			with open(markdown_path, "w", encoding="utf-8") as f:
				f.write(template.format(title, date, date, authors))
			print(bundle_path)


def slugify(s, lower=True):
	bad_symbols = (".", "_", ":")  # Symbols to replace with hyphen delimiter.
	delimiter = "-"
	good_symbols = (delimiter,)  # Symbols to keep.
	for r in bad_symbols:
		s = s.replace(r, delimiter)

	s = re.sub(r"(\D+)(\d+)", r"\1\-\2", s)  # Delimit non-number, number.
	s = re.sub(r"(\d+)(\D+)", r"\1\-\2", s)  # Delimit number, non-number.
	s = re.sub(r"((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))", r"\-\1", s)  # Delimit camelcase.
	s = "".join(c for c in s if c.isalnum() or c in good_symbols).strip()  # Strip non-alphanumeric and non-hyphen.
	s = re.sub("-{2,}", "-", s)  # Remove consecutive hyphens.

	if lower:
		s = s.lower()
	return s

	
if __name__ == "__main__":
	import_talks()
