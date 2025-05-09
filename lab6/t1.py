from collections import defaultdict, deque
import sys

def topological_sort(n, prerequisites):
    graph=defaultdict(list)
    indegree= [0]*(n+1)
    for a,b in prerequisites:
        graph[a].append(b)
        indegree[b]+=1
    Q=deque([i for i in range(1,n+1) if indegree[i]==0])
    result=[]
    while Q:
        cur=Q.popleft()
        result.append(cur)
        for i in graph[cur]:
            indegree[i]-=1
            if indegree[i]==0:
                Q.append(i)
    if len(result)==n:
        return result
    else:
        return [-1]
if __name__ == "__main__":
    n, m = map(int, input().split())
    prerequisites = [tuple(map(int, input().split())) for _ in range(m)]
    order = topological_sort(n, prerequisites)
    print(" ".join(map(str, order)))