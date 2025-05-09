import sys
from collections import deque
input = sys.stdin.readline
N, R = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
subtree = [0] * (N + 1)
parent = [0] * (N + 1)
stack = [R]
order = []
while stack:
    node=stack.pop()
    order.append(node)
    for cur in adj[node]:
        if cur!=parent[node]:
            parent[cur]=node
            stack.append(cur)
for node in reversed(order):
    subtree[node]=1
    for cur in adj[node]:
        if cur!=parent[node]:
            subtree[node]+=subtree[cur]
Q = int(input())
output = []
for _ in range(Q):
    X = int(input())
    output.append(str(subtree[X]))
print("\n".join(output))