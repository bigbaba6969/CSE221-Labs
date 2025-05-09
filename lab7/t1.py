import sys
import heapq
from collections import defaultdict
 
def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N, M, S, D = map(int, data[idx:idx+4])
    idx += 4
    
    u = list(map(int, data[idx:idx+M]))
    idx += M
    v = list(map(int, data[idx:idx+M]))
    idx += M
    w = list(map(int, data[idx:idx+M]))
    
 
    graph = defaultdict(list)
    for i in range(M):
        graph[u[i]].append((v[i], w[i]))
 
 
    dist = [float('inf')] * (N + 1)
    prev = [None] * (N + 1)
    dist[S] = 0
    heap = [(0, S)]
 
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]: continue
        for nei, cost in graph[node]:
            if dist[node] + cost < dist[nei]:
                dist[nei] = dist[node] + cost
                prev[nei] = node
                heapq.heappush(heap, (dist[nei], nei))
 
 
    if dist[D] == float('inf'):
        print(-1)
    else:
        path = []
        cur = D
        while cur:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        print(dist[D])
        print(*path)
 
if __name__ == "__main__":
    main()