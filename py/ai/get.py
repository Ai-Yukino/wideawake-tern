"""
Utilities functions for dealing with get requests in web scraping
"""

# 🐍 Python standard library
from urllib.request import urlretrieve, urlcleanup
from os.path import join
from datetime import datetime
from time import timezone

import csv

from random import choices, uniform

# 🐍 Python standard library
# None

# 🐍 Python standard library
# None


def page(url, directory, filename, filename_extension=".html", timestamp=False):
    """Save a single static web page"""
    if timestamp == False:
        urlretrieve(url, join(directory, filename + filename_extension))
        urlcleanup()
    elif timestamp == True:
        urlretrieve(
            url,
            join(
                directory,
                filename
                + datetime.now().strftime("_%Y%m%d_%H%M%S")
                + f"_{(timezone / 3600.00):.0f}"
                + filename_extension,
            ),
        )
        urlcleanup()


page(
    url="https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime",
    directory=".",
    filename="test",
    timestamp=True,
)


def pages():
    pass


def column(path, column_index, sep="\t"):
    """Get a single column from a csv file (tsv format by default)"""
    column = []
    with open(path, "r") as file:
        table = csv.reader(file, delimiter=sep)
        next(table)
        for row in table:
            column.append(row[column_index])
    return column


def delays(
    count,
    partition=[0, 0.85, 2.25],
    probabilities=[0.60, 0.40],
    verbose=False,
):
    """Generate a random list of delay times"""
    delays = []

    indices = choices(range(0, len(partition) - 1), weights=probabilities, k=count)

    for index in indices:
        delays.append(uniform(partition[index], partition[index + 1]))

    if verbose == True:
        for index, delay in zip(indices, delays):
            print(f"index: {index}")
            print(f"interval: ({partition[index]}, {partition[index + 1]})")
            print(f"delay: {delay}")

    return delays
