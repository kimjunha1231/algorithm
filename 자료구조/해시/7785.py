import sys

n = int(sys.stdin.readline())
result = set()
for _ in range(n):
    person, entered = sys.stdin.readline().split()
    if entered == "enter":
        result.add(person)
    else:
        if person in result:
            result.remove(person)
print("\n".join(sorted(result, reverse=True)))
