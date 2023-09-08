import sys
input = sys.stdin.readline

N, K = map(int, input().split())

money_list = []
for i in range(N):
    money = int(input())
    money_list.append(money)

cnt = 0
total = K
startidx = N

for i in range(startidx - 1, -1, -1):

    if money_list[i] > K:
        continue
    else:
        if total >= money_list[i]:
            cnt += total // money_list[i]
            total %= money_list[i]
    if not total:
        break
print(cnt)