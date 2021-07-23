

def print_board(board):
    """
    The functions prints the board it is given
    Args:
        board(2-D List): The bpard to be printed
    Returns:
        (None): Function doesn't return a value
    """
    for rows in range(len(board)):
        for cols in  range(len(board[rows])):
            print(str(board[rows][cols])+ "  ",end='')
        print("\n")

