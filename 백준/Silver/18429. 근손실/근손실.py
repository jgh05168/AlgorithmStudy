def backtracking(i, N, weight):
    global cnt

    if i == N:
        cnt += 1
        return

    if weight < 500:
        return

    else:
        for day in range(N):
            if selected[day] == False:
                selected[day] = True
                weight = weight - K + A[day]
                backtracking(i + 1, N, weight)
                weight = weight + K - A[day]
                selected[day] = False

cnt = 0
N, K = map(int, input().split())
A = list(map(int, input().split()))
weight = 500
selected = [False] * N

backtracking(0, N, weight)

print(cnt)