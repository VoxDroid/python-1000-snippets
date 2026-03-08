# sample2.py
# demonstrate oscillators and still lifes

def game_of_life(board, steps):
    def count_neighbors(board, i, j):
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    count += board[ni][nj]
        return count

    for _ in range(steps):
        new_board = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = count_neighbors(board, i, j)
                if board[i][j] == 1 and neighbors in [2, 3]:
                    new_board[i][j] = 1
                elif board[i][j] == 0 and neighbors == 3:
                    new_board[i][j] = 1
        board = new_board
    return board

if __name__ == '__main__':
    blinker = [[0,1,0],[0,1,0],[0,1,0]]
    print('blinker', game_of_life(blinker,1))
    block = [[1,1],[1,1]]
    print('block', game_of_life(block,3))
