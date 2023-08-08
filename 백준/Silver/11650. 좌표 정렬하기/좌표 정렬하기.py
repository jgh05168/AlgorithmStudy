import sys

input = sys.stdin.readline

N = int(input())

locs = []
for _ in range(N):
    x, y = map(int, input().split())
    locs.append((x, y))

locs.sort()
for i in range(len(locs)):
    print(*locs[i])