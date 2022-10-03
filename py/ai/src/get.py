"""
Utilities functions for dealing with get requests in web scraping
"""

# 🐍 Python standard library
from os.path import join
from urllib.request import urlretrieve, urlcleanup
import csv
from random import choices, seed

# 🐍 External libraries
import requests

# 🐍 Local modules
from ai.src.logging import timer


@timer
def save(url, path):
    """Save the network object at `url` to a local file at `path`."""
    urlretrieve(url, path)
    urlcleanup()


@timer
def get_pages(
    urls,
    directory,
    filenames,
    filename_extension=".html",
    sample_size=-1,
    sample_seed="uwu",
):
    "Save multiple static web pages"

    if 0 < sample_size < len(urls):
        seed(sample_seed)
        sample_indices = choices(range(0, len(urls)), k=sample_size)
        urls = [urls[index] for index in sample_indices]
        filenames = [filenames[index] for index in sample_indices]

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
