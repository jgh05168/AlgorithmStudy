'''
1. 일단 첫번째 문자를 찾는다.
2. DFS 탐색하며 가능한 모든 경우를 저장
    -> 문자열의 순서도 같이 넘겨준다. (비교를 위해)
- 반드시 한 칸 이상 이동
- 같은 자리에 있을 수 없음
- 여러번 이동할 수 있다.
- 문자열이 완성되는 경우에 cnt++

----------- 시간초과 해결법 -------------
dp + dfs 진행
현재 칸에서 몇 개의 단어를 만들 수 있는지에 대해 저장한다
dp[x][y][idx] : (x, y) 좌표에서 string의 몇 번 째 인덱스일 때 단어를 몇 개 만들 수 있는지

- 설명이 잘 되있어서 ... 
    https://yabmoons.tistory.com/194
'''

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(row, col, idx):
    global cnt
    if idx == len(target_str):
        return 1

    if dp[row][col][idx] != -1:
        return dp[row][col][idx]

    dp[row][col][idx] = 0       # 해당 좌표에 있는 값을 특정 인덱스 번호로 설정했을 때, 나올 수 있는 경우의 수
    for i in range(4):
        temp_x, temp_y = row, col
        for _ in range(k):
            nrow = temp_x + dr[i]
            ncol = temp_y + dc[i]
            if 0 <= nrow < n and 0 <= ncol < m:
                if grid[nrow][ncol] == target_str[idx]:
                    dp[row][col][idx] += dfs(nrow, ncol, idx + 1)
            temp_x, temp_y = nrow, ncol
    return dp[row][col][idx]

n, m, k = map(int, input().split())
grid = [list(input()) for _ in range(n)]
target_str = input().rstrip()
cnt = 0

dp = [[[-1] * len(target_str) for _ in range(m)] for _ in range(n)]
start_list = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == target_str[0]:
            start_list.append((i, j))

for sr, sc in start_list:
    cnt += dfs(sr, sc, 1)   # (row, col, 문자열 인덱스)

print(cnt)