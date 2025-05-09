import sys
import math
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0

    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1


    neighbors = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and math.gcd(i, j) == 1:
                neighbors[i].append(j)
        neighbors[i].sort()

    results = []

    for _ in range(Q):
        X = int(data[idx])
        idx += 1
        K = int(data[idx])
        idx += 1

        if K <= len(neighbors[X]):
            results.append(str(neighbors[X][K - 1]))
        else:
            results.append('-1')

    print('\n'.join(results))

if __name__ == "__main__":
    main()