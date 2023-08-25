T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    k = 1
    cnts = []
    cnt = 0
    while True:
        new_n = str(k * N)
        for i in new_n:
            if i not in cnts:
                cnts.append(i)

        if len(cnts) == 10:
            break
        k += 1

    print(f'#{tc} {int(new_n)}')