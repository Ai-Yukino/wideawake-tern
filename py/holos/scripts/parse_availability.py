# 🐍 Python standard library
from os.path import join
from glob import glob
from re import search

from random import sample, seed, choices

# 🐍 External libraries
from bs4 import BeautifulSoup, SoupStrainer
import polars as pl

# 🐍 Local module imports
from ai.logging import timer


@timer
def parse_availability(paths):
    # ❄ Set up columns
    volcano_numbers = []
    eruptive_history = []
    synonyms = []
    cones = []
    craters = []
    domes = []
    thermal = []

    # 🌸 Get column data for each page
    for path in paths:
        volcano_numbers.append(int(search(r"\d+", path)[0]))

        with open(path, "r") as file:
            tables = BeautifulSoup(
                markup=file,
                features="lxml",
                parse_only=SoupStrainer(name="table", attrs={"class": "DivTable"}),
            )
            file.close()

        has_eruptive_history = int(
            len(tables.select("table[title='Eruption history table for this volcano']"))
            > 0
        )
        eruptive_history.append(has_eruptive_history)

    # ❄ Export tsv file
    pl.DataFrame(
        {
            "volcano_number": volcano_numbers,
            "eruptive_history": eruptive_history,
            "synonyms": synonyms,
            "cones": cones,
            "craters": craters,
            "domes": domes,
            "thermal": thermal,
        }
    ).write_csv(join("..", "data", "tsv", "availability.tsv"), sep="\t")


if __name__ == "__main__":
    paths = glob(join("..", "data", "html", "volcano_pages", "*"))

    seed("Rubber Human")
    sample_paths = choices(paths, k=1)
    for path in sample_paths:
        print(path)
    # parse_availability(sample_paths)
