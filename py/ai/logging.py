"""Logging utility functions"""

# 🐍 Python standard library
from functools import wraps
from time import time

# 🐍 External libraries
# None

# 🐍 Local module imports
# None


def timer(f):
    @wraps(f)
    def g(*args, **kwargs):
        start = time()
        print("\n---")
        print(f"Running {f.__name__}() ...")
        f(*args, *kwargs)
        end = time()

        print(f"{f.__name__}() ran for {end - start} seconds")
        print("---")

    return g
