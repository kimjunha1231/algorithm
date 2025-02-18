import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.reverse()
down_list = []

count = 1
while n_list:

    if down_list and down_list[-1] == count:
        down_list.pop()
        count += 1
    elif count != n_list[-1]:
        num = n_list.pop()
        down_list.append(num)
    else:
        num = n_list.pop()
        count += 1


while down_list:
    if down_list.pop() == count:
        count += 1
if count - 1 == N:
    print("Nice")
else:
    print("Sad")
