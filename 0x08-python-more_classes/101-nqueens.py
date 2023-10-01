#!/usr/bin/python3
"""The N-queens puzzle"""

import sys


def init_board(n):
    """Inits an `N`x`N` sized chessboard with 0's."""
    board = []
    [board.append([]) for y in range(n)]
    [row.append(' ') for y in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Returns a Chessboard deepcopy"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists in a board."""
    sol = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                sol.append([row, col])
                break
    return (sol)


def xout(board, row, col):
    """Returns X spots on a chessboard"""

    for cl in range(col + 1, len(board)):
        board[row][cl] = "x"

    for cl in range(col - 1, -1, -1):
        board[row][cl] = "x"

    for rw in range(row + 1, len(board)):
        board[rw][col] = "x"

    for rw in range(row - 1, -1, -1):
        board[rw][col] = "x"

    cl = col + 1
    for rw in range(row + 1, len(board)):
        if cl >= len(board):
            break
        board[rw][cl] = "x"
        cl += 1

    cl = col - 1
    for rw in range(row - 1, -1, -1):
        if cl < 0:
            break
        board[rw][cl]
        cl -= 1

    cl = col + 1
    for rw in range(row - 1, -1, -1):
        if cl >= len(board):
            break
        board[rw][cl] = "x"
        cl += 1

    cl = col - 1
    for rw in range(row + 1, len(board)):
        if cl < 0:
            break
        board[rw][cl] = "x"
        cl -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle"""
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for cl in range(len(board)):
        if board[row][cl] == " ":
            temp_board = board_deepcopy(board)
            temp_board[row][cl] = "Q"
            xout(temp_board, row, cl)
            solutions = recursive_solve(temp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for soln in solutions:
        print(soln)
