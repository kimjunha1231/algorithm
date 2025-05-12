import sys
from operator import itemgetter


input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())
    count = 1
    n_list = list(list(map(int, input().split())) for _ in range(N))
    sort_n_list = sorted(n_list, key=itemgetter(0))
    min_ranking = sort_n_list[0][1]
    for i in range(1, N):
        if sort_n_list[i][1] < min_ranking:
            min_ranking = sort_n_list[i][1]
            count += 1

    print(count)
