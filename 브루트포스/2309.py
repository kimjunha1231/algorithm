import sys

n_list = []
for i in range(9):
    n_list.append(int(sys.stdin.readline()))
count = 0
result = sum(n_list) - 100

for i in range(9):
    for j in range(i + 1, 9):

        if n_list[i] + n_list[j] == result:

            n_list.pop(j)
            n_list.pop(i)
            print("\n".join(map(str, sorted(n_list))))
            sys.exit(0)
