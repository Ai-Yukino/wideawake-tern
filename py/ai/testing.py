"""
Utilities functions to assist with unit tests
"""

# 🐍 Python standard library
# None

# 🐍 External libraries
import polars as pl
from polars.testing import assert_frame_equal

# 🐍 Local module imports
# None


def assert_frame_subset(left, right) -> None:
    """
    Raise detailed AssertionError if `left` is not a subset of `right`.

    Parameters
    ----------
    subset
        the supposed subset dataframe
    superset
        the supposed superset dataframe
    """

    difference = left.join(right, on=left.columns, how="anti")
    skeleton = pl.DataFrame(
        columns=[(name, t) for (name, t) in zip(left.columns, left.dtypes)]
    ).lazy()

    assert_frame_equal(difference, skeleton)


def print_col(lf, col) -> None:
    """
    Print all values from the column of `lf` specified by `col`

    Parameters
    ----------
    lf
        lazy frame
    col
        column name
    """

    ser = lf.select(col).collect()
    for i in range(0, ser.shape[0]):
        print(ser[i, 0])
