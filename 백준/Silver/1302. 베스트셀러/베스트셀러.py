import sys, heapq
input = sys.stdin.readline

n = int(input())
tmp_dict = {}

for _ in range(n):
    book = input().rstrip()
    if book in tmp_dict.keys():
        tmp_dict[book] += 1
    else:
        tmp_dict.update({book: 1})

ans = []
for key, value in tmp_dict.items():
    heapq.heappush(ans, (-value, key))

print(heapq.heappop(ans)[1])