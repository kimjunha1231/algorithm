import sys

S, E, Q = sys.stdin.readline().strip().split()


def minutes(time):
    h, m = list(map(int, time.split(":")))
    return h * 60 + m


stime = minutes(S)
etime = minutes(E)
qtime = minutes(Q)

attend_list = set()
count = 0
for i in sys.stdin:

    times, nickname = i.strip().split()
    in_time = minutes(times)
    if in_time <= stime:
        attend_list.add(nickname)
    elif in_time >= etime and in_time <= qtime and nickname in attend_list:
        attend_list.remove(nickname)
        count += 1

print(count)
