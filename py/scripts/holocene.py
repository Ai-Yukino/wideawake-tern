# 🐍 Python standard library
import os
import timeit
import csv

# 🐍 External libraries
import pandas as pd

# 🐍 Local module imports
from src.tsv import get_column

csv_path = os.path.join("..", "data", "holocene_hub" + ".tsv")
urls = get_column(path=csv_path, column_index=1)
