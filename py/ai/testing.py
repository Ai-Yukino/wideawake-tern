"""
Utilities functions to assist with unit tests
"""

# 🐍 Python standard library
from random import seed, choices

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


def print_col(lf, col, sample_size=None, seed_value="uwu") -> None:
    """
    Print values from the column of `lf` specified by `col`;
    If `sample_size` is specified, then only `sample_size` many
    values are sampled using `seed` and printed out.

    Parameters
    ----------
    lf
        lazy frame
    col
        column name
    sample_size
        number of samples
    seed_value
        value to use as a random seed
    """

    ser = lf.select(col).collect()
    if sample_size is not None:
        seed(seed_value)
        indices = choices(range(0, ser.shape[0]), k=sample_size)
    else:
        indices = range(0, ser.shape[0])

    for i in indices:
        print(ser[i, 0])
