# 🐍 Python standard library
import os.path
import re

# 🐍 External libaries
from bs4 import BeautifulSoup, SoupStrainer

# 🐍 Local module imports
from src.html import save_html

# 📝 Save html file
html_url = "https://volcano.si.edu/volcanolist_holocene.cfm"
html_directory = os.path.join("..", "data", "holocene_hub")
html_filename = "hub.html"
html_path = os.path.join(html_directory, html_filename)

if os.path.exists(html_path) == False:
    save_html(
        url=html_url,
        directory=html_directory,
        filename=html_filename,
    )

# 🍲 Make soup
strainer = SoupStrainer(name="table", attrs={})

with open(html_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(markup=file, features="lxml", parse_only=strainer)

## ❄ Get rows
rows = soup("tr")

## 🌸 Extract "url" column
base_url = "https://volcano.si.edu"
urls = [
    os.path.join(base_url, rows[i].contents[1].a.attrs["href"]) for i in range(1, 1338)
]

## ❄ Extract "volcano_number" column
volcano_numbers = [int(re.search("\d{6}$", urls[i])[0]) for i in range(0, 1337)]
