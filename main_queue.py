import requests, bs4, os, hashlib, json, datetime
htmls = ['https://gigazine.net/','https://tonari-it.com/','https://getnews.jp/']

for html in htmls:
    html_md5 = hashlib.md5(html.encode()).hexdigest()
    res = requests.get(html)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('h2')
    with open(f'{html_md5}.txt','a',encoding="utf-8") as f:
        for elem in elems:
            print(elem.get_text(),file=f)
        f.flush()
        os.fsync(f.fileno())