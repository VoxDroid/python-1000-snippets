# sample1.py
# Pre-scripted moves where X wins quickly

def play(moves):
    board = [[' ']*3 for _ in range(3)]
    def print_board():
        for r in board:
            print('|'.join(r))
            print('-----')
    def check_win(p):
        for i in range(3):
            if all(board[i][j]==p for j in range(3)) or all(board[j][i]==p for j in range(3)):
                return True
        if all(board[i][i]==p for i in range(3)) or all(board[i][2-i]==p for i in range(3)):
            return True
        return False
    player='X'
    for r,c in moves:
        board[r][c] = player
        if check_win(player):
            print_board()
            print(player,'wins!')
            return
        player = 'O' if player=='X' else 'X'
    print_board()
    print('draw')

if __name__ == '__main__':
    # moves: X at (0,0), O at (1,0), X at (0,1), O at (1,1), X at (0,2)
    play([(0,0),(1,0),(0,1),(1,1),(0,2)])
