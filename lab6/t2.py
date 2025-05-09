from collections import defaultdict, deque
def robot_or_human(n, m, tackles):
    graph=defaultdict(list)
    for u,v in tackles:
        graph[u].append(v)
        graph[v].append(u)
    visited=[False]*(n+1)
    color=[-1]*(n+1)
    def bfs(start):
        Q=deque([start])
        visited[start]=True
        color[start]=0
        count=[1,0]
        while Q:
            node=Q.popleft()
            for cur in graph[node]:
                if not visited[cur]:
                    visited[cur]=True
                    color[cur]=1-color[node]
                    count[color[cur]]+=1
                    Q.append(cur)
                elif color[cur]==color[node]:
                    return 0
        return max(count)
    result=0
    for i in range(1,n+1):
        if not visited[i]:
            result+=bfs(i)
    return result
if __name__ == "__main__":
    n, m = map(int, input().split())
    tackles = [tuple(map(int, input().split())) for _ in range(m)]
    print(robot_or_human(n, m, tackles))