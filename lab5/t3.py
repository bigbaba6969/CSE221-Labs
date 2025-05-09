from collections import defaultdict, deque

def lexicographically_smallest_bfs_path(N,M,S,D, u_list, v_list):
    graph = defaultdict(list)

    for i in range(M):
        u = u_list[i]
        v = v_list[i]
        graph[u].append(v)
        graph[v].append(u)

    for node in graph:
        graph[node].sort()

    visited = [False] * (N + 1)
    parent = [0] * (N + 1)

    queue = deque([S])
    visited[S] = True

    while queue:
        current = queue.popleft()
        if current == D:
            break
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)


    if not visited[D]:
        print(-1)
    else:
        path = []
        node = D
        while node:
            path.append(node)
            node = parent[node]
        path.reverse()
        print(len(path) - 1)
        print(*path)


N,M,S,D = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
lexicographically_smallest_bfs_path(N,M,S,D, u_list, v_list)