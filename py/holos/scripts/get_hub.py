# 🐍 Python standard library
from os.path import join, exists
from os import makedirs
from re import compile, search

# 🐍 External libaries
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd

# 🐍 Local module imports
from ai.get import get_page

# ❄ Create base variables
base_url = "https://volcano.si.edu"
base_name = "holocene_hub"

# 🌸 Create data directory
data_directory = join("..", "data")

if exists(data_directory) == False:
    makedirs(data_directory)

# ❄ Save html file
html_url = join(base_url, "volcanolist_holocene.cfm")
html_filename = base_name
html_path = join(data_directory, html_filename + ".html")

if exists(html_path) == False:
    get_page(
        url=html_url,
        directory=data_directory,
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
urls = [join(base_url, row.contents[1].a.attrs["href"]) for row in rows]
volcano_numbers = [int(search("\d{6}", url)[0]) for url in urls]

names = [row.contents[1].string for row in rows]
subregions = [row.contents[3].string for row in rows]
volcano_types = [row.contents[5].string for row in rows]
evidences = [
    compile(
        r"^ ",
    ).sub("", row.contents[7].string)
    for row in rows
]

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

tsv_path = join(data_directory, base_name + ".tsv")

if exists(tsv_path) == False:
    df.to_csv(tsv_path, sep="\t", index=False)
