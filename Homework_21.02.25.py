from collections import defaultdict
def judge(n, trust):
    judges = list()

    graph = defaultdict(list)

    for a, b in trust:
        graph[b].append(a) #словарь, где ключи - человек, которому доверяют, значения - люди, которые доверяют
    # print(f'graph: {graph}')
            
    for key in graph.keys():
        if len(graph[key]) == n - 1:
            judges.append(key)   #пока здесь все, удовлетворяющие второму условию

    for i in judges:
        valu = list()
        for j in graph.values():
            for k in j:
                valu.append(k)
        if i in valu:
            judges.remove(i) #теперь здесь те, кто удовлетворяют первому условию тоже
    
    if len(judges) == 1:
        return judges[0]
    
    return -1

print(judge(2, [[1,2]]))