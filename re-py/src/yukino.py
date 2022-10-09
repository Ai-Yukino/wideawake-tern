"""Main module for local `src` package

{Description TBA}

"""

# 🐍 Python standard library
from functools import wraps
from time import time

# 🐍 External libraries
# None

# 🐍 Local modules
# None


def time_this(f):
    """Returns a function `g` which
    runs the function `f` and
    prints its execution time
    """

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
