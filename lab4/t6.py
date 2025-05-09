N = int(input())
x, y = map(int, input().split())


directions = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, -1), (-1, 1),
    (1, -1), (1, 1)
]


def insert_sorted(moves, move):
    for i in range(len(moves)):
        if move[0] < moves[i][0] or (move[0] == moves[i][0] and move[1] < moves[i][1]):
            moves.insert(i, move)
            return
    moves.append(move)

valid_moves = []
for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if 1 <= nx <= N and 1 <= ny <= N:
        insert_sorted(valid_moves, (nx, ny))

print(len(valid_moves))
for i, j in valid_moves:
    print(i, j)