'''
LIS

1. 정렬
2. 앞순서의 B가 뒷순서의 B보다 최대가 되도록 이어지게 하기
'''

import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    lines.append(tuple(map(int, input().split())))

lines.sort(key=lambda x: x[0])

dp = [1] * n

for i in range(n):
    # 이전에 연결에서 몇 줄이나 연결되어 있는지 확인해보기
    for j in range(i):
        # 만약 한 줄 더 연결할 수 있다면, max로 증가시키기
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# n에서 가장 많이 연결된 전깃줄 개수 빼기
print(n - max(dp))