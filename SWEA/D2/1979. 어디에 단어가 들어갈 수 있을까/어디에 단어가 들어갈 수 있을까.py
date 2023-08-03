T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(len(arr)):
        arr[i].append(0)
    arr.append([0] * (len(arr) + 1))


    cnt = 0

    for row in range(len(arr)):
        rowcnt = 0
        colcnt = 0
        for col in range(len(arr)):
            if arr[row][col] == 1:
                rowcnt += 1
                if rowcnt == K and arr[row][col + 1] == 0:
                    cnt += 1
            else:
                rowcnt = 0

            if arr[col][row] == 1:
                colcnt += 1
                if colcnt == K and arr[col + 1][row] == 0:
                    cnt += 1
            else:
                colcnt = 0





    print(f'#{tc} {cnt}')
