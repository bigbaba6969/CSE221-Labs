import sys
input = sys.stdin.read

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


def main():
    data = input().split()
    n, m = int(data[0]), int(data[1])
    
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        edges.append((w, u, v))
        idx += 3

    edges.sort()
    dsu = DisjointSetUnion(n)
    total_cost = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            total_cost += w

    print(total_cost)

if __name__ == "__main__":
    main()
