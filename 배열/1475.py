import sys

N = list(sys.stdin.readline().strip())
T = set(N)
sets = 0
counts = 0
for i in T:

    if i == "6" or i == "9":

        counts = (
            (N.count("6") + N.count("9")) // 2
            if (N.count("6") + N.count("9")) % 2 == 0
            else (N.count("6") + N.count("9")) // 2 + 1
        )
    elif sets < N.count(i):
        counts = N.count(i)

    sets = max(sets, counts)
sys.stdout.write(str(sets))
