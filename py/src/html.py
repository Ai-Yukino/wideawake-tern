# 🐍 Python standard library
import urllib.request
import os.path

# 🐍 External libaries
from bs4 import BeautifulSoup

# 🐍 Local module imports
# None


def save_html(url, directory, filename):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, features="lxml")
    html = str(soup)

    path = os.path.join(directory, filename)
    with open(path, "x", encoding="utf-8") as file:
        file.write(html)
        file.close()
