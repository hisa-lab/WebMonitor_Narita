import requests, bs4, os, hashlib, json, datetime, feedparser

with open('RSSURL.txt','r',encoding="utf-8") as f:
    htmls = f.read().splitlines()

for html in htmls:
    fdp = feedparser.parse(html)
    rawhtml = html.replace('/','').replace(':','').replace('https','').replace('http','')
    jexport = {"url":"","update":"","contents":""}
    jt=[]
    with open('rss/'f'{rawhtml}''.json','w',encoding="utf-8") as f:    
        for entry in fdp.entries:
            jexport["url"] = f"{entry.link}"
            jexport["update"] = f"{entry.date}"
            jexport["contents"] = f"{entry.title}"
            jt.append(jexport)
            jexport={}
        json.dump(jt,f,indent=2,ensure_ascii=False)


