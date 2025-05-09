
from collections import deque, defaultdict

def bfs_traversal(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)


    for node in graph:
        graph[node].sort()

    visited = [False] * (n + 1)
    result = []

    queue = deque([1])
    visited[1] = True

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
result = bfs_traversal(n, edges)
print(*result)
