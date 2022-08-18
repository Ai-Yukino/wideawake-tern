# 🐍 Python standard library
from dataclasses import field
from os.path import join
from glob import glob
from random import seed, choices

# 🐍 External libraries
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd

# 🐍 Local module imports
# None

paths = glob(join("..", "data", "volcano_pages", "*"))
seed("Blooming in the mud by Wolpis Carter")
test_paths = choices(paths, k=1)

df = pd.DataFrame(
    columns=[
        "volcano_number",
        "name",
        "country",
        "primary_volcano_type",
        "last_known_eruption",
        "latitude",
        "longitude",
        "summit_elevation_meters",
        "summit_elevation_feet",
    ]
)

for path in test_paths:
    with open(path, "r") as file:
        soup = BeautifulSoup(
            markup=file,
            features="lxml",
            parse_only=SoupStrainer(
                name="div", attrs={"id": "ProfileHolocene", "class": "section"}
            ),
        )
        file.close()

    name = ""
