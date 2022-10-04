# 🐍 Python standard library
from os.path import join, exists
from os import makedirs
from re import compile, search

# 🐍 External libaries
from bs4 import BeautifulSoup, SoupStrainer
import polars as pl

# 🐍 Local module imports
from ai.src.get import get_page


def get_hub():
    url = "https://volcano.si.edu/volcanolist_holocene.cfm"
