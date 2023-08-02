T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prime = [[2, 0], [3, 0], [5, 0], [7, 0], [11, 0]]
    prime_cnt = []
    while N != 1:
        for div in prime:
            if N % div[0] == 0:
                div[1] += 1
                N /= div[0]
                break


    print(f'#{tc}', end=' ')
    for cnt in prime:
        print(cnt[1], end=' ')
    print()