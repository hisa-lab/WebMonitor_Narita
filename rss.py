import requests, bs4, os, hashlib, json, datetime, feedparser

with open('RSSURL.txt','r',encoding="utf-8") as f:
    htmls = f.read().splitlines()

for html in htmls:
    fdp = feedparser.parse(html)
    rawhtml = html.replace('/','').replace(':','').replace('https','').replace('http','')
    with open('rss/'f'{rawhtml}''.json','w',encoding="utf-8") as f:
        for entry in fdp.entries:
            jexport = {
                    "url" : f"{entry.link}",
                    "update" : f"{entry.date}",
                    "contents" : f"{entry.title}",
            }
            json.dump(jexport,f,indent=2,ensure_ascii=False)


