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

program_start = time()

tsv_path = join("..", "data", "holocene_hub" + ".tsv")
urls = get_column(path=tsv_path, column_index=1)

test_urls = [
    urls[367],
    urls[1089],
    urls[109],
    urls[264],
    urls[375],
    urls[435],
    urls[494],
    urls[544],
    urls[749],
    urls[1247],
]

# test_urls = urls[0:99]

delays = get_delays(len(test_urls))

html_directory = join("..", "data", "holocene")
if exists(html_directory) == False:
    makedirs(html_directory)

for url, delay in zip(test_urls, delays):
    start = time()
    sleep(delay)
    save_html(
        url=url, directory=html_directory, filename=search(r"\d{6}", url)[0] + ".html"
    )
    stop = time()

    print(f"Delay: {delay}")
    print(f"Total iteration time: {stop - start}\n")

program_stop = time()

print(f"Total program time: {program_stop - program_start}")
