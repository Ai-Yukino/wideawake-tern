# 🐍 Python standard library
from os.path import join, exists
from os import makedirs
from time import time, sleep
from re import search

# 🐍 External libraries
# None

# 🐍 Local module imports
from src.tsv import get_column
from src.delay import get_delays
from src.html import save_html

# ❄ Start tracking script time
program_start = time()

# 🌸 Get urls of holocene volcanoes
tsv_path = join("..", "data", "holocene_hub" + ".tsv")
urls = get_column(path=tsv_path, column_index=1)

# ❄ Create html output directory
html_directory = join("..", "data", "holocene_pages")
if exists(html_directory) == False:
    makedirs(html_directory)

# 🌸 Create random delays for each get request
delays = get_delays(len(urls), partition=[0, 1, 2], probabilities=[0.5, 0.5])

# ❄ Request and save each page for the holocene volcanoes
for url, delay in zip(urls, delays):
    start = time()
    sleep(delay)
    save_html(
        url=url, directory=html_directory, filename=search(r"\d{6}", url)[0] + ".html"
    )
    stop = time()

    print(f"Delay: {delay}")
    print(f"Total iteration time: {stop - start}\n")

# 🌸 Output total script time
program_stop = time()
print(f"Total program time: {program_stop - program_start}")
