T = int(input())
result = []
result_list = []
for i in range(T):
    a = input()
    a_list = a.split()
    if a_list[0] == "push":
        result_list.append(a_list[1])
    elif a_list[0] == "top":
        if len(result_list) == 0:
            result.append(-1)
            continue
        result.append(result_list[-1])
    elif a_list[0] == "size":
        result.append(len(result_list))
    elif a_list[0] == "empty":
        if len(result_list) == 0:
            result.append(1)
            continue
        result.append(0)
    else:
        if len(result_list) == 0:
            result.append(-1)
            continue
        result.append(result_list.pop())
for j in result:
    print(j)
