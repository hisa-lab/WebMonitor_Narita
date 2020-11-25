import requests, bs4, os, hashlib, json, datetime
with open('URL.txt','r',encoding="utf-8") as f:
    htmls = f.read().splitlines()

for html in htmls:
    html_md5 = hashlib.md5(html.encode()).hexdigest()
    res = requests.get(html)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for script in soup(["script","style"]):
        script.decompose()
    text = soup.get_text()
    lines = [line.strip() for line in text.splitlines()]
    text="\n".join(line for line in lines if line)
    oks = []
    oks = text.splitlines()
    with open(f'{html_md5}.txt','a',encoding="utf-8") as f:
        for ok in oks:
            print(ok,file=f)
        f.flush()
        os.fsync(f.fileno())