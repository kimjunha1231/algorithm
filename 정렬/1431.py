import sys
import re

N = int(sys.stdin.readline())

lists = []
for _ in range(N):

    lists.append(sys.stdin.readline().strip())


lists_sum = []


def sum_digits(s):
    numbers = re.findall(r"\d", s)
    return sum(map(int, numbers))


sorted_lists = sorted(lists, key=lambda x: (len(x), sum_digits(x), x))

print("\n".join(sorted_lists))
