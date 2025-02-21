import sys

n = sys.stdin.readline()
zero = n.strip().split("0")
one = n.strip().split("1")

z = list(filter(lambda x: x != "", zero))
o = list(filter(lambda x: x != "", one))

print(min(len(z), len(o)))
