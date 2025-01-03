def solve_chessboard_repainting(n, m, board):
    chessboard1 = ["WBWBWBWB", "BWBWBWBW"] * 4
    chessboard2 = ["BWBWBWBW", "WBWBWBWB"] * 4

    def count_repaints(x, y, pattern):
        return sum(
            board[x + i][y + j] != pattern[i][j]
            for i in range(8) for j in range(8)
        )

    return min(
        min(count_repaints(i, j, chessboard1), count_repaints(i, j, chessboard2))
        for i in range(n - 7) for j in range(m - 7)
    )

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

print(solve_chessboard_repainting(n, m, board))
