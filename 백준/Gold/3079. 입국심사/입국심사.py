'''
걸리는 시간에 대해서 이진탐색 수행

예상 시간(mid)를 각각 입국심사대로 나눠준 몫을 모두 더해서 모든 사람 수보다 큰 지 작은 지 판단

'''


N, M = map(int, input().split())
T = [0] * N
for i in range(N):
    T[i] = int(input())

start, end = 0, max(T) * M

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(N):
        temp += mid // T[i]

    if temp < M:
        start = mid + 1
    else:
        end = mid - 1

print(start)