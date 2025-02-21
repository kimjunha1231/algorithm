import sys

N = int(sys.stdin.readline())

x_list = list(map(int, sys.stdin.readline().split()))


set_x = sorted(set(x_list))
dic = {value: idx for idx, value in enumerate(set_x)}
print(" ".join(str(dic[x]) for x in x_list))
