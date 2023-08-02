T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]


    col1 = []
    for col in range(N):
        rotate = ''
        for row in range(N):
            rotate += arr[N - row - 1][col]
        col1.append(rotate)

    col2 = []
    for row in range(N):
        rotate = ''
        for col in range(N):
            rotate += arr[N - row - 1][N - col - 1]
        col2.append(rotate)

    col3 = []
    for col in range(N):
        rotate = ''
        for row in range(N):
            rotate += arr[row][N - col - 1]
        col3.append(rotate)


    new_arr = []
    for i in range(N):
        new_arr.append([col1[i], col2[i], col3[i]])

    print(f'#{tc}')
    for i in range(len(new_arr)):
        print(*new_arr[i])
