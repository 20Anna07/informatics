from collections import defaultdict

def change_list(graph):
    dicty = defaultdict(list)
    for a, b in graph:
        dicty[b].append(a)
        dicty[a].append(b)
    # print(f'dicty: {dicty}')
    return dicty

def is_bipartite_dfs(graph, node, groups=None, group=0):
    if groups is None:
        groups = {}  # Словарь для хранения цветов вершин
    
    if node in groups:
        return groups[node] == group  # Проверяем, что вершина уже окрашена правильно
    
    groups[node] = group  # Красим текущую вершину в текущий цвет
    
    for neighbor in graph[node]:
        # Рекурсивно проверяем соседей, окрашивая их в противоположный цвет
        if not is_bipartite_dfs(graph, neighbor, groups, 1 - group):
            return False
    
    return True

def check_bipartite(graph):
    graph = change_list(graph)
    groups = {}  # Словарь для хранения информации о цветах вершин
    for node in graph:
        if node not in groups:  # Проверяем каждую компоненту связности
            if not is_bipartite_dfs(graph, node, groups):
                return False  # Если хоть одна компонента не двудольная, возвращаем False
    return True

n = int(input())
# dislikes = [[1,2], [1,3], [2,4]] #true
dislikes = [[1,2], [1,3], [2,3]] #false

print('true' if check_bipartite(dislikes) else 'false')