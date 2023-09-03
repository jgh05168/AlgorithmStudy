
def change_magnet(magnet, rotate):
    visited[magnet] = 1

    if magnet == 2 or magnet == 3:
        # 왼쪽
        if not visited[magnet - 1] and magnets[magnet - 1][2] != magnets[magnet][6]:
            if rotate == -1:
                rotates[magnet - 1] = 1
            else:
                rotates[magnet - 1] = -1
            change_magnet(magnet - 1, rotates[magnet - 1])
        # 오른쪽 확인
        if not visited[magnet + 1] and magnets[magnet][2] != magnets[magnet + 1][6]:
            if rotate == -1:
                rotates[magnet + 1] = 1
            else:
                rotates[magnet + 1] = -1
            change_magnet(magnet + 1, rotates[magnet + 1])

    elif magnet == 1:
        if not visited[magnet + 1] and magnets[magnet][2] != magnets[magnet + 1][6]:
            if rotate == -1:
                rotates[magnet + 1] = 1
            else:
                rotates[magnet + 1] = -1
            change_magnet(magnet + 1, rotates[magnet + 1])

    elif magnet == 4:
        if not visited[magnet - 1] and magnets[magnet - 1][2] != magnets[magnet][6]:
            if rotate == -1:
                rotates[magnet - 1] = 1
            else:
                rotates[magnet - 1] = -1
            change_magnet(magnet - 1, rotates[magnet - 1])


T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    magnet1 = list(map(int, input().split()))
    magnet2 = list(map(int, input().split()))
    magnet3 = list(map(int, input().split()))
    magnet4 = list(map(int, input().split()))
    magnets = [[0], magnet1, magnet2, magnet3, magnet4]
    graph = [[0], [2], [1, 3], [2, 4], [3]]
    rotates = [0] * 5

    for _ in range(K):
        visited = [0] * 5
        rotates = [0] * 5
        magnet, rotate = map(int, input().split())

        rotates[magnet] = rotate
        change_magnet(magnet, rotate)

        for idx, value in enumerate(rotates):
            # 시계방향 회전
            if value == 1:
                end_mag = magnets[idx].pop()
                magnets[idx].insert(0, end_mag)

            # 반시계방향 회전
            elif value == -1:
                magnets[idx].append(magnets[idx].pop(0))

    # 점수 산출
    point = 0
    for i in range(1, len(magnets)):
        if magnets[i][0] == 1:
            point += 2 ** (i - 1)

    print(f'#{tc} {point}')