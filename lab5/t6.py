#6
def max_diamonds(R, C, grid):
    visited = [[False for _ in range(C)] for _ in range(R)]

    def dfs_iterative(r, c):
        stack = [(r, c)]
        count = 0

        while stack:
            x, y = stack.pop()
            if x < 0 or x >= R or y < 0 or y >= C:
                continue
            if visited[x][y] or grid[x][y] == '#':
                continue

            visited[x][y] = True
            if grid[x][y] == 'D':
                count += 1


            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

        return count

    max_collected = 0

    for i in range(R):
        for j in range(C):
            if not visited[i][j] and grid[i][j] != '#':
                collected = dfs_iterative(i, j)
                max_collected = max(max_collected, collected)

    print(max_collected)



R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]
max_diamonds(R, C, grid)
