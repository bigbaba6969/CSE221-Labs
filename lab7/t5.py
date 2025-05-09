import sys
import heapq
from collections import defaultdict
 
def shortest_parity_path(n, m, u, v, w):
    graph = defaultdict(list)
    for i in range(m):
        graph[u[i]].append((v[i], w[i]))
 
    
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[1][0] = dist[1][1] = 0
 
    
    heap = [(0, 1, -1)] 
    while heap:
        d, node, last_parity = heapq.heappop(heap)
 
        for neighbor, weight in graph[node]:
            parity = weight % 2
            if parity == last_parity:
                continue  
 
            if d + weight < dist[neighbor][parity]:
                dist[neighbor][parity] = d + weight
                heapq.heappush(heap, (d + weight, neighbor, parity))
 
    res = min(dist[n][0], dist[n][1])
    return res if res != float('inf') else -1
 

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
 
    u = list(map(int, data[idx:idx + m]))
    idx += m
    v = list(map(int, data[idx:idx + m]))
    idx += m
    w = list(map(int, data[idx:idx + m]))
    
    result = shortest_parity_path(n, m, u, v, w)
    print(result)
 
if __name__ == "__main__":
    main()