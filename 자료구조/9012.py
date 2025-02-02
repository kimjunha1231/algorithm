import sys

T = int(input())
result = []
is_true = True
for i in range(T):
    x = input()

    count = 0
    for j in x:
        if count == -1:
            is_true = False
            break
        if j == "(":
            count += 1
        else:
            count -= 1
    if count != 0:
        is_true = False
    else:
        is_true = True
    if is_true:
        result.append("YES")
    else:
        result.append("NO")
    count = 0
for k in result:
    print(k)
