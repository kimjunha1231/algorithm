K = int(input())

result = []
for i in range(K):
    n = int(input())
    if n != 0:
        result.append(n)
    else:
        result.pop()
print(sum(result))
