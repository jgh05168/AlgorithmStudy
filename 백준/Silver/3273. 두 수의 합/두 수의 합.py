'''
자연수 x가 주어졌을 때, ai + aj = x를 만족하는 쌍의 수를 구하자

수열의 크기 n <= 100000
'''

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

# 1 2 3 5 7 9 10 11 12
# 정렬 후, 수가 커지면 right idx 줄이고, 수가 작거나 같다면 left idx 옮기기

left, right = 0, n - 1
ans = 0
while left < right:
    total = arr[left] + arr[right]
    if total <= x:
        if total == x:
            ans += 1
        left += 1
    else:
        right -= 1

print(ans)