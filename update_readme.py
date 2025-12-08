import os
import feedparser
import re

HASHNODE_USERNAME = 'thatmoodygirl'
RSS_FEED = f'https://rakshapahariya.hashnode.dev/rss.xml'
README_TEMPLATE = 'README_TEMPLATE.md'
README_OUTPUT = 'README.md'

folders = sorted([f for f in os.listdir('.') if os.path.isdir(f) and f.upper().startswith('DAY')])

feed = feedparser.parse(RSS_FEED)
blog_links = {}

for entry in feed.entries:
    match = re.search(r'Day\s*(\d+)', entry.title, re.IGNORECASE)
    if match:
        day_num = int(match.group(1))
        folder_name = f'DAY{day_num:02d}'
        blog_links[folder_name] = entry.link

table_rows = []
for idx, folder in enumerate(folders, 1):
    blog_link = blog_links.get(folder, "#")
    
    blog_title = None
    for entry in feed.entries:
        if re.search(rf'Day\s*{idx}', entry.title, re.IGNORECASE):
            blog_title = entry.title
            break
    if not blog_title:
        blog_title = "Blog"
    
    table_rows.append(f"| Day {idx:02d} | [{folder}](./{folder}) | [{blog_title}]({blog_link}) |")


table_md = "\n".join(table_rows)
with open(README_TEMPLATE, "r") as f:
    content = f.read()

content = content.replace("<!--DAY_TABLE-->", table_md)

with open(README_OUTPUT, "w") as f:
    f.write(content)

print("README.md updated successfully with latest blog links!")
