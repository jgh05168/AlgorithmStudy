'''
2 x n
지뢰는 둘째 줄에만 있다.
모든 지뢰의 개수를 찾자

풀이:
1. 지뢰 확률이 높은 순서대로 정렬
2. 높은 확률 순서대로 순회하며 지뢰 찾기
    - 숫자는 0 ~ 3까지만 나올 수 있음
- 양 끝은 0 ~ 2만 가능하다.
    - 우선체크해서 2인 경우, 지뢰 2개 미리 심어주기
---------------- 틀렸습니다 -------------------
 순차적으로 밀어가면서 생각하기
- 1번 ~ n번 인덱스까지 확인해가며
인접한 곳에 지뢰가 있다면 pass, 아니라면 지뢰 하나 놓고 이어가기
'''

import sys
input = sys.stdin.readline

dr = 1
dc = [-1, 0, 1]


t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    grid.append(list(int(i) for i in input().rstrip()))
    grid.append(list(input().rstrip()))
    ans = 0

    # 1. 이미 있는 지뢰의 경우의 수 제거해주기
    for i in range(n):
        if grid[1][i] == '*':
            grid[0][i] -= 1
            ans += 1
            if i + 1 < n:
                grid[0][i + 1] -= 1
            if i - 1 >= 0:
                grid[0][i - 1] -= 1

    ### 범위가 다르기 때문에 나눠서 체크해준다.

    # 2. 첫번째 부분 먼저 체크해주기
    if grid[1][0] == '#' and grid[0][0] and grid[0][1]:
        ans += 1
        grid[0][0] -= 1
        grid[0][1] -= 1
        grid[1][0] = '*'

    # 3. 마지막 부분 제외한 나머지 부분 순회하며 체크해주기
    for i in range(1, n - 1):
        if grid[1][i] == '#':
            # 만약 세 부분 모두 지뢰를 놓을 수 있다면 (아직 지뢰 체크가 되지 않았다면) 지뢰로 체크하기
            if grid[0][i - 1] and grid[0][i] and grid[0][i + 1]:
                grid[0][i - 1] -= 1
                grid[0][i] -= 1
                grid[0][i + 1] -= 1
                ans += 1
                grid[1][i] = '*'

    # 4. 맨 마지막 부분 체크해주기
    if grid[1][-1] == '#' and grid[0][-1] and grid[0][-2]:
        ans += 1
        grid[0][-1] -= 1
        grid[0][-2] -= 1
        grid[1][-1] = '*'

    print(ans)