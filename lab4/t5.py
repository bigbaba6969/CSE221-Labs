n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))


indegree = [0] * (n + 1)
outdegree = [0] * (n + 1)


for i in range(m):
    outdegree[u[i]] += 1
    indegree[v[i]] += 1


result = [indegree[i] - outdegree[i] for i in range(1, n + 1)]


print(" ".join(map(str, result)))