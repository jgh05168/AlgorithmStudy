T = int(input())

def recur(person, val):
    global max_v
    if person >= N:
        if max_v < val:
            max_v = val
        return
    if max_v >= val:
        return
    for i in range(N):
        if not arr[person][i]:
            continue
        if not selected[i]:
            selected[i] = 1
            recur(person + 1, val * (arr[person][i] / 100))
            selected[i] = 0

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    selected = [0] * N
    max_v = 0
    recur(0, 1)
    print(f'#{tc} {max_v * 100:.6f}')