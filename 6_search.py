from collections import deque


def init_graph():
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['peggy'] = []
    graph['anuj'] = []
    graph['thom'] = []
    graph['jonny'] = []


def person_is_seller(person):
    if person[-1] == 'm':
        return True
    return False


def search(name):
    # 新建一个队列
    search_deque = deque()
    search_deque.extend(graph[name])

    # 搜索过的记录下来
    searched = []

    # 队列不为空
    while search_deque:
        person = search_deque.popleft()
        if not person in searched:
            print(person)
            searched.append(person)
            # 判断是否为所寻找的
            if person_is_seller(person):
                return person
            else:
                # 把他的所有节点添加至队列中
                search_deque.extend(graph[person])
    return None


graph = {}
init_graph()
print(search('you'))
