import heapq
import sys
input = sys.stdin.read
 
def dijkstra(start, graph, N):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist
 
def main():
    data = input().split()
    idx = 0
 
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
 
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        graph[u].append((v, w))
 
    dist_from_S = dijkstra(S, graph, N)
    dist_from_T = dijkstra(T, graph, N)
 
    min_time = float('inf')
    meeting_point = -1
 
    for i in range(1, N + 1):
        max_time = max(dist_from_S[i], dist_from_T[i])
        if max_time < min_time:
            min_time = max_time
            meeting_point = i
        elif max_time == min_time and i < meeting_point:
            meeting_point = i
 
    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time, meeting_point)
 
if __name__ == "__main__":
    main()