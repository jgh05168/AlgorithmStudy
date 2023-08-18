# 양방향 방향벡터 설정
#     6 | 12    5 | 11   3 | 9  1 | 7
dr = [[1, -1], [1, -1], [0, 0], [-1, 1]]
dc = [[0, 0], [1, -1], [1, -1], [1, -1]]


def omoc(row, col, color):
    for d in range(len(dr)):
        uprow, upcol = row, col         # 정방향 확인을 위한 좌표 생성
        downrow, downcol = row, col     # 역방향 확인을 위한 좌표 생성
        check = 0       # 오목이 완성되었는지 연속되는 돌의 개수로 확인
        cur_loc = []    # 연속적으로 놓여지는 돌의 위치를 저장

        # 정방향(아래,오른쪽)
        # 좌표가 오목판의 범위 내에 있고, 입력으로 들어온 돌의 색과 같을 때 반복. 틀린경우 바로 빠져나온다.
        while 0 <= downrow < N and 0 <= downcol < N and board[downrow][downcol] == color:
            check += 1
            cur_loc.append((downrow, downcol))
            downrow = downrow + dr[d][0]
            downcol = downcol + dc[d][0]

        # 역방향(위, 왼쪽)
        # 좌표가 오목판의 범위 내에 있고, 입력으로 들어온 돌의 색과 같을 때 반복. 틀린경우 바로 빠져나온다.
        while 0 <= uprow < N and 0 <= upcol < N and board[uprow][upcol] == color:
            check += 1
            cur_loc.append((uprow, upcol))
            uprow = uprow + dr[d][1]
            upcol = upcol + dc[d][1]

        check -= 1      # 정방향과 역방향을 두 번 실행하므로 초기의 check가 한 번 겹친다.
        if check == 5:  # 오목일 경우
            # 문제의 조건에서 세로로 완성되었을 경우, 왼쪽 첫번째 돌의 위치를 출력해야 한다.
            # 따라서 현재 저장된 완성된 돌의 위치들을 column 을 기준으로 정렬해주었음
            cur_loc.sort(key=lambda x : x[1])
            # print(cur_loc)
            return check, cur_loc[0][0], cur_loc[0][1]      # 오목 check, 가장 왼쪽의 row, col 값 반환

    return check, row, col       # 어차피 오목이 성공하지 않았으므로 check, 입력의 row, col을 되돌려준다.


N = 19
board = [list(map(int, input().split())) for _ in range(N)]
find = False

# 오목판 탐색
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 or board[i][j] == 2:        # 만약 오목돌 하나가 탐색되었다 ?
            color = board[i][j]                         # 색을 지정해준다
            check, r, c = omoc(i, j, color)             # 오목인지 아닌지 판단
            if check == 5:                              # 오목이 완성되었다면
                find = True                             # 찾았다고 확인 후 반복문을 빠져나온다.
                break

    if find == True:        # find의 역할 : 이중 for문을 빠져나오기 위함
        break

if find == True:            # 오목을 찾은 경우의 출력
    print(color)
    print(r + 1, c + 1)
else:                       # 아닌 경우 : 이긴 사람이 없으므로 0 출력
    print(0)