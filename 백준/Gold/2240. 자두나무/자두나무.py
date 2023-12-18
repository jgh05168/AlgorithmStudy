'''
현재 나무를 저장하는 변수 생성
매 초마다 이동해보고, 이동하지 않아보고를 결정하여 max값 저장


'''

import sys
input = sys.stdin.readline


t, w = map(int, input().split())
dp = [[0] * (w + 1) for _ in range(t + 1)]    # 먹느냐 안먹느냐
check_tree = [[0] * (w + 1) for _ in range(t + 1)]  # 어떤 나무에 서있는지 확인

# 초기 나무와 얻은 자두 값 초기화
for sj in range(w + 1):
    dp[0][sj] = 0
    check_tree[0][sj] = 1

for i in range(1, t + 1):
    cur_tree = int(input())
    for j in range(w + 1):
        # 현재 나무와 같은지 다른지 점수를 매기기
        if check_tree[i - 1][j] == cur_tree:
            point = 1
        else:
            point = 0

        if not j:       # 한번도 이동하지 않았을 경우
            dp[i][j] = dp[i - 1][j] + point
            check_tree[i][j] = check_tree[i - 1][j]
        else:
            # 다른 나무로 이동했을 때 점수를 얻는지 얻지 않는지 확인
            if check_tree[i - 1][j - 1] != cur_tree:
                next_point = 1
            else:       # 만약 이동했는데 현재 나무와 이전 나무가 같다면 점수를 얻지 못함
                next_point = 0

            # 이동하지 않고 점수를 획득하는 방법이 최선이므로 else에 처리
            if dp[i - 1][j - 1] + next_point > dp[i - 1][j] + point:
                dp[i][j] = dp[i - 1][j - 1] + next_point
                check_tree[i][j] = cur_tree
            else:
                dp[i][j] = dp[i - 1][j] + point
                check_tree[i][j] = check_tree[i - 1][j]

print(max(dp[-1]))