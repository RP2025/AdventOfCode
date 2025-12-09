from bs4 import BeautifulSoup

# If you have downloaded rss.xml
with open("rss.xml", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "xml")
items = soup.find_all("item")

for i, item in enumerate(items, 1):
    title = item.find("title").text.strip()
    link = item.find("link").text.strip()
    print(f"{i}. {title} — {link}")
