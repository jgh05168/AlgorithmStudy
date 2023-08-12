# List와 Dictionary로 문제 해결
# List에 [[y축 좌표, x축 좌표], 미생물 수, 방향] 식으로 저장
# transform_list 함수를 사용하여 미생물들이 한곳에 모이는 경우(x, y 좌표가 같은 경우) 미생물의 개수에 따라 방향을 정해주고, 값을 더해주어 반환
T = int(input())


def transform_list(input_list):
    result_dict = {}        # (y, x) : (미생물 수, 방향) 꼴의 dictionary 생성
    same_dict = {}          # (y, x)가 같은 값들에 대해 dictionary 생성
                            # (y, x) : [(미생물 수1, 방향1), (미생물 수2, 방향2) ...] 꼴로 저장하여 하나의 좌표에 대해 여러 개의 정보를 비교

    for bug in input_list:      # input_list의 각 좌표([[y, x], 미생물 수, 방향])을 순차적으로 탐색
        loc = tuple(bug[0])     # 불러온 좌표 정보를 튜플로 생성
        if loc not in result_dict.keys():   # result_dict 의 key에 좌표 정보가 없다면
            result_dict.update({loc: (bug[1], bug[2])})     # result_dict에 좌표 정보를 key로, value에 ( 미생물 수, 방향) 모양으로 저장
        else:               # key에 좌표 정보가 있다면 ==> 미생물의 위치가 겹치는 부분이 존재한다!
            if loc not in same_dict.keys():         # 만약 없다는 것을 확인했는데, same_dict에 한번도 저장된 적이 없다면 ?
                same_dict.update({loc : [result_dict[loc]]})        # result_dict에 저장된 초기 키, 값 정보를 업데이트
            same_dict[loc].append((bug[1], bug[2]))         # 이후 현재 겹치는 부분의 새로운 정보를 저장

    # same_dict에 저장된 값들을 하나씩 비교하여 미생물의 최고 개수와 최고 개수의 방향을 찾자
    for key, value in same_dict.items():        # same_dict의 key와 value를 items()를 이용하여 불러옴
        max_bug = 0            # 미생물의 총 합을 구하기 위해 초기화
        value.sort(key=lambda x: x[0], reverse=True)        # 좌표가 같은 것들을 미생물 수를 기준으로 내림차순 정렬(lambda 숙지)
        max_dir = value[0][1]           # 정렬된 가장 큰 미생물 수의 좌표를 max_dir로 설정
        for val in value:               # 값에 들어있는 각각의 정보에 대해
            max_bug += val[0]           # 미생물 총 개수를 위해 더해준다.
        result_dict.update({key: (max_bug, max_dir)})       # result_dict에 새로운 정보를 덮어씌워 업데이트 해준다.

    # print(result_dict)
    # print()
    result_list = [[list(key), value[0], value[1]] for key, value in result_dict.items()]   # input_list와 같은 꼴로 변환 후 반환
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
