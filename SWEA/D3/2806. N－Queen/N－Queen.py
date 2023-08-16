
T = int(input())

# row = 0 부터 훑고 내려오기 때문에 위쪽은 확인할 필요가 없다.
drow = [0, 1, 1, 1, 0]
dcol = [1, 1, 0, -1, -1]

# 퀸의 이동경로를 False로 설정
def makeFalse(row, col):
    for d in range(len(drow)):
        for depth in range(N):
            nrow = row + drow[d] * depth
            ncol = col + dcol[d] * depth
            if 0 <= nrow < N and 0 <= ncol < N and arr[nrow][ncol] == True:
                track[row].append((nrow, ncol))     # False로 바꾼 경로를 저장(백트래킹 시 다시 True로 돌려놓기 위함)
                arr[nrow][ncol] = False

# 이동경로가 더이상 없기 때문에 이전에 False로 바꿔준 경로를 다시 True로 설정
def makeTrue(idx, track):
    for row, col in track[idx]:     # 현재 idx에 저장된 모든 좌표의 값들을 True로 변경
        arr[row][col] = True
    track[idx] = []                 # 인덱스 정보를 비워주는 역할


def check(queen, idx):
    global ans
    if N == 1:      # 자리가 1 by 1이라면, 
        ans = 1
        return

    if idx == N:    # 모든 어레이를 탐색했다면 = 가능한 경우가 있다는 것이다!
        ans += 1
        return

    else:
        for c in range(N):          # 한 row index의 열들에 대해 하나씩 조사
            if queen[idx][c]:       # 갈 수 있는 경로라면 ?
                makeFalse(idx, c)   # 퀸의 위치를 두고 현재 퀸이 갈 수 있는 거리들을 False 처리
                check(queen, idx + 1)   # 다음 index로 넘어간다
                makeTrue(idx, track)    # 다음 인덱스로 넘어갔을 떄 더이상 갈 곳이 없다면, 이전 인덱스의 방문 정보들에 대해 True로 다시 바꿔준다


for tc in range(1, T + 1):
    N = int(input())

    arr = [[True] * N for _ in range(N)]
    ans = 0
    track = [[] * N for _ in range(N)]      # 빈 배열 생성(False로 바꿔준 경로를 추적하기 위한 배열)
    check(arr, 0)
    print(f'#{tc} {ans}')