def move(board, direction):
    def slide(row):
        new_row = [i for i in row if i != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [i for i in new_row if i != 0]
        return new_row + [0] * (len(row) - len(new_row))

    for i in range(board.size):
        if direction == 'w':
            col = [board.grid[r][i] for r in range(board.size)]
            col = slide(col)
            for r in range(board.size):
                board.grid[r][i] = col[r]
        elif direction == 's':
            col = [board.grid[r][i] for r in range(board.size)][::-1]
            col = slide(col)
            for r in range(board.size):
                board.grid[r][i] = col[::-1][r]
        elif direction == 'a':
            board.grid[i] = slide(board.grid[i])
        elif direction == 'd':
            board.grid[i] = slide(board.grid[i][::-1])
            board.grid[i].reverse()
