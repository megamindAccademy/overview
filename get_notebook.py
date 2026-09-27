import subprocess
import time
import json
import urllib.request
import asyncio
import sys

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
url = "https://notebook.google.com/notebook/ba068196-9886-49eb-bca3-f33718919c77/artifact/8c2b324a-d227-4a20-a025-a06a442c6c7a?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_"

proc = subprocess.Popen([edge_path, "--headless=new", "--remote-debugging-port=9222", "--disable-gpu", url])
time.sleep(8)

try:
    req = urllib.request.urlopen("http://127.0.0.1:9222/json")
    targets = json.loads(req.read().decode())
    print("CDP Targets:", len(targets))
    for t in targets:
        print(t.get("title"), t.get("url"))
        ws_url = t.get("webSocketDebuggerUrl")
        if ws_url:
            print("WebSocket URL:", ws_url)
finally:
    proc.kill()
