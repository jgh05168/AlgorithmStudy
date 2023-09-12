import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [[] * M for _ in range(N)]

max_h = 0
min_h = 500
for i in range(N):
    land[i] = list(map(int, input().split()))

    if max_h < max(land[i]):
        max_h = max(land[i])
    if min_h > min(land[i]):
        min_h = min(land[i])

min_time = 100000000
ans_height = 0
# min 층부터 max 층까지 세보기
for height in range(min_h, max_h + 1):
    remove_block, stack_block = 0, 0
    total = 0
    for row in range(N):
        for col in range(M):
            if land[row][col] < height:
                stack_block += height - land[row][col]
            else:
                remove_block += land[row][col] - height

            # 인벤토리에 블럭이 없는데 칸수를 다 맞추려 했다면 이 층은 불가능
    if stack_block > remove_block + B:
        continue

    # 갖고있는 블럭을 다 사용할 수 있을 때만 정답 계산
    total = stack_block + remove_block * 2
    if min_time >= total:
        min_time = total
        ans_height = height

print(min_time, ans_height)
