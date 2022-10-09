# 🐍 Python standard library
from os.path import join, exists
from os import makedirs
from re import compile, search

# 🐍 External libaries
from bs4 import BeautifulSoup, SoupStrainer
import polars as pl

# 🐍 Local module
from ai.src.get import save_html
from ai.src.logging import timer


@timer
def get_hub(
    hub_url="https://volcano.si.edu/volcanolist_holocene.cfm",
    html_dir=join("data", "html"),
    tsv_dir=join("data", "tsv"),
    filename="hub",
):
    if not exists(html_dir):
        makedirs(html_dir)
    if not exists(tsv_dir):
        makedirs(tsv_dir)

    save_html(hub_url, html_dir, filename)

    html_path = join(html_dir, filename + ".html")
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(
            markup=f, features="lxml", parse_only=SoupStrainer(name="table", attrs={})
        )
    rows = soup("tr")[1:]

    base_url = "https://volcano.si.edu"
    urls = [join(base_url, row.contents[1].a.attrs["href"]) for row in rows]
    volcano_numbers = [int(search("\d{6}$", url)[0]) for url in urls]

    names = []
