"""
Utilities functions for dealing with get requests in web scraping
"""

# 🐍 Python standard library
from urllib.request import urlretrieve, urlcleanup
from os.path import join
from datetime import datetime
from time import timezone, time

import csv

from random import choices, uniform, seed

from re import search

# 🐍 Python standard library
import requests

# 🐍 Python standard library
# None


def get_page(url, directory, filename, filename_extension=".html", timestamp=False):
    """Save a single static web page"""
    urlretrieve(url, join(directory, filename + filename_extension))
    urlcleanup()


def get_column(path, column_index, sep="\t"):
    """Get a single column from a csv file ignoring the header row (tsv format by default)"""
    column = []
    with open(path, "r") as file:
        table = csv.reader(file, delimiter=sep)
        next(table)
        for row in table:
            column.append(row[column_index])
    return column


script_start = time()

data_path = join("..", "holos", "data", "holocene_hub.tsv")

urls = get_column(path=data_path, column_index=1)
seed("ara ara")
urls = choices(urls, k=10)

with requests.Session() as s:
    for url in urls:
        start = time()
        r = s.get(url)
        path = join(".", str(search(r"\d{6}", url)[0]) + ".html")
        with open(path, "x") as file:
            file.write(r.text)
        end = time()
        print(f"Total iteration time: {end - start}")

script_end = time()
print(f"Total script time: {script_end - script_start}")
