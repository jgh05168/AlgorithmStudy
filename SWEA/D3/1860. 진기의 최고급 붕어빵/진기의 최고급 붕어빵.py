T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    times = list(map(int, input().split()))
    ans = 'Possible'
    # 붕어빵 개수와 시간 별 사람의 수 관련 빈 리스트 생성
    line = [0] * 11112
    fishbread = [0] * 11112

    # 시간을 인덱스로 사람 수 저장
    for i in range(len(times)):
        line[times[i]] = 1

    # 붕어방이 나오는 시간에 대한 리스트에 붕어빵 개수를 저장
    for i in range(M, len(fishbread), M):
        fishbread[i] = K


    for idx in range(len(line)):
        if idx == 0:            # 0초에 사람이 오는 경우
            if fishbread[idx] - line[idx] < 0:      # 바로 줄 수 있는 붕어빵이 사람 수보다 적은 경우
                ans = 'Impossible'
                break
        else:       # 남은 붕어빵 개수 누적해서 가져오기
            fishbread[idx] += fishbread[idx - 1]
            if line[idx] > 0:       # 대기줄에 사람이 서있는 경우
                fishbread[idx] -= line[idx]         # 붕어빵을 지급한다.
                # print(idx, fishbread[idx])
                if fishbread[idx] < 0:      # 사람에게 붕어빵을 바로 줄 수 없는 경우
                    ans = 'Impossible'
                    break

    print(f'#{tc} {ans}')