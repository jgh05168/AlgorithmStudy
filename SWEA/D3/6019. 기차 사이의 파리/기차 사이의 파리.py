T = int(input())

for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    t = D / (A + B)

    flymile = t * F


    print(f'#{tc} ', end='')
    print('%.10f' %float(flymile))

