# sample2.py
# Sequence of moves that leads to a draw

def play(moves):
    board = [[' ']*3 for _ in range(3)]
    def check_win(p):
        for i in range(3):
            if all(board[i][j]==p for j in range(3)) or all(board[j][i]==p for j in range(3)):
                return True
        if all(board[i][i]==p for i in range(3)) or all(board[i][2-i]==p for i in range(3)):
            return True
        return False
    player='X'
    for r,c in moves:
        board[r][c]=player
        player='O' if player=='X' else 'X'
    for row in board:
        print('|'.join(row))
        print('-----')
    print('draw')

if __name__ == '__main__':
    play([(0,0),(0,1),(0,2),(1,1),(1,0),(1,2),(2,1),(2,0),(2,2)])
