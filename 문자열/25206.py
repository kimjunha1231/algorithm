import sys

result_m = 0
result_score = 0
for i in sys.stdin:
    name, m, score = i.split()
    m = float(m)
    if score != "P":
        result_m += m
    if score == "A+":
        result_score += 4.5 * m
    elif score == "A0":
        result_score += 4.0 * m
    elif score == "B+":
        result_score += 3.5 * m
    elif score == "B0":
        result_score += 3.0 * m
    elif score == "C+":
        result_score += 2.5 * m
    elif score == "C0":
        result_score += 2.0 * m
    elif score == "D+":
        result_score += 1.5 * m
    elif score == "D0":
        result_score += 1.0 * m

if result_m == 0:
    print(0)
else:

    print(result_score / result_m)
