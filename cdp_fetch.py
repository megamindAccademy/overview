import subprocess
import time
import json
import urllib.request
import websocket

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
url = "https://notebook.google.com/notebook/ba068196-9886-49eb-bca3-f33718919c77/artifact/8c2b324a-d227-4a20-a025-a06a442c6c7a?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_"

proc = subprocess.Popen([edge_path, "--headless=new", "--remote-debugging-port=9222", "--disable-gpu", "--remote-allow-origins=*", url])
time.sleep(15)

try:
    res = urllib.request.urlopen("http://127.0.0.1:9222/json").read()
    targets = json.loads(res.decode())
    target = None
    for t in targets:
        if "notebook.google.com" in t.get("url", ""):
            target = t
            break
    if not target:
        target = targets[0]

    ws_url = target["webSocketDebuggerUrl"]
    ws = websocket.create_connection(ws_url)

    js_code = """
    (() => {
        function getAllText(node) {
            let text = "";
            if (node.nodeType === Node.TEXT_NODE) {
                text += node.textContent.trim() + " ";
            } else if (node.nodeType === Node.ELEMENT_NODE) {
                if (node.tagName === 'IFRAME') {
                    try {
                        let doc = node.contentDocument || node.contentWindow.document;
                        if (doc) text += getAllText(doc.body);
                    } catch(e) {}
                }
                if (node.shadowRoot) {
                    text += getAllText(node.shadowRoot);
                }
                for (let child of node.childNodes) {
                    text += getAllText(child);
                }
            }
            return text;
        }
        return getAllText(document.body);
    })()
    """

    msg = {
        "id": 1,
        "method": "Runtime.evaluate",
        "params": {
            "expression": js_code
        }
    }
    ws.send(json.dumps(msg))
    result = ws.recv()
    data = json.loads(result)
    text_content = data.get("result", {}).get("result", {}).get("value", "")

    with open("notebook_full_dump.txt", "w", encoding="utf-8") as f:
        f.write(text_content)

    # Dump full innerHTML of document.body including iframe html if possible
    js_html = "document.body.outerHTML"
    msg2 = {
        "id": 2,
        "method": "Runtime.evaluate",
        "params": {
            "expression": js_html
        }
    }
    ws.send(json.dumps(msg2))
    result2 = ws.recv()
    data2 = json.loads(result2)
    html_content = data2.get("result", {}).get("result", {}).get("value", "")

    with open("notebook_full_dump.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    ws.close()
    print("DONE! Full dump saved. Length:", len(text_content))
finally:
    proc.kill()
