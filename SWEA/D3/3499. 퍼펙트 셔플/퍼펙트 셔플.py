T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    deck = list(input().split())

    # mid 인덱스 설정
    if N % 2 == 0:
        mid = N // 2
    else:
        mid = N // 2 + 1

    left = []
    right = []
    # left
    for i in range(mid):
        left.append(deck[i])
    # right
    for i in range(mid, N):
        right.append(deck[i])

    shuffle = []
    # left 혹은 right가 빌 때까지 반복
    while left or right:
        if left:    # left가 비지 않았다면
            shuffle.append(left.pop(0))
        if right:   # right가 비지 않았다면
            shuffle.append(right.pop(0))

    print(f'#{tc} ', end='')
    print(*shuffle)
