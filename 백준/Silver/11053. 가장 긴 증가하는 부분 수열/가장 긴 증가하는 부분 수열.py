N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N  # 각 인덱스에서의 최대 부분 수열 길이를 저장하는 배열
              # 각 순열은 자기자신만 갖으므로, 길이 인덱스의 값들은 모두 1로 설정

# DP(Bottom - Up)
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            # 현재 저장된 수열의 길이와 이전에 저장된 수열의 길이 + 1 간의 최대값을 구해 현재 저장된 수열의 길이에 업데이트
            dp[i] = max(dp[i], dp[j] + 1)

max_length = max(dp)
print(max_length)
