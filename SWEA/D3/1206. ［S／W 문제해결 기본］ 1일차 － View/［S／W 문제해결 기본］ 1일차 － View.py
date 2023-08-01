T = 10

for tc in range(1, T + 1):
    N = int(input())

    buildings = list(map(int, input().split()))

    # 조망권을 갖는 세대 수
    count = 0


    # 반복문을 통해 각 빌딩의 조망권이 확보된 세대의 수를 세 줌

    # 중첩반복문 사용 - 안쪽 : 빌딩의 층 수 / 바깥쪽 : 빌딩의 개수
    for i in range(2, N - 2):
        # buildins[i] = i 번째 빌딩의 높이
        height = buildings[i]
        for j in range(height, -1, -1):
            # 각 건물의 좌 우측 2칸 거리를 고려하여 조건 생성
            if j > buildings[i - 1] and j > buildings[i - 2] and j > buildings[i + 1] and j > buildings[i + 2]:
                count += 1
            else:
                break

    print(f'#{tc} {count}')
