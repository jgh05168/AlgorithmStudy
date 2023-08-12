T = int(input())

def transform_list(input_list):
    result_dict = {}
    same_dict = {}
    # print(input_list)
    for bug in input_list:
        loc = tuple(bug[0])
        if loc not in result_dict.keys():
            result_dict.update({loc: (bug[1], bug[2])})
        else:
            if loc not in same_dict.keys():
                same_dict.update({loc : [result_dict[loc]]})
            same_dict[loc].append((bug[1], bug[2]))

    for key, value in same_dict.items():
        max_bug = 0
        value.sort(key=lambda x: x[0], reverse=True)
        max_dir = value[0][1]
        for val in value:
            max_bug += val[0]
        result_dict.update({key: (max_bug, max_dir)})

    # print(result_dict)
    # print()
    result_list = [[list(key), value[0], value[1]] for key, value in result_dict.items()]
    return result_list




for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    # cell 정보 생성(겉부분은 False 처리)
    area = [[False] + [True] * (N - 2) + [False] for _ in range(N)]
    for i in range(N):
        area[0][i] = False
        area[-1][i] = False

    # 미생물 정보 입력 / 저장
    bugs = []       # [0] : row | [1] : col | [2] : direction
                    # direction 정보
                    # 1 : 위쪽 | 2 : 아래쪽 | 3 : 왼쪽 | 4 : 오른쪽
    for i in range(K):
        bug_info = list(map(int, input().split()))
        bugs.append([[bug_info[0], bug_info[1]], bug_info[2], bug_info[3]])


    for time in range(1, M + 1):
        # 같은 location이 있는지 확인해봐
        # print(bugs)
        bugs_list = transform_list(bugs)
        # print(bugs_list)
        # print()
        for bug in bugs_list:
            row, col = bug[0][0], bug[0][1]
            # print(row, col)
            # 위쪽 이동
            if bug[2] == 1:
                # 만약 cell 주변부 도착이라면
                if row - 1 == 0:
                    bug[1] //= 2    # 개체수 절반
                    if bug[1] <= 0:
                        bug[1] = 0
                    bug[2] = 2      # 방향 전환
                bug[0][0], bug[0][1] = row - 1, col       # 현재 bug 정보 업데이트

            elif bug[2] == 2:
                # 만약 cell 주변부 도착이라면
                if row + 1 == N - 1:
                    bug[1] //= 2  # 개체수 절반
                    if bug[1] <= 0:
                        bug[1] = 0
                    bug[2] = 1  # 방향 전환
                bug[0][0], bug[0][1] = row + 1, col  # 현재 bug 정보 업데이트

            elif bug[2] == 3:
                if col - 1 == 0:
                    bug[1] //= 2  # 개체수 절반
                    if bug[1] <= 0:
                        bug[1] = 0
                    bug[2] = 4  # 방향 전환
                bug[0][0], bug[0][1] = row, col - 1  # 현재 bug 정보 업데이트

            elif bug[2] == 4:
                if col + 1 == N - 1:
                    bug[1] //= 2  # 개체수 절반
                    if bug[1] <= 0:
                        bug[1] = 0
                    bug[2] = 3  # 방향 전환
                bug[0][0], bug[0][1] = row, col + 1  # 현재 bug 정보 업데이트

        bugs = bugs_list
    # print(bugs)


    cnt = 0
    for i in range(len(bugs)):
        cnt += bugs[i][1]
    print(f'#{tc} {cnt}')
