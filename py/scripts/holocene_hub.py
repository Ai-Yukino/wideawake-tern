# 🐍 Python standard library
import os.path

# 🐍 External libaries
# None

# 🐍 Local module imports
from src.html import save_html

save_html(
    url="https://volcano.si.edu/volcanolist_holocene.cfm",
    directory=os.path.join("..", "data", "holocene_hub"),
    filename="hub.html",
)
