import requests, bs4, os ,hashlib
htmls = ['https://gigazine.net/','http://blog.livedoor.jp/itsoku/','https://nlab.itmedia.co.jp/']


for html in htmls:
    nowhtml = html
    html_md5 = hashlib.md5(b'{nowhtml}').hexdigest()
    res = requests.get(nowhtml)
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
        with open(f'{html_md5}' + 'result.txt','w',encoding="utf-8") as f:
            for check in diff:
                print(check,file=f)
            f.flush()
            os.fsync(f.fileno())
    else:
        with open(f'{html_md5}.txt','w',encoding="utf-8") as f:
            for elem in elems:
                print(elem.get_text(),file=f)
            f.flush()
            os.fsync(f.fileno())
        with open(f'{html_md5}' + 'result.txt','a',encoding="utf-8") as f:
            pass
            f.flush()
            os.fsync(f.fileno())
