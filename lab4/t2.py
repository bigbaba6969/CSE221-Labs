N, M = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
w_list = list(map(int, input().split()))

adj_list = {i: [] for i in range(1, N+1)}

for i in range(M):
    u = list1[i]
    v = list2[i]
    w = w_list[i]
    adj_list[u].append((v, w))

for i in range(1, N+1):
    neighbors = ' '.join(f'({v},{w})' for v, w in adj_list[i])
    print(f"{i}: {neighbors}")