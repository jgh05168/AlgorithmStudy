'''
도로 길이를 순회하면서 현재 운전거리의 최솟값을 메모이제이션한다.
지름길을 지나지 않는 것이 거리가 더 짧을 수 있다.
현재 위치가 지름길 도착 위치와 같다면 지름길을 지나서 온 거리와 현재 값 중 작은 것을 선택한다.
'''

import sys
input = sys.stdin.readline

n, d = map(int, input().split())
short_road = [tuple(map(int, input().split())) for _ in range(n)]

dp = [1e9] * (d + 1)
dp[0] = 0
for i in range(1, d + 1):
    dp[i] = dp[i - 1] + 1
    for start, end, length in short_road:
        if i == end: #
            dp[i] = min(dp[i], dp[start] + length)

print(dp[d])