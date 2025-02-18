import sys

N, M = map(int, sys.stdin.readline().split())
chess_W = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

chess_B = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]


def check_board(board, x, y):
    count_w, count_b = 0, 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != chess_W[i][j]:
                count_w += 1
            if board[x + i][y + j] != chess_B[i][j]:
                count_b += 1
    return min(count_w, count_b)


def min_paint(board, N, M):
    min_count = float("inf")
    for i in range(N - 7):
        for j in range(M - 7):
            min_count = min(min_count, check_board(board, i, j))
    return min_count


board = [sys.stdin.readline().strip() for _ in range(N)]
print(min_paint(board, N, M))
