N, M = map(int, input().split())

arr = list(i for i in range(1, N + 1))

# 중복이 없는 순열의 경우
# 부분집합을 구하여 문제 해결
# 백트래킹을 사용하여 문제를 푸는 방법 공부 필요 !!
pers = []
for i in range(1 << N):         # 1 << 4 : 2진수 1을 4번 shifting -> 0b10000(16)
    # print(bin(i))
    sample = []
    for j in range(N):
        if i & (1 << j):
            sample.append(arr[j])
    pers.append(sample)

pers.sort()
for per in pers:
    if len(per) == M:
        print(*per)