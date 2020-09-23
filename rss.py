import feedparser

url='https://gigazine.net/index.php?/news/rss_2.0/'
 
a = feedparser.parse(url)
for entry in a.entries:
    print(entry.title,entry.link)

