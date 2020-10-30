import requests, bs4, os, hashlib, json, datetime
htmls = ['https://gigazine.net/','https://tonari-it.com/','https://getnews.jp/']

dt_now = datetime.datetime.now()
for html in htmls:
    html_md5 = hashlib.md5(html.encode()).hexdigest()
    res = requests.get(html)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('h2')
    gets = []
    with open(f'{html_md5}.txt','a',encoding="utf-8") as f:
        pass
        f.flush()
        os.fsync(f.fileno())
    judge = os.path.getsize(f'{html_md5}.txt')
    if judge != 0:
        with open(f'{html_md5}.txt','r',encoding="utf-8") as f:
            beforelists = f.read().splitlines()
        with open(f'{html_md5}.txt','w',encoding="utf-8") as f:
            for elem in elems:
                print(elem.get_text(),file=f)
                gets.append(elem.get_text())
            f.flush()
            os.fsync(f.fileno())
        diff = list(filter(lambda x: x not in beforelists,gets))
        jexport = {
                    "url" : f"{html}",
                    "update" : f"{dt_now}",
                    "contents" : f"{diff}"
        }
        with open(f'{html_md5}.json','w',encoding="utf-8") as f:
            json.dump(jexport,f,indent=2,ensure_ascii=False)
    else:
        with open(f'{html_md5}.txt','w',encoding="utf-8") as f:
            for elem in elems:
                print(elem.get_text(),file=f)
            f.flush()
            os.fsync(f.fileno())
