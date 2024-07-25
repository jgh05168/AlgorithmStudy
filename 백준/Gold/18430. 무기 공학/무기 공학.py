'''
나무 재료의 부위마다 강도가 다름
부메랑은 ㄱ 모양
중심이 되는 칸은 강도의 영향을 2배로 받음

- 여러 개의 부메랑을 만들 수 있음
- 시작 지점의 강도는 2배로 계산

백트랙킹, 완탐
풀이 :
selected 배열을 2차원으로 만든다.
선택, 만들기, 돌리기 과정이 진행되어야 함
5 x 5라서 백트랙킹이 충분히 가능함
    -> 더이상 부메랑을 만들 수 없을 때 값 업데이트 하기
'''

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(sr, sc, val):
    global ans
    for r in range(sr, n):
        if r != sr:     # 해당 row 일 때는 들어온 col보다 작은 값 보지 않기
            sc = 0
        for c in range(sc, m):
            if not selected[r][c]:
                # 부메랑 네 방향에 걸쳐서 만들어보기
                for d in range(len(dr)):
                    nr1, nc1 = r + dr[(d + 1) % 4], c + dc[(d + 1) % 4]
                    nr2, nc2 = r + dr[(d + 2) % 4], c + dc[(d + 2) % 4]
                    if 0 <= nr1 < n and 0 <= nr2 < n and 0 <= nc1 < m and 0 <= nc2 < m:
                        if not selected[nr1][nc1] and not selected[nr2][nc2]:
                            selected[nr1][nc1], selected[nr2][nc2], selected[r][c] = 1, 1, 1
                            dfs(r, c, val + grid[r][c] * 2 + grid[nr1][nc1] + grid[nr2][nc2])
                            selected[nr1][nc1], selected[nr2][nc2], selected[r][c] = 0, 0, 0
            ans = max(ans, val)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
selected = [[0] * m for _ in range(n)]

ans = 0
dfs(0, 0, 0)

print(ans)