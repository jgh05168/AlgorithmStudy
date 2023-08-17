def backtracking(i, N, weight):
    global cnt

    # 만약 case를 다 돌았다면 = 경우의 수가 존재한다
    if i == N:
        cnt += 1        # 카운트
        return

    # 3대 500보다 중량이 낮아진 경우, 백트래킹
    if weight < 500:
        return

    else:
        for day in range(N):        # 모든 날에 대해
            if selected[day] == False:      # 만약 사용하지 않은 키트라면
                selected[day] = True        # 사용함으로 변경
                weight = weight - K + A[day]    # 운동 후 중량 업데이트
                backtracking(i + 1, N, weight)  # 다음 날 확인
                weight = weight + K - A[day]    # 이전에 사용한 조건을 back시켜줌
                selected[day] = False           # 사용하지 않음 으로 업데이트

cnt = 0
N, K = map(int, input().split())
A = list(map(int, input().split()))
weight = 500        # 대학원생 중량
selected = [False] * N  # 그 날 사용한 키트에 대해 표시

backtracking(0, N, weight)

print(cnt)