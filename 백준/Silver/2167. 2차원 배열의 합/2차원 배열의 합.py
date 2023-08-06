
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# prefis_sum은 4칸씩 더해가며 sum을 누적한다.
# 1 2 3                 0  0  0  0
# 4 5 6     의 경우 -->  0  1  3  6
#                       0  5 12 21
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = arr[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

K = int(input())

for tc in range(K):
    s_row, s_col, f_row, f_col = map(int, input().split())

    # prefix sum 배열을 사용하여 부분 그리드의 합 계산
    total = prefix_sum[f_row][f_col] - prefix_sum[s_row - 1][f_col] - prefix_sum[f_row][s_col - 1] + prefix_sum[s_row - 1][s_col - 1]

    print(total)
