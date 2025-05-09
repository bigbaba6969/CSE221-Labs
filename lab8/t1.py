import sys

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return self.size[root_x]

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return self.size[root_x]

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    dsu = DisjointSetUnion(N)

    idx = 2
    for _ in range(K):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        print(dsu.union(a, b))

if __name__ == "__main__":
    main()
