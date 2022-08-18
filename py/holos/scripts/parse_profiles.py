# 🐍 Python standard library
from os.path import join
from glob import glob
from random import seed, choices

# 🐍 External libraries
from bs4 import BeautifulSoup, SoupStrainer

# 🐍 Local module imports
# None

paths = glob(join("..", "data", "volcano_pages", "*"))
seed("Blooming in the mud by Wolpis Carter")
test_paths = choices(paths, k=1)
