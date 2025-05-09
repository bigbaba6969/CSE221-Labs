import sys
from collections import defaultdict, deque
import heapq
input = sys.stdin.readline
def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    graph = defaultdict(set)
    in_degree = [0] * 26
    present = [False] * 26
    for word in words:
        for c in word:
            present[ord(c) - ord('a')] = True
    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        found_diff = False
        for j in range(min_len):
            if w1[j] != w2[j]:
                u = ord(w1[j]) - ord('a')
                v = ord(w2[j]) - ord('a')
                if v not in graph[u]:
                    graph[u].add(v)
                    in_degree[v] += 1
                found_diff = True
                break
        if not found_diff and len(w1) > len(w2):
            print(-1)
            return
    heap = []
    for i in range(26):
        if present[i] and in_degree[i] == 0:
            heapq.heappush(heap, i)
    result = []
    while heap:
        u = heapq.heappop(heap)
        result.append(chr(u + ord('a')))
        for v in sorted(graph[u]):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)
    if len(result) != sum(present):
        print(-1)
    else:
        print("".join(result))
main()