T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())

    boxes = [0] * N
    L, R = [], []
    for i in range(Q):
        Li, Ri = map(int, input().split())
        L.append(Li)
        R.append(Ri)

    for i in range(0, len(L)):
        for color in range(L[i], R[i] + 1):
            boxes[color - 1] = i + 1

    print(f'#{tc} ', end='')
    print(*boxes)