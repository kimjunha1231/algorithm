import sys

input = sys.stdin.readline

S, P = map(int, input().split())

Dna = input().strip()

A, C, G, T = map(int, input().split())
count = 0

current = [0, 0, 0, 0]

for i in range(P):
    if Dna[i] == "A":
        current[0] += 1
    elif Dna[i] == "C":
        current[1] += 1
    elif Dna[i] == "G":
        current[2] += 1
    elif Dna[i] == "T":
        current[3] += 1
if current[0] >= A and current[1] >= C and current[2] >= G and current[3] >= T:
    count += 1

for i in range(P, S):
    if Dna[i] == "A":
        current[0] += 1
    elif Dna[i] == "C":
        current[1] += 1
    elif Dna[i] == "G":
        current[2] += 1
    elif Dna[i] == "T":
        current[3] += 1

    if Dna[i - P] == "A":
        current[0] -= 1
    elif Dna[i - P] == "C":
        current[1] -= 1
    elif Dna[i - P] == "G":
        current[2] -= 1
    elif Dna[i - P] == "T":
        current[3] -= 1

    if current[0] >= A and current[1] >= C and current[2] >= G and current[3] >= T:
        count += 1

print(count)
