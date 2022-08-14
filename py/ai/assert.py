"""
Utilities functions to help with unit tests using pandas
"""

# 🐍 Python standard library
# None

# 🐍 External libraries
import pandas as pd

# 🐍 Local module imports
# None


def assert_rows_subset(subset, superset):
    """
    Checks if the set of rows of one DataFrame
    are a subset of another DataFrame's set of rows.
    """
    subset = subset.drop_duplicates()
    superset = superset.drop_duplicates()
    if subset.shape[1] != superset.shape[1]:
        return False
    else:
        return subset.merge(superset).shape == subset.shape
