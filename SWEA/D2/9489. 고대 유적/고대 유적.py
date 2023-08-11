T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    pict = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0
    # row 방향
    for i in range(N):
        length = 0
        for j in range(M):
            if pict[i][j] == 1:
                length += 1
            else:
                if max_len <= length and length >= 2:
                    max_len = length
                    length = 0
            if max_len <= length and length >= 2:
                max_len = length

    # col 방향
    for j in range(M):
        length = 0
        for i in range(N):
            if pict[i][j] == 1:
                length += 1
            else:
                if max_len <= length and length >= 2:
                    max_len = length
                length = 0
            if max_len <= length and length >= 2:
                max_len = length

    print(f'#{tc} {max_len}')