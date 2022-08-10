# 🐍 Python standard library
from random import choices, uniform

# 🐍 External libraries
# None

# 🐍 Local module imports
# None


def get_delays(
    count,
    partition=[0.008, 0.7274, 2.998, 5.126, 7.942, 10.019],
    probabilities=[0.01, 0.08, 0.70, 0.20, 0.01],
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
