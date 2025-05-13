import sys

input = sys.stdin.readline

N = int(input())

board = [list(input().strip()) for _ in range(N)]


def check(n_list):
    result = 1
    for i in range(N):

        count = 1
        for j in range(1, N):

            if n_list[i][j] == n_list[i][j - 1]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        count = 1
        for j in range(1, N):
            if n_list[j][i] == n_list[j - 1][i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
    return result


result_count = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            result_count = max(result_count, check(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            result_count = max(result_count, check(board))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
print(result_count)
