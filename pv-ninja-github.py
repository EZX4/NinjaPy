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

# === GitHub Replacements ===
github_replacements = {
    "https://raw.githubusercontent.com/Demhon420666/Demhon420666/refs/heads/main/PRV":
        "https://raw.githubusercontent.com/EZX4/Paid/refs/heads/main/Permanent",
    # Add more GitHub replacements here
}

# === Pastebin Replacements ===
pastebin_replacements = {
    "https://pastebin.com/j878fVn4":
        "https://pastebin.com/raw/j878fVn4",
    # Add more Pastebin replacements here
}
redirect_telegram_to = "https://t.me/OldRingz"

# === Safe mention replacer (skip emails) ===
def replace_mentions(text):
    return re.sub(
        r'@([a-zA-Z0-9_]{1,32})(?![\w]*\.(com|net|org|pk|edu|gov|io|me|us|in|info))',
        '@OldRingz',
        text
    )

# === Stdout interceptor ===
class StdoutInterceptor:
    def write(self, text):
        modified = replace_mentions(text)
        sys.__stdout__.write(modified)
    def flush(self):
        sys.__stdout__.flush()
repr = lambda *args: f"{args}"
list = lambda *args: f"{args}"
stduot = StdoutInterceptor()
stdout = StdoutInterceptor()
sys.stdout = stduot

# === Modify Telegram sendMessage ===
def modify_telegram_text(url, data=None):
    if "api.telegram.org" in url and "sendMessage" in url:
        if data and isinstance(data, dict) and "text" in data:
            data["text"] = "CONVERTED TO FREE & PERMANENT BY JOKER | @OLDRINGZ • " + replace_mentions(data["text"])
        elif "&text=" in url:
            base, text_part = url.split("&text=", 1)
            decoded = urllib.parse.unquote(text_part)
            modified = "CONVERTED TO FREE & PERMANENT BY JOKER | @OLDRINGZ • " + replace_mentions(decoded.strip())
            encoded = urllib.parse.quote(modified)
            url = base + "&text=" + encoded
    return url, data
def modify_link_sources(url, data=None):
    def replace_from_maps(u):
        if u in github_replacements:
         
            return github_replacements[u]
        elif u in pastebin_replacements:
            
            return pastebin_replacements[u]
        return u

    
    url = replace_from_maps(url)

   
    if data and isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, str):
                data[k] = replace_from_maps(v)

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
requests.post = modified_post
original_web_open = webbrowser.open
def custom_browser_opener(url, *args, **kwargs):
    if "t.me/" in url or "telegram.me/" in url:
        url = redirect_telegram_to
    return original_web_open(url, *args, **kwargs)

webbrowser.open = custom_browser_opener

# === Show startup message ===
webbrowser.open('https://t.me/NawabiPy')
print('DECODE BY JOKER | @OldRingz')"""
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
