"""
Utilities functions to assist with unit tests
"""

# 🐍 Python standard library
from random import seed, choices

try:
    # hashlib is pretty heavy to load, try lean internal module first
    from _sha512 import sha512 as _sha512
except ImportError:
    # fallback to official implementation
    from hashlib import sha512 as _sha512

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


def print_col(table, col=None, n=None, s="uwu", path=None) -> None:
    """
    Print values from the column of `table` specified by `col`;
    If `k` is specified, then only `k` many values are sampled
    using `seed` and printed out.
    If `path` is specified, then the values are saved to a
    tsv file at `path`.

    Parameters
    ----------
    table
        Polars LazyFrame, Polars DataFrame, or path to tsv file
    col
        column name
    n
        number of samples
    s
        random seed
    path
        file path to write values to
    """

    if type(table) is str:
        lf = pl.scan_csv(table, sep="\t")
    elif type(table) is pl.DataFrame:
        lf = table.lazy()

    if col is None:
        col = lf.columns[0]

    ser = lf.select(col).collect()
    if n is not None:
        seed(s)
        indices = choices(range(0, ser.shape[0]), k=n)
    else:
        indices = range(0, ser.shape[0])

    for i in indices:
        print(ser[i, 0])

    if path is not None:
        with open(path, "x") as file:
            file.write("values:\n")
            for i in indices:
                file.write(f"{ser[i, 0]}\n")
            file.close()


def z(s) -> int:
    """
    Converts a string `s` to an integer;
    taken from `seed()` in the standard
    random library

    Parameters
    ----------
    s
        string to be converted to an integer
    """
    s = s.encode()
    s = int.from_bytes(s + _sha512(s).digest(), "big")
    return s
