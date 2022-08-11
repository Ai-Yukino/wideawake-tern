# 🐍 Python standard library
import csv

# 🐍 External libraries
# None

# 🐍 Local module imports
# None


def get_column(path, column_index):
    column = []
    with open(path, "r") as file:
        csv_table = csv.reader(file, delimiter="\t")
        next(csv_table)
        for row in csv_table:
            column.append(row[column_index])
    return column
