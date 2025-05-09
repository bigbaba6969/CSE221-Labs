import sys
import heapq
input = sys.stdin.read
 
def min_cost_path(N, M, S, D, weights, edges):
    graph = [[] for _ in range(N + 1)]
    for u, v in edges:
        graph[u].append(v)  
 
    dist = [float('inf')] * (N + 1)
    dist[S] = weights[S - 1]
 
    pq = [(dist[S], S)] 
 
    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u]:
            continue
        for v in graph[u]:
            new_cost = cost + weights[v - 1]
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
 
    return dist[D] if dist[D] != float('inf') else -1
 
def main():
    data = input().split()
    idx = 0
 
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    D = int(data[idx]); idx += 1
 
    weights = [int(data[idx + i]) for i in range(N)]
    idx += N
 
    edges = []
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        edges.append((u, v))
 
    result = min_cost_path(N, M, S, D, weights, edges)
    print(result)
 
if __name__ == "__main__":
    main()