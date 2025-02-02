N = int(input())

n_list = set(input().split())

M = int(input())
result = []
m_list = input().split()

for i in m_list:
    if i in n_list:
        result.append(1)
    else:
        result.append(0)


print("\n".join(map(str, result)))
