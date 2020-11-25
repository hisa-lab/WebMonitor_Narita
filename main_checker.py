import requests, bs4, os, hashlib, json, datetime, http.server, socketserver
with open('URL.txt','r',encoding="utf-8") as f:
    htmls = f.read().splitlines()
dt_now = datetime.datetime.now()


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
    rawhtml = html.replace('/','').replace(':','').replace('https','').replace('http','')
    with open(f'{html_md5}.txt','a',encoding="utf-8") as f:
        pass
        f.flush()
        os.fsync(f.fileno())
    judge = os.path.getsize(f'{html_md5}.txt')
    if judge != 0:
        with open(f'{html_md5}.txt','r',encoding="utf-8") as f:
            beforelists = f.read().splitlines()
        diff = list(filter(lambda x: x not in beforelists,oks))
        jexport = {
                    "url" : f"{html}",
                    "update" : f"{dt_now}",
                    "contents" : f"{diff}"
        }
        with open('links/'f'{rawhtml}''.json','w',encoding="utf-8") as f:
            json.dump(jexport,f,indent=2,ensure_ascii=False)
    else:
        pass

#PORT = 8000
#DIRECTORY="links"
#class Handler(http.server.SimpleHTTPRequestHandler):
#    def __init__(self,*args,**kwargs):
#        super().__init__(*args,directory=DIRECTORY,**kwargs)
#with socketserver.TCPServer(("", PORT), Handler) as httpd:
#    print("serving at port", PORT)
#    httpd.serve_forever()
