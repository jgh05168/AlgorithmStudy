'''
그냥 제곱근 구하기 ?

이분탐색
'''


n = int(input())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)