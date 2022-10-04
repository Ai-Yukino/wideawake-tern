"""
Utilities functions for dealing with get requests in web scraping
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
def save_html(url, dir, name):
    """Save an html page from `url` to
    a local html file `name` at `dir`."""
    urlretrieve(url, join(dir, name + ".html"))
    urlcleanup()


@timer
def session_save_html(
    urls,
    directory,
    filenames,
    filename_extension=".html",
):
    "Save multiple static web pages using a single persistent HTTP connection"

    with requests.Session() as s:
        for url, filename in zip(urls, filenames):
            with requests.Session() as s:
                r = s.get(url)
                path = join(directory, filename + filename_extension)
                with open(path, "x") as file:
                    file.write(r.text)


def get_column(path, column_index, sep="\t"):
    """Get a single column from a csv file ignoring the header row (tsv format by default)"""
    column = []
    with open(path, "r") as file:
        table = csv.reader(file, delimiter=sep)
        next(table)
        for row in table:
            column.append(row[column_index])
    return column
