import sys

N = int(sys.stdin.readline())

route_list = list(map(int, sys.stdin.readline().split()))
price_list = list(map(int, sys.stdin.readline().split()))
count = 0
for i in range(len(price_list) - 1):

    if i == (len(price_list) - 2):
        count += price_list[i] * route_list[i]
        break
    for j in range(i + 1, len(price_list) - 1):
        if price_list[i] > price_list[j]:
            count += price_list[i] * route_list[j - 1]
            break
        else:
            count += price_list[i] * route_list[i]
            price_list[j] = price_list[i]
            break


print(count)
