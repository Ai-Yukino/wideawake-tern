# 🐍 Python standard library
from os.path import join
from glob import glob

from random import seed, choices

# 🐍 External libraries
from bs4 import BeautifulSoup, SoupStrainer
import polars as pl

# 🐍 Local module imports
from ai.logging import timer


@timer
def parse_availability(paths):
    # ❄ Set up columns
    volcano_numbers = []
    eruption_history = []
    synonyms = []
    cones = []
    craters = []
    domes = []
    thermal = []

    # 🌸 Get column data for each page
    for path in paths:
        with open(path, "r") as file:
            soup = BeautifulSoup(
                markup=file,
                features="lxml",
                parse_only=SoupStrainer(),
            )
            file.close()

    # ❄ Export tsv file
    pl.DataFrame(
        {
            "volcano_number": volcano_numbers,
            "eruption_history": eruption_history,
            "synonyms": synonyms,
            "cones": cones,
            "craters": craters,
            "domes": domes,
            "thermal": thermal
        }
    ).write_csv(join("..", "data", "tsv", "availability.tsv"), sep="\t")


if __name__ == "__main__":
    paths = glob(join("..", "data", "html", "volcano_pages", "*"))

    seed("zutomayo - study me")
    sample_paths = choices(paths, k=1)
    parse_availability(paths)
