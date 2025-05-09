N, M = map(int, input().split())
adj_matrix= [[0] * N for i in range(N)]
for i in range(M):
    a,b,c = map(int, input().split())
    adj_matrix[a - 1][b - 1] = c


for row in adj_matrix:
    print(' '.join(map(str, row)))