"""Main function

{Description TBA}
"""

## 🐍 Python standard library
from os.path import join
from os import makedirs

## 🐍 External packages
import requests
from bs4 import BeautifulSoup, SoupStrainer

## 🐍 Local modules
# None

## 📝 Main function
def ai():
    ### 📝 Save "Database Updates" page
    # makedirs(join("data", "html"))
    # makedirs(join("data", "tsv"))
    # r = requests.get("https://volcano.si.edu/gvp_votw.cfm")
    # with open(join("data", "html", "db_info.html"), "x") as f:
    #     f.write(r.text)
    #     f.close()

    ### 📝
    with open(join("data", "html", "db_info.html"), "r") as f:
        soup = BeautifulSoup(markup=f, features="lxml", parse_only=SoupStrainer())
        f.close()


if __name__ == "__main__":
    ai()
