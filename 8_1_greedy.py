def init_station():
    global state_need
    state_need = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
    stations['kone'] = {'id', 'nv', 'ut'}
    stations['ktwo'] = {'wa', 'id', 'mt'}
    stations['kthree'] = {'or', 'nv', 'ca'}
    stations['kfour'] = {'nv', 'ut'}
    stations['kfive'] = {'ca', 'az'}


def greedy():
    global state_need
    final_stations = set()

    while state_need:
        best_station = None
        state_covered = set()
        # 每次找出覆盖面积最大的电台
        for station, states in stations.items():
            covered = state_need & states
            if len(covered) > len(state_covered):
                best_station = station
                state_covered = covered

        # 添加进去并且去除已包含的
        state_need -= state_covered
        final_stations.add(best_station)

    return final_stations


state_need = set()
stations = {}
init_station()
print(greedy())
