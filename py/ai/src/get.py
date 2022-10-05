"""
Utilitiy functions to help with get requests
"""

# 🐍 Python standard library
from os.path import join
from urllib.request import urlretrieve, urlcleanup
import csv

# 🐍 External libraries
import requests

# 🐍 Local modules
from ai.src.logging import timer


@timer
def save_html(url, dir, filename):
    """Save an html page from `url` to
    a local html file `name` at `dir`."""
    urlretrieve(url, join(dir, filename + ".html"))
    urlcleanup()


@timer
def session_save_html(
    urls,
    dir,
    filenames,
):
    """Use a single persistent HTTP connection
    to save multiple html pages from `urls` to
    local html files `names` at `dir`"""

    with requests.Session() as s:
        for url, filename in zip(urls, filenames):
            with requests.Session() as s:
                r = s.get(url)
                path = join(dir, filename + ".html")
                with open(path, "x") as f:
                    f.write(r.text)


def get_column(path, column_index):
    """Get a single column from a tsv file
    ignoring the header row"""
    column = []
    with open(path, "r") as f:
        table = csv.reader(f, delimiter="\t")
        next(table)
        for row in table:
            column.append(row[column_index])
    return column
