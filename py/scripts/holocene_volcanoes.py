# 🐍 Python standard library
from os.path import join
from time import time, sleep

# 🐍 External libraries
# None

# 🐍 Local module imports
from src.tsv import get_column

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

for url in test_urls:
    print(url)
