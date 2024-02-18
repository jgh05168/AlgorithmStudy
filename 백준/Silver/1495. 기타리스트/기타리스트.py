'''
1. 가능한 수 list로 만들어두고,
2. 그 수 중 최대 볼륨 dp에 저장
'''

import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [0] * n

tmp_v = set()
tmp_v.add(s)
for i in range(n):
    tmp = set()
    tmp_v = list(tmp_v)
    for j in range(len(tmp_v)):
        if 0 <= tmp_v[j] + v[i] <= m:
            dp[i] = max(dp[i], tmp_v[j] + v[i])
            tmp.add(tmp_v[j] + v[i])
        if 0 <= tmp_v[j] - v[i] <= m:
            dp[i] = max(dp[i], tmp_v[j] - v[i])
            tmp.add(tmp_v[j] - v[i])
    if not len(tmp):
        print(-1)
        exit()
    else:
        tmp_v = tmp

print(dp[-1])