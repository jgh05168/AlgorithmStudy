'''
DP

1. 숫자가 3개씩 적혀있다.

2. 아랫줄로 내려갈 떄 3가지 경우가 존재한다.

: dp[0]은 초기설정으로 지정해주고
1 ~ n까지 반복문 수행.
각 위치에 대한 최대값, 최소값을 각각 저장한다.

------------ 수정 --------------
dp를 2차원 배열로 하니 메모리초과가 발생했다.

-> dp를 각각 dp_min, dp_max로 설정해보기
'''

N = int(input())
# i=0일 떄(초기상태) dp 설정
grid = list(map(int, input().split()))
dp_max = [grid[0], grid[1], grid[2]]
dp_min = [grid[0], grid[1], grid[2]]

for i in range(1, N):
    grid = list(map(int, input().split()))
    ndp_max = [0, 0, 0]
    ndp_min = [0, 0, 0]
    # max 업데이트
    ndp_max = [grid[0] + max(dp_max[0], dp_max[1]), grid[1] + max(dp_max[0], dp_max[1], dp_max[2]), grid[2] + max(dp_max[1], dp_max[2])]
    # min 업데이트
    ndp_min = [grid[0] + min(dp_min[0], dp_min[1]), grid[1] + min(dp_min[0], dp_min[1], dp_min[2]), grid[2] + min(dp_min[1], dp_min[2])]

    dp_max, dp_min = ndp_max, ndp_min

print(max(dp_max), min(dp_min))
