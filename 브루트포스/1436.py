import sys

N = int(sys.stdin.readline())
result = 666
count = 0
while count != N:
    if "666" in str(result):
        count += 1
    result += 1
print(result - 1)
