import requests, bs4, os
res = requests.get('https://gigazine.net/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select('h2')
for elem in elems:
    with open('file.txt','a') as f:
     print(elem.get_text(),file=f)

delfile = 'file.txt'

with open("before.txt","r") as f:
    beforelists = f.read().splitlines()
with open("after.txt","r") as f:
    afterlists = f.read().splitlines()

diff = list(set(afterlists)-set(beforelists))

with open('result.txt','w') as f:
    for check in diff:
        print(check,file=f)

#os.remove(delfile)