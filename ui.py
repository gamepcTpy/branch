def print_board(grid):
    for row in grid:
        print("+----" * len(row) + "+")
        print("".join(f"| {num or ' ':4} " for num in row) + "|")
    print("+----" * len(row) + "+")
