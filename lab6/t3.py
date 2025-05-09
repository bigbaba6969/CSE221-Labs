from collections import deque
import sys
input = sys.stdin.readline
def min_knight_moves(n, x1, y1, x2, y2):
    x1-=1
    x2-=1
    y1-=1
    y2-=1
    directions = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    if x1 == x2 and y1 == y2:
        return 0
    visited=[0]*(n*n)
    def index(x, y):
        return x * n + y
    Q=deque()
    Q.append((x1,y1,0))
    visited[index(x1,y1)]=1
    while Q:
        x,y,d=Q.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                idx=index(nx,ny)
                if not visited[idx]:
                    if nx==x2 and ny==y2:
                        return d+1
                    visited[idx]=1
                    Q.append((nx,ny,d+1))
    return -1

if __name__ == "__main__":
    n = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    print(min_knight_moves(n, x1, y1, x2, y2))