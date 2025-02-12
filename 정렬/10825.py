import sys

N = int(sys.stdin.readline())

# def sorted_item():

dicts = []
for i in range(N):
    data = sys.stdin.readline().split()
    dicts.append([data[0], int(data[1]), int(data[2]), int(data[3])])

sort_item = sorted(dicts, key=lambda x: (-x[1], x[2], -x[3], x[0]))


for student in sort_item:
    print(student[0])
