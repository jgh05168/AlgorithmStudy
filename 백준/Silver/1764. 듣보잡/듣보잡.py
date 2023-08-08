import sys

input = sys.stdin.readline

N, M = map(int, input().split())

x_heard = []
x_seen = []
for i in range(N + M):
    if i < N:
        name = input()
        x_heard.append(name[:-1])
    else:
        name = input()
        x_seen.append(name[:-1])



x_heard_seen = list(set(x_seen).intersection(set(x_heard)))

x_heard_seen.sort()
print(len(x_heard_seen))
for person in x_heard_seen:
    print(person)