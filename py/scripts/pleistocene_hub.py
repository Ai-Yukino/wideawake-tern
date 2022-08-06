# 🐍 Python standard library
import os.path

# 🐍 External libaries
# None

# 🐍 Local module imports
from src.html import save_html

save_html(
    url="https://volcano.si.edu/volcanolist_pleistocene.cfm",
    directory=os.path.join("..", "data", "pleistocene_hub"),
    filename="hub.html",
)
