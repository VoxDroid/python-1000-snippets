# sample2.py
# Minimax AI for Tic-Tac-Toe with a simple evaluation.

import math
from typing import List, Optional


def check_winner(board: List[str]) -> Optional[str]:
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    for a, b, c in lines:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell for cell in board):
        return "draw"
    return None


def minimax(board: List[str], player: str) -> int:
    winner = check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if winner == "draw":
        return 0

    if player == "X":
        best = -math.inf
        for i in range(9):
            if not board[i]:
                board[i] = "X"
                score = minimax(board, "O")
                board[i] = ""
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if not board[i]:
                board[i] = "O"
                score = minimax(board, "X")
                board[i] = ""
                best = min(best, score)
        return best


def best_move(board: List[str], player: str) -> int:
    best_score = -math.inf if player == "X" else math.inf
    best_pos = 0
    for i in range(9):
        if not board[i]:
            board[i] = player
            score = minimax(board, "O" if player == "X" else "X")
            board[i] = ""
            if player == "X" and score > best_score:
                best_score = score
                best_pos = i
            if player == "O" and score < best_score:
                best_score = score
                best_pos = i
    return best_pos


def print_board(board: List[str]) -> None:
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()


def main() -> None:
    board = ["", "", "", "", "", "", "", "", ""]
    current = "X"
    while True:
        pos = best_move(board, current)
        board[pos] = current
        print(f"{current} moves to {pos}")
        print_board(board)
        w = check_winner(board)
        if w:
            print("Result:", w)
            break
        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    main()
