# 🐍 Python standard library
from random import choices, uniform

# 🐍 External libraries
# None

# 🐍 Local module imports
# None


def get_delays(
    count,
    partition=[0, 1, 3],
    probabilities=[0.20, 0.80],
    verbose=False,
):
    delays = []

    indices = choices(range(0, len(partition) - 1), weights=probabilities, k=count)

    for index in indices:
        delays.append(uniform(partition[index], partition[index + 1]))

    if verbose == True:
        for index, delay in zip(indices, delays):
            print(f"index: {index}")
            print(f"interval: ({partition[index]}, {partition[index + 1]})")
            print(f"delay: {delay}")

    return delays
