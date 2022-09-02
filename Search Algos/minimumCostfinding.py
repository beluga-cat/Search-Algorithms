from numpy import Inf
def minimumCost(graph, root):
    n = len(graph)
    dist = [Inf for i in range(n)]
    dist[root] = 0
    visited = [False for i in range(n)]
    for i in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
            if dist[u] == Inf:
                break
            visited[u] = True
            for v, l in graph[u]:
                if dist[u] + l < dist[v]:
                    dist[v] = dist[u] + l
    return dist
graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 6), (2, 4), (4, 1)],
    4: [(2, 5), (3, 1)]
}
print(minimumCost(graph,0))