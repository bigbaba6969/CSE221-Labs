#5
import sys
sys.setrecursionlimit(10**6)

def has_cycle(n, adj):
    visited = [False] * (n + 1)
    rec_stack = [False] * (n + 1)

    def dfs(v):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in adj[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    for node in range(1, n + 1):
        if not visited[node]:
            if dfs(node):
                return True
    return False



n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)


print("YES" if has_cycle(n, adj) else "NO")
