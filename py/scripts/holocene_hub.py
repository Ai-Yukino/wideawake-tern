# 🐍 Python standard library
import os
import re

# 🐍 External libaries
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd

# 🐍 Local module imports
from src.html import save_html

# ❄ Save html file
html_url = "https://volcano.si.edu/volcanolist_holocene.cfm"
html_directory = os.path.join("..", "data", "holocene_hub")
html_filename = "hub.html"
html_path = os.path.join(html_directory, html_filename)

if os.path.exists(html_directory) == False:
    os.makedirs(html_directory)

if os.path.exists(html_path) == False:
    save_html(
        url=html_url,
        directory=html_directory,
        filename=html_filename,
    )

# 🌸 Make soup
with open(html_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(
        markup=file, features="lxml", parse_only=SoupStrainer(name="table", attrs={})
    )

# ❄ Get rows
rows = soup("tr")[1:]

# 🌸 Extract columns
base_url = "https://volcano.si.edu"
urls = [os.path.join(base_url, row.contents[1].a.attrs["href"]) for row in rows]

volcano_numbers = [int(re.search("\d{6}", url)[0]) for url in urls]

names = [row.contents[1].string for row in rows]
subregions = [row.contents[3].string for row in rows]
volcano_types = [row.contents[5].string for row in rows]
evidences = [row.contents[7].string for row in rows]

# ❄ Save tsv file
dictionary = {
    "volcano_number": volcano_numbers,
    "url": urls,
    "name": names,
    "subregion": subregions,
    "volcano_type": volcano_types,
    "evidence": evidences,
}
df = pd.DataFrame(dictionary)

tsv_path = os.path.join("..", "data", "holocene_hub", "hub.tsv")
df.to_csv(tsv_path, sep="\t", index=False)
