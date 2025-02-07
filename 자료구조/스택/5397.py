import sys
from collections import deque


input = sys.stdin.readline
T = int(input())


for _ in range(T):
    left_list = []
    right_list = []

    for n in input().strip():
        if n == "<":
            if left_list:
                right_list.append(left_list.pop())
        elif n == ">":
            if right_list:
                left_list.append(right_list.pop())
        elif n == "-":
            if left_list:
                left_list.pop()
        else:
            left_list.append(n)
    left_list.extend(reversed(right_list))
    print("".join(left_list))
