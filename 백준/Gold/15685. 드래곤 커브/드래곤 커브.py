'''
세가지 속성으로 이루어짐
1. 시작점
2. 시작 방향
3. 세대
    - 다음 세대로 넘어가기 위해서는 끝 점에 같은 세대를 붙인 것이다.
        - 끝 점 : 시작 점에서 선분을 타고 이동했을 떄, 가장 먼 가리에 있는 점
        - k 세대 : k - 1세대를 끝 점 기준 90도 시계방향으로 회전한 뒤 붙인 것

풀이:
구현
정사각형을 이룰 필요는 없다.
네 점이 드래곤커브에 포함만 되어있으면 된다.
- 방향 정보에 대해서만 커브에 넣기
- 방향을 결정할 때는, 커브의 역순으로 탐색을 시작해야 한다.
- 이후, 원점에 대해서 방향만 돌려가면서 업데이트 시키기

-> 방향 정보를 모두 저장했으면, 보드에 하나씩 1로 업데이트하기. (만약 범위 벗어나면 불가능)
'''

import sys
input = sys.stdin.readline

# 조건 0 : 0세대 드래곤 커브 ㅡ
# 조건 1 : n세대 드래곤 커브 = n-1세대 + n-1세대를 90도
# 조건 2-1 : 생성 규칙 : 0세대 : →  1세대 : → ↑ 2세대 : → ↑(여기서부터 역순으로 뒤집기) ← ↑ 3세대 → ↑ ← ↑(여기서부터 역순으로 뒤집기) ← ↓ ← ↑
# 조건 2-2 : 방향 90도 변환 규칙 : ↑ to ← / ← to ↓ /  ↓ to → / → to ↑ (해당위치 % 4)
# 조건 3 : 시작 방향 고려
# 조건 4 : 크기가 1x1이면서 네 꼭지점이 모두 드래곤 커브의 일부인 정사각형의 개수

N = int(input())

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
board = [[0]*101 for _ in range(101)]
for _ in range(N):
    y, x, d, g = map(int, sys.stdin.readline().split())
    board[y][x] = 1 # 시작 위치
    curve = [d] # 조건 3 시작 방향 입력

    for _ in range(g):
        for i in range(len(curve)-1, -1, -1): # 조건 0 ~ 2-1 역순으로 90도 뒤집기 시작해야하니
            curve.append((curve[i]+1) % 4) # 조건 2-2


    for i in range(len(curve)): # 커브 방향 동안
        y, x = y + dy[curve[i]], x + dx[curve[i]]
        board[y][x] = 1

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]: # 조건 4
            result += 1
print(result)
