T = int(input())

for tc in range(1, T + 1):
    N = { '2' : 0, '3' : 0, '5' : 0, '7' : 0, '11' : 0}
    val = int(input())

    while val > 1:
        for i in N.keys():
            if val % int(i) == 0:
                N[i] += 1
                val = val // int(i)

    cnt = []
    for i in N.values():
        cnt.append(i)

    print(f'#{tc} ', end='')
    print(*cnt)
