# 🐍 Python standard library
import os.path

# 🐍 External libaries
# None

# 🐍 Local module imports
from src.html import save_html

# 📝 Save html file
html_url = "https://volcano.si.edu/volcanolist_pleistocene.cfm"
html_directory = os.path.join("..", "data", "pleistocene_hub")
html_filename = "hub.html"

if os.path.exists(os.path.join(html_directory, html_filename)) == False:
    save_html(
        url=html_url,
        directory=html_directory,
        filename=html_filename,
    )

# 📝 Parse html file
