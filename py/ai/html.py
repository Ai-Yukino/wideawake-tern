# 🐍 Python standard library
from urllib.request import urlretrieve
from os.path import join

# 🐍 External libaries
# None

# 🐍 Local module imports
# None

def save_html(url, directory, filename):
    urlretrieve(url, join(directory, filename))