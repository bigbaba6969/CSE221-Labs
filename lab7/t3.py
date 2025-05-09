import heapq
import sys
input = sys.stdin.read
 
def minimum_danger_levels(N, M, edges):
    graph = [[] for _ in range(N + 1)]
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w)) 
 
    danger = [float('inf')] * (N + 1)
    danger[1] = 0
    pq = [(0, 1)] 
 
    while pq:
        cur_danger, u = heapq.heappop(pq)
        if cur_danger > danger[u]:
            continue
        for v, w in graph[u]:
            new_danger = max(cur_danger, w)
            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(pq, (new_danger, v))
 
 
    result = []
    for i in range(1, N + 1):
        result.append(str(danger[i]) if danger[i] != float('inf') else "-1")
    return result
 
def main():
    data = input().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
 
    edges = []
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
 
    result = minimum_danger_levels(N, M, edges)
    print(' '.join(result))
 
if __name__ == "__main__":
    main()