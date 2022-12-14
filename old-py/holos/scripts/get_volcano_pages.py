# 🐍 Python standard library
from os.path import join, exists
from os import makedirs
from re import search

# 🐍 External libraries
# None

# 🐍 Local module imports
from ai.get import get_column, get_pages

# 🌸 Get urls of volcanoes
tsv_path = join("..", "data", "tsv", "hub.tsv")
urls = get_column(path=tsv_path, column_index=1)

# ❄ Create html output directory
html_directory = join("..", "data", "html", "volcano_pages")
if exists(html_directory) == False:
    makedirs(html_directory)

# 🌸 Create filenames for html files
html_filenames = [search(r"\d+$", url)[0] for url in urls]

# ❄ Get volcano pages
get_pages(urls=urls, directory=html_directory, filenames=html_filenames)
