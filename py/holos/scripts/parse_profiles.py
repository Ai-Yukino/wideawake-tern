# 🐍 Python standard library
from os.path import join
from glob import glob
from random import seed, choices
from re import search

# 🐍 External libraries
from bs4 import BeautifulSoup, SoupStrainer
import polars as pl

# 🐍 Local module imports
# None

paths = glob(join("..", "data", "volcano_pages", "*"))
seed("Blooming in the mud by Wolpis Carter")
test_paths = choices(paths, k=10)

volcano_numbers = []
names = []
countries = []
primary_volcano_types = []
last_known_eruptions = []
latitudes = []
longitudes = []
summit_elevations_meters = []
summit_elevations_feet = []

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

        names.append(str(soup.select("div.volcano-title-container > h3")[0].string))

        li_tags = soup.select("div.volcano-info-table > ul")[0]("li")
        countries.append(str(li_tags[0].string))
        primary_volcano_types.append(str(li_tags[1].string))
        last_known_eruptions.append(int(search("^\d+", str(li_tags[2].string))[0]))

        li_tags = soup.select("div.volcano-subinfo-table > ul")[0]("li")
        latitudes.append(str(li_tags[0].string))
        longitudes.append(str(li_tags[1].string))
        volcano_numbers.append(int(li_tags[5].string))

        elevations = [string for string in li_tags[3].strings]
        summit_elevations_meters.append(int(search("^\d+", elevations[0])[0]))
        summit_elevations_feet.append(int(search("^\d+", elevations[1])[0]))

dictionary = {
    "volcano_number": volcano_numbers,
    "name": names,
    "country": countries,
    "primary_volcano_type": primary_volcano_types,
    "last_known_eruption": last_known_eruptions,
    "latitude": latitudes,
    "longitude": longitudes,
    "summit_elevation_meters": summit_elevations_meters,
    "summit_elevation_feet": summit_elevations_feet,
}

df = pl.DataFrame(dictionary)
path = join("..", "data", "profiles.tsv")
df.write_csv(path, sep="\t")
