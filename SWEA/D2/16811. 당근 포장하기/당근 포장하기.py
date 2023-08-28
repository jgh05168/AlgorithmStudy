# 인덱스를 갖고 노는 문제들은 각각 인덱스 탐색 범위를 잘 조절해서 해결해야 한다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 당근은 크기 순이 아니다.
    carrots = list(map(int, input().split()))
    ans = -1
    # 정렬 필요
    carrots.sort()
    min_v = 1000
    
    #  N개의 원소를 가진 1차원 배열을 3개의 영역으로 나누기 위해서 ..
    #  (각 영역은 최소 1개 이상의 원소를 가짐)
    # 배열 나누기 문제의 경우 인덱스 슬라이싱으로 해결하면 좋다.
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            # 같은 것들끼리 나누어여한다.
            if carrots[i] != carrots[i + 1] and carrots[j] != carrots[j + 1]:
                small = i + 1
                mid = j - i
                large = N - 1 - j
                # 한 박스에 포장할 수 있는 최대 당근 개수
                if small <= N//2 and mid <= N//2 and large <= N//2: 
                    if min_v > max(small, mid, large) - min(small, mid, large):
                        min_v = max(small, mid, large) - min(small, mid, large)
    
    if min_v == 1000:
        min_v = -1

    print(f'#{tc} {min_v}')