def makeFalse(row, col, queen, cols, diag, rev_diag):
    queen[row] = col
    cols[col] = True
    diag[row - col + N - 1] = True
    rev_diag[row + col] = True

def makeTrue(row, col, queen, cols, diag, rev_diag):
    queen[row] = -1
    cols[col] = False
    diag[row - col + N - 1] = False
    rev_diag[row + col] = False

def check(queen, row, cols, diag, rev_diag):
    global ans
    if row == N:   # 모든 어레이를 탐색했다면 = 가능한 경우가 있다는 것이다!
        ans += 1
        return

    for col in range(N):
        # 주대각선과 부대각선을 사용하여 퀸들이 겹치지 않도록 관리하는 핵심 아이디어 --> 둘 다 False인 부분을 확인하는 것이 키포인트
        # row - col + N - 1 : 주대각선을 왼쪽 위에서 오른쪽 아래로 향하는 방향으로 표현
        # row + col : 부대각선을 왼쪽 아래에서 오른쪽 위로 향하는 방향으로 표현
        # 주대각선이 지나는 모든 좌표들을 row - col + N - 1 식에 넣어보면 항상 같은 값을 같는다 == 주대각선 배열의 인덱스 번호
        # 부대각선이 지나는 모든 좌표들을 row + col 식에 넣어보면 항상 같은 값을 같는다 == 부대각선 배열의 인덱스 번호
        '''
        ex) 4 by 4 행렬 기준
        
        if: (1, 2)가 지나는 주대각선의 좌표 : (0, 1), (2, 3)
            위 좌표들은 항상 2의 값을 갖는다 --> diag[row - col + N - 1] = True
            
        elif: (1, 2)가 지나는 부대각선의 좌표 : (0, 3), (2, 1), (3, 0)
            위 좌표들은 항상 3의 값을 갖는다 --> rev_diag[row + col] = True
        
        '''
        if not cols[col] and not diag[row - col + N - 1] and not rev_diag[row + col]:
            makeFalse(row, col, queen, cols, diag, rev_diag)
            check(queen, row + 1, cols, diag, rev_diag)
            makeTrue(row, col, queen, cols, diag, rev_diag)

N = int(input())

queen = [-1] * N
cols = [False] * N
rev_diag = [False] * (2 * N - 1)
diag = [False] * (2 * N - 1)

ans = 0
check(queen, 0, cols, diag, rev_diag)
print(ans)
