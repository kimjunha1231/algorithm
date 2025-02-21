import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
n_list = list(sys.stdin.readline().strip().split())
mo_list = ["a", "e", "i", "o", "u"]
one_list = []
two_list = []
for n in n_list:
    if n not in mo_list:
        two_list.append(n)
    else:
        one_list.append(n)
answer = []
for i in range(1, min(len(one_list), L - 2) + 1):
    one_com = list(combinations(one_list, i))
    two_com = list(combinations(two_list, L - i))

    for one in one_com:
        for two in two_com:
            result = one + two
            answer.append("".join(map(str, sorted(result))))
print("\n".join(sorted(answer)))
