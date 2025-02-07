import sys

J = int(sys.stdin.readline())

A = int(sys.stdin.readline())

list = []
count = 0
for i in range(J):
    k = sys.stdin.readline().strip()
    if k == "S":
        k = 0
    elif k == "M":
        k = 1
    else:
        k = 2
    list.append(k)


for a in range(A):
    size, num = sys.stdin.readline().split()
    if size == "S":
        size = 0
    elif size == "M":
        size = 1
    else:
        size = 2
    if list[int(num) - 1] >= size:
        list[int(num) - 1] = -1
        count += 1
print(count)
