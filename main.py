import requests, bs4, os ,smtplib ,ssl ,hashlib ,copy
from email.mime.text import MIMEText

htmls = ['https://gigazine.net/','http://blog.livedoor.jp/itsoku/','https://nlab.itmedia.co.jp/']

for html in htmls:
    html_md5 = hashlib.md5(b'{html}').hexdigest()
    res = requests.get(html)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('h2')
    with open(f'{html_md5}.txt','w') as f:
        for elem in elems:
            print(elem.get_text(),file=f)
    with open(f'{html_md5}' + 'before.txt','r') as f:
        beforelists = f.read().splitlines()
    with open(f'{html_md5}.txt','r') as f:
        nowlists = f.read().splitlines()
    diff = list(set(nowlists)-set(beforelists))
    with open(f'{html_md5}' + 'result.txt','w') as f:
        for check in diff:
            print(check,file=f)
    with open(f'{html_md5}' + 'before.txt','w') as f:
        for nowlist in nowlists:
            print(nowlist,file=f)