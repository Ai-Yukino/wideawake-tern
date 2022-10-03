"""
Utilities functions for dealing with get requests in web scraping
"""

# 🐍 Python standard library
from urllib.request import urlretrieve, urlcleanup
from os.path import join
from time import time
import csv
from random import choices, seed

# 🐍 Python standard library
import requests

# 🐍 Python standard library
# None


def get_page(url, directory, filename, filename_extension=".html"):
    """Save a single static web page"""
    start = time()

    urlretrieve(url, join(directory, filename + filename_extension))
    urlcleanup()

    end = time()
    print("\n---")
    print(f"url: {url}")
    print(f"get_page() ran for {end - start} seconds")
    print("---")


def get_pages(
    urls,
    directory,
    filenames,
    filename_extension=".html",
    sample_size=-1,
    sample_seed="uwu",
):
    "Same multiple static web pages"
    function_start = time()

    if 0 < sample_size < len(urls):
        seed(sample_seed)
        sample_indices = choices(range(0, len(urls)), k=sample_size)
        urls = [urls[index] for index in sample_indices]
        filenames = [filenames[index] for index in sample_indices]

    with requests.Session() as s:
        i = 1
        for url, filename in zip(urls, filenames):
            start = time()
            with requests.Session() as s:
                r = s.get(url)
                path = join(directory, filename + filename_extension)
                with open(path, "x") as file:
                    file.write(r.text)
            end = time()

            print("\n---")
            print(f"Iteration: {i}")
            print(f"url: {url}")
            print(f"Time elapsed: {end - start}")
            print("---")
            i += 1

    function_end = time()
    print(f"get_pages() ran for {function_end - function_start} seconds")


def get_column(path, column_index, sep="\t"):
    """Get a single column from a csv file ignoring the header row (tsv format by default)"""
    column = []
    with open(path, "r") as file:
        table = csv.reader(file, delimiter=sep)
        next(table)
        for row in table:
            column.append(row[column_index])
    return column
