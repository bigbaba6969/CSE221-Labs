import sys
input = sys.stdin.read
from heapq import heappush, heappop
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return False
        if self.rank[ru] < self.rank[rv]:
            self.parent[ru] = rv
        else:
            self.parent[rv] = ru
            if self.rank[ru] == self.rank[rv]:
                self.rank[ru] += 1
        return True

def kruskal(n, edges):
    dsu = DSU(n)
    mst = []
    total_cost = 0
    for w, u, v in sorted(edges):
        if dsu.union(u, v):
            mst.append((w, u, v))
            total_cost += w
    return mst, total_cost

def build_graph(n, mst_edges):
    graph = defaultdict(list)
    for w, u, v in mst_edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph

def max_edge_in_path(n, graph):
    max_edge = [[0]*n for _ in range(n)]
    
    def dfs(start, u, parent, max_so_far):
        max_edge[start][u] = max_so_far
        for v, w in graph[u]:
            if v != parent:
                dfs(start, v, u, max(max_so_far, w))

    for u in range(n):
        dfs(u, u, -1, 0)

    return max_edge

def find_second_best_mst(n, edges, mst_edges, mst_cost):
    mst_set = set((min(u, v), max(u, v), w) for w, u, v in mst_edges)
    graph = build_graph(n, mst_edges)
    max_edge = max_edge_in_path(n, graph)
    
    second_best = float('inf')
    for w, u, v in edges:
        if (min(u, v), max(u, v), w) not in mst_set:
            max_w = max_edge[u][v]
            if max_w != w:
                new_cost = mst_cost + w - max_w
                if new_cost > mst_cost:
                    second_best = min(second_best, new_cost)
    return second_best if second_best != float('inf') else -1

def main():
    data = input().split()
    n, m = int(data[0]), int(data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u, v, w = int(data[idx])-1, int(data[idx+1])-1, int(data[idx+2])
        edges.append((w, u, v))
        idx += 3

    mst_edges, mst_cost = kruskal(n, edges)
    if len(mst_edges) != n - 1:
        print(-1)
        return

    result = find_second_best_mst(n, edges, mst_edges, mst_cost)
    print(result)

if __name__ == "__main__":
    main()
