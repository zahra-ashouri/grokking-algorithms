"""
Suppose you're starting a radio show and you want to reach listeners in all states.
There are stations, and each station covers a region and there's overlap.
Select smallest set of stations to cover all states

"""

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)
    print("states_covered:", states_covered)
    print("states_needed:", states_needed)
    print("******************")
