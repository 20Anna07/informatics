from collections import defaultdict
def judge(n, trust):
    count = 0
    judges = list()

    graph = dict.fromkeys(i for i in range(n))

    for a, b in trust:
        graph[a].append(b)

    for i in range(1, n + 1):
        if len(graph[i]) == n - 1:
            count += 1
            judges.append(i)
            if count > 1:
                return -1
    
    return judges[0]

print(judge(3, [[1,3], [2,3]]))