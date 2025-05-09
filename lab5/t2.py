import sys
sys.setrecursionlimit(2 * 10**5 + 10)

from collections import defaultdict

def dfs(node, graph, visited, result):
    visited[node] = True
    result.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, result)

def solve_dfs(n, m, u_list, v_list):
    graph = defaultdict(list)


    for u, v in zip(u_list, v_list):
        graph[u].append(v)
        graph[v].append(u)


    for key in graph:
        graph[key].sort()

    visited = [False] * (n + 1)
    result = []

    dfs(1, graph, visited, result)
    return result


n, m = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

result = solve_dfs(n, m, u_list, v_list)
print(*result)