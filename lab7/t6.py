import heapq
 
def second_shortest_path(n, m, s, d, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w)) 
    INF = float('inf')
    dist = [[INF, INF] for _ in range(n + 1)]
    dist[s][0] = 0
 
   
    heap = [(0, s)]
 
    while heap:
        cost, u = heapq.heappop(heap)
        for v, w in graph[u]:
            new_cost = cost + w
            if new_cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = new_cost
                heapq.heappush(heap, (new_cost, v))
            elif dist[v][0] < new_cost < dist[v][1]:
                dist[v][1] = new_cost
                heapq.heappush(heap, (new_cost, v))
 
    return dist[d][1] if dist[d][1] != INF else -1
 
 
if __name__ == "__main__":
    n, m, s, d = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = second_shortest_path(n, m, s, d, edges)
    print(result)