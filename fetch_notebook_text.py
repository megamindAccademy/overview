from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")

driver = webdriver.Edge(options=options)
url = "https://notebook.google.com/notebook/ba068196-9886-49eb-bca3-f33718919c77/artifact/8c2b324a-d227-4a20-a025-a06a442c6c7a?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_"

try:
    driver.get(url)
    time.sleep(12)
    text = driver.find_element("tag name", "body").text
    html = driver.page_source
    with open("fetched_notebook_rendered.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("fetched_notebook_rendered.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS! Length of text:", len(text))
    print("Preview:\n", text[:2000])
finally:
    driver.quit()
