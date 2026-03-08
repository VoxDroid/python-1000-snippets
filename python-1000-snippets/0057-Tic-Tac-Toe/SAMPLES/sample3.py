# sample3.py
# Play game reading moves (row col) from stdin until end or win

import sys

def print_board(board):
    for r in board:
        print('|'.join(r))
        print('-----')

def check_win(board, p):
    for i in range(3):
        if all(board[i][j]==p for j in range(3)) or all(board[j][i]==p for j in range(3)):
            return True
    if all(board[i][i]==p for i in range(3)) or all(board[i][2-i]==p for i in range(3)):
        return True
    return False

if __name__ == '__main__':
    board=[[' ']*3 for _ in range(3)]
    player='X'
    for line in sys.stdin:
        parts=line.split()
        if len(parts)<2: continue
        r=int(parts[0]); c=int(parts[1])
        if board[r][c] != ' ':
            continue
        board[r][c]=player
        print_board(board)
        if check_win(board, player):
            print(player,'wins')
            break
        player='O' if player=='X' else 'X'
    else:
        print('game over')
