N, M = map(int, input().split())


U = list(map(int, input().split()))
V = list(map(int, input().split()))


degree = [0] * (N + 1)


for i in range(M):
    degree[U[i]] += 1
    degree[V[i]] += 1


odd_count = 0
for d in degree:
    if d % 2 == 1:
        odd_count += 1


if odd_count == 0 or odd_count == 2:
    print("YES")
else:
    print("NO")