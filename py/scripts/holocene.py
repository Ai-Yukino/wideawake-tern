# 🐍 Python standard library
import os

# 🐍 External libraries
# None

# 🐍 Local module imports
from src.tsv import get_column

csv_path = os.path.join("..", "data", "holocene_hub" + ".tsv")
urls = get_column(path=csv_path, column_index=1)
