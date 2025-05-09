def adjacency_list_to_matrix():
    N = int(input())

    matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        line = list(map(int, input().split()))
        k = line[0]
        neighbors = line[1:]
        for neighbor in neighbors:
            matrix[i][neighbor] = 1


    for row in matrix:
        print(' '.join(map(str, row)))


adjacency_list_to_matrix()