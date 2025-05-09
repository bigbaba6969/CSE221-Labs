#4
from collections import deque, defaultdict

def bfs(start, end, graph, n):
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    dist = [float('inf')] * (n + 1)

    queue = deque([start])
    visited[start] = True
    dist[start] = 0

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    if not visited[end]:
        return -1, []


    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return dist[end], path

def shortest_path_with_k(n, m, s, d, k, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    if s == k or k == d:
        dist, path = bfs(s, d, graph, n)
        if dist != -1:
            return dist, path
        else:
            return -1

    dist1, path1 = bfs(s, k, graph, n)
    if dist1 == -1:
        return -1

    dist2, path2 = bfs(k, d, graph, n)
    if dist2 == -1:
        return -1

    full_path = path1 + path2[1:]
    return dist1 + dist2, full_path


def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().split('\n')

    n, m, s, d, k = map(int, lines[0].split())
    edges = [tuple(map(int, line.split())) for line in lines[1:]]

    result = shortest_path_with_k(n, m, s, d, k, edges)

    if result == -1:
        print(-1)
    else:
        length, path = result
        print(length)
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()