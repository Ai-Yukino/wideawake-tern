# 🐍 Python standard library
# None

# 🐍 External libraries
import polars as pl

# 🐍 Local module imports
# None

start_dates = []
stop_dates = []
eruption_certainties = []
veis = []
evidences = []
activity_areas_or_units = []

start_dates.append("[ 1854 Dec 23")
stop_dates.append("1855 Jan 9 ]")
eruption_certainties.append("Uncertain")
veis.append(None)
evidences.append(None)
activity_areas_or_units.append(None)

dictionary = {
    "start_date": start_dates,
    "stop_date": stop_dates,
    "eruption_certainty": eruption_certainties,
    "vei": veis,
    "evidence": evidences,
    "activity_area_or_unit": activity_areas_or_units,
}

pl.DataFrame(dictionary).write_csv("uwu.tsv", sep="\t")
