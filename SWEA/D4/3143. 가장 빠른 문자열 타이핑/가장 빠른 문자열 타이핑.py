T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()

    key_cnt = 0
    p = 0
    t = 0

    while t < len(A):
        if A[t] != B[p]:
            key_cnt = key_cnt - p
            t = t - p
            p = -1
        t += 1
        p += 1
        key_cnt += 1
        if p == len(B):
            key_cnt = key_cnt - p + 1
            p = 0

    print(f'#{tc} {key_cnt}')
