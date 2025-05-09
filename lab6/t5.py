import sys
from collections import deque
input = sys.stdin.readline
def bfs(start, adj, n):
    visited = [-1] * (n + 1)
    visited[start] = 0
    Q = deque([start])
    far= start
    while Q:
        node=Q.popleft()
        for cur in adj[node]:
            if visited[cur]==-1:
                visited[cur]=visited[node]+1
                Q.append(cur)
                if visited[cur]>visited[far]:
                    far=cur
    return far, visited[far], visited
def main():
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    A, _, _ = bfs(1, adj, n)
    B, length, _ = bfs(A, adj, n)
    print(length)
    print(A, B)
main()