'''
2048게임

같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
한번의 이동에서 이미 합쳐진 블록은 또다른 블록과 다시 합쳐질 수 없다.

4방향 이동 - 각각 합쳐지는 시작점이 다르기 때문에 따로 생각해 주어야 한다.
    -> 인덱스 마지막부터 처음 순으로 순회

최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록
놓을 공간이 없다면 return

시뮬레이션, 백트래킹
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def dfs(move, check):
    global max_block
    # 5번 모두 이동한 경우 or 이동이 불가능한 경우(게임 끝)
    if move == 5 or not check:
        max_block = max(max_block, max(map(max, board)))
        return


    # 상 하 좌 우
    # 상/하 는 col, row 순서로 순회하고, 좌/우 는 row, col 순으로 순회한다.
    for case in range(4):
        # 상
        if case == 0:
            check = False
            temp_list = []      # 되돌릴 때를 위한 리스트 저장
            merge_check = [[False] * N for _ in range(N)]
            for col in range(N):
                for row in range(N):
                    if board[row][col]:
                        cur_row = row
                        # 만약 값이 존재한다면, 합칠 수 있는 경우가 있는지 체크
                        cur_val = board[row][col]
                        temp_list.append((row, col, cur_val))
                        for nrow in range(row - 1, -1, -1):
                            # 0인 부분이라면, continue
                            if not board[nrow][col]:
                                continue
                            # 처음 마주하는 값이 현재 값과 다르다면 break
                            if board[nrow][col] != cur_val or merge_check[nrow][col]:
                                break
                            # 현재와 이전 값이 같다면 이전값의 자리에 합쳐주기
                            else:
                                # 무조건 이동한다.
                                check = True
                                merge_check[nrow][col] = True
                                temp_list.append((nrow, col, board[nrow][col]))
                                board[nrow][col] += cur_val
                                board[cur_row][col] = 0
                                cur_row = nrow
                                break   # 한 번 합쳤으면 다시 합쳐지지 않으므로 break
                        # 무조건 0이나 값이 나올 때까지 이동
                        while cur_row - 1 > -1 and not board[cur_row - 1][col]:
                            check = True
                            temp_list.append((cur_row - 1, col, board[cur_row - 1][col]))
                            board[cur_row - 1][col] = board[cur_row][col]
                            board[cur_row][col] = 0
                            cur_row -= 1
            dfs(move + 1, check)
            while temp_list:
                crow, ccol, cval = temp_list.pop()
                board[crow][ccol] = cval

        # 하
        if case == 1:
            check = False
            temp_list = []      # 되돌릴 때를 위한 리스트 저장
            merge_check = [[False] * N for _ in range(N)]
            for col in range(N):
                for row in range(N - 1, -1, -1):
                    if board[row][col]:
                        cur_row = row
                        # 만약 값이 존재한다면, 합칠 수 있는 경우가 있는지 체크
                        cur_val = board[row][col]
                        temp_list.append((row, col, cur_val))
                        for nrow in range(row + 1, N):
                            # 0인 부분이라면, continue
                            if not board[nrow][col]:
                                continue
                            # 처음 마주하는 값이 현재 값과 다르다면 break
                            if board[nrow][col] != cur_val or merge_check[nrow][col]:
                                break
                            # 현재와 이전 값이 같다면 이전값의 자리에 합쳐주기
                            else:
                                # 무조건 이동한다.
                                check = True
                                merge_check[nrow][col] = True
                                temp_list.append((nrow, col, board[nrow][col]))
                                board[nrow][col] += cur_val
                                board[cur_row][col] = 0
                                cur_row = nrow
                                break   # 한 번 합쳤으면 다시 합쳐지지 않으므로 break
                        # 무조건 0이나 값이 나올 때까지 이동
                        while cur_row + 1 < N and not board[cur_row + 1][col]:
                            check = True
                            temp_list.append((cur_row + 1, col, board[cur_row + 1][col]))
                            board[cur_row + 1][col] = board[cur_row][col]
                            board[cur_row][col] = 0
                            cur_row += 1
            dfs(move + 1, check)
            while temp_list:
                crow, ccol, cval = temp_list.pop()
                board[crow][ccol] = cval

        # 좌
        if case == 2:
            check = False
            temp_list = []
            merge_check = [[False] * N for _ in range(N)]
            for row in range(N):
                for col in range(N):
                    if board[row][col]:
                        cur_col = col
                        cur_val = board[row][col]
                        temp_list.append((row, col, cur_val))
                        for ncol in range(col - 1, -1, -1):
                            # 0인 부분이라면, continue
                            if not board[row][ncol]:
                                continue
                            # 처음 마주하는 값이 현재 값과 다르다면 break
                            if board[row][ncol] != cur_val or merge_check[row][ncol]:
                                break
                            else:
                                check = True
                                merge_check[row][ncol] = True
                                temp_list.append((row, ncol, board[row][ncol]))
                                board[row][ncol] += cur_val
                                board[row][cur_col] = 0
                                cur_col = ncol
                                break
                        while cur_col - 1 > -1 and not board[row][cur_col - 1]:
                            check = True
                            temp_list.append((row, cur_col - 1, board[row][cur_col - 1]))
                            board[row][cur_col - 1] = board[row][cur_col]
                            board[row][cur_col] = 0
                            cur_col -= 1
            dfs(move + 1, check)
            while temp_list:
                crow, ccol, cval = temp_list.pop()
                board[crow][ccol] = cval

        # 우
        if case == 3:
            check = False
            temp_list = []
            merge_check = [[False] * N for _ in range(N)]
            for row in range(N):
                for col in range(N - 1, -1, -1):
                    if board[row][col]:
                        cur_col = col
                        cur_val = board[row][col]
                        temp_list.append((row, col, cur_val))
                        for ncol in range(col + 1, N):
                            # 0인 부분이라면, continue
                            if not board[row][ncol]:
                                continue
                            # 처음 마주하는 값이 현재 값과 다르다면 break
                            if board[row][ncol] != cur_val or merge_check[row][ncol]:
                                break
                            else:
                                check = True
                                merge_check[row][ncol] = True
                                temp_list.append((row, ncol, board[row][ncol]))
                                board[row][ncol] += cur_val
                                board[row][cur_col] = 0
                                cur_col = ncol
                                break
                        while cur_col + 1 < N and not board[row][cur_col + 1]:
                            check = True
                            temp_list.append((row, cur_col + 1, board[row][cur_col + 1]))
                            board[row][cur_col + 1] = board[row][cur_col]
                            board[row][cur_col] = 0
                            cur_col += 1
            dfs(move + 1, check)
            while temp_list:
                crow, ccol, cval = temp_list.pop()
                board[crow][ccol] = cval


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_block = 0
dfs(0, True)    # count, block 크기, 옮겨졌는지 체크
print(max_block)