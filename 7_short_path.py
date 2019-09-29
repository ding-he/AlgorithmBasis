def init_graph():
    graph['musicpaper'] = {}
    graph['musicpaper']['CD'] = 5
    graph['musicpaper']['newspaper'] = 0
    graph['CD'] = {}
    graph['CD']['guitar'] = 15
    graph['CD']['drum'] = 20
    graph['newspaper'] = {}
    graph['newspaper']['guitar'] = 30
    graph['newspaper']['drum'] = 35
    graph['guitar'] = {}
    graph['guitar']['piano'] = 20
    graph['drum'] = {}
    graph['drum']['piano'] = 10
    graph['piano'] = {}

    costs['musicpaper'] = float('inf')
    costs['CD'] = float('inf')
    costs['newspaper'] = float('inf')
    costs['guitar'] = float('inf')
    costs['drum'] = float('inf')
    costs['piano'] = float('inf')

    '''
    costs['CD'] = 5
    costs['newspaper'] = 0
    costs['piano'] = float('inf')
    

    parents['CD'] = 'musicpaper'
    parents['newspaper'] = 'musicpaper'
    '''


def find_lostnode():
    low_cost = float('inf')
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = cost
            low_cost_node = node

    return low_cost_node


def short_path(start):
    # 初始化costs和parents
    for (key, value) in graph[start].items():
        costs[key] = value
        parents[key] = start

    # 找到权重最小的节点
    node = find_lostnode()
    while node is not None:
        # 找到所有邻近节点
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            # new cost
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost or costs[n] is None:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lostnode()

    weight = costs['piano']
    path = []
    node = 'piano'
    while node in parents:
        path.append(node)
        node = parents[node]
    path.append(node)

    return path[::-1], weight


graph = {}
costs = {}
parents = {}
processed = []
init_graph()
(path, weight) = short_path('musicpaper')
print(weight)
for p in path:
    print(p, end=' -> ')
print('\b'*4)
