import sys
from itertools import permutations

N = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))
T = list(map(int, sys.stdin.readline().split()))
oper_list = []
maxs = -float("inf")
mins = float("inf")
for i in range(4):
    if i == 0:
        for _ in range(T[i]):
            oper_list.append("+")
    elif i == 1:
        for _ in range(T[i]):
            oper_list.append("-")
    elif i == 2:
        for _ in range(T[i]):
            oper_list.append("*")
    else:
        for _ in range(T[i]):
            oper_list.append("/")
o_list = set(permutations(oper_list, N - 1))

for oper in o_list:
    result = n_list[0]
    for i in range(len(oper)):
        if oper[i] == "+":
            result += n_list[i + 1]
        elif oper[i] == "-":
            result -= n_list[i + 1]
        elif oper[i] == "*":
            result *= n_list[i + 1]
        else:
            if result < 0:
                result = -(-result // n_list[i + 1])
            else:
                result //= n_list[i + 1]

    maxs = max(maxs, result)
    mins = min(mins, result)


print(maxs)
print(mins)
