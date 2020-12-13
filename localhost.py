import requests, bs4, os, hashlib, json, datetime, http.server, socketserver

PORT = 8000
DIRECTORY="links"
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory=DIRECTORY,**kwargs)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()