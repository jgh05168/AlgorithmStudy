n = 15
arr = [list(input().split()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'w':
            print('chunbae')
            exit()
        elif arr[i][j] == 'b':
            print('nabi')
            exit()
        elif arr[i][j] == 'g':
            print('yeongcheol')
            exit()