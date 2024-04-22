'''
스티커 : 상하좌우 모두 연결되있고, 불필요한 행이나 열이 존재하지 않는다.
스티커를 먼저 받았던 것들부터 차례대로 격자에 맞춰 붙이고자 함
1. 스티커를 회전시키지 않고 모눈종이에서 떼어낸다
2. 스티커를 붙일 수 있는 위치를 찾는다.
    2-1. 위쪽의 위치를 먼저 선택.
    2-2. 여러곳이라면 그 중 가장 왼쪽의 위치를 선택
3. 스티커를 붙인다. 만약 스티커를 붙이지 못했다면 시계방향으로 90도 회전한 뒤 위 과정 반복
4. 4번 회전시켜도 스티커를 붙이지 못한다면 버린다.

- 모든 스티커를 붙인 뒤 몇 개의 칸이 채워졌는지 확인해보자.

40 x 40
스티커의 개수 100개

풀이:
- 스티커는 정사각형 모양 배열로 다시 만든다.
- 나머지는 스티커 붙이는 방법 따라가기.

'''

import sys
input = sys.stdin.readline


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def isvalid(sticker, srow, scol):
    for row in range(len(sticker)):
        for col in range(len(sticker[0])):
            if 0 <= row + srow < n and 0 <= col + scol < m:
                # 이미 값이 존재한다면, return 0
                if notebook[row + srow][col + scol] and sticker[row][col]:
                    return 0
            else:
                return 0
    return 1

def check_sticker(sticker):
    #### 범위 설정 주의 ####
    for row in range(n - len(sticker) + 1):
        for col in range(m - len(sticker[0]) + 1):
            if isvalid(sticker, row, col):
                for nrow in range(len(sticker)):
                    for ncol in range(len(sticker[0])):
                        # 이미 있는 값이라면 continue
                        if notebook[row + nrow][col + ncol]:
                            continue
                        notebook[row + nrow][col + ncol] = sticker[nrow][ncol]
                return 1
    return 0


def rotate():
    # 범위는 rotate 될 때마다 재설정해줘야 한다.
    n = len(sticker)
    m = len(sticker[0])
    # tmp_sticker의 모양이 항상 달라진다.
    tmp_sticker = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            # 리스트 자체가 돌아갔기 때문에 tmp_sticker 기준으로 배열을 작성해주어야 한다
            tmp_sticker[j][n-i-1] = sticker[i][j]
            
    return tmp_sticker



n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]

for _ in range(k):
    sr, sc = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(sr)]

    # 2. 스티커 rotate 시키며 붙여보기
    for _ in range(4):
        if check_sticker(sticker):
            break
        else:
            # 붙일 공간이 없다면 rotate
            sticker = rotate()

# 3. 몇 칸 붙었는지 확인
cnt = 0
for i in range(n):
    for j in range(m):
        if notebook[i][j]:
            cnt += 1
print(cnt)