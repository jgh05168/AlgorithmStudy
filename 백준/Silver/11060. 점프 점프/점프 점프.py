'''
bfs + dp

dp에 비교해서 작은 값 저장
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
maze = list(map(int, input().split()))

dp = [int(1e9)] * n
queue = deque()
queue.append(0)
dp[0] = 0

while queue:
    u = queue.popleft()

    tmp_val = maze[u]
    while tmp_val > 0:
        if u + tmp_val < n and dp[u + tmp_val] == int(1e9):
            dp[u + tmp_val] = min(dp[u + tmp_val], dp[u] + 1)
            queue.append(u + tmp_val)
            if u + tmp_val == n - 1:
                break
        tmp_val -= 1
if dp[-1] == int(1e9):
    print(-1)
else:
    print(dp[-1])
