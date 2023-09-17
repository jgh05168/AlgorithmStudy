'''
1. 에라토스테네스의 체로 제곱수 판별
    -> 체의 개수는 max - min이여야 한다. ( 우리가 알고자 하는 범위 )
    -> 우리가 알고싶은 범위에 대해서만 체로 걸러주면 된다.
    -> 3번 경우에 대한 결과를 체로 걸러준다.

2. min과 max는 정해져 있으므로 while문을 max까지만 돌리면 된다.

3. 제곱으로 나누어 떨어지는 모든 경우를 제곱수라 하므로 그 경우에 대해서 모두 걸러줘야 한다.

'''

x, y = map(int, input().split())
arr = [False] * (y - x + 1)

i = 2
while i**2 <= y:

    # 제곱수에 대한 에라토스테네스의 체
    update = 0
    # min이 제곱수인지 아닌지 판단하기 위한 조건문 : 시작점이 min, max 범위 안에 있는지 확인해준다.
    if not x % (i ** 2):
        start = x // (i ** 2)
    else:
        start = x // (i ** 2) + 1

    while (i ** 2) * (start + update) <= y:
        if not arr[(i ** 2) * (start + update) - x]:
            arr[(i ** 2) * (start + update) - x] = True
        update += 1

    i += 1

cnt = 0
for i in range(len(arr)):
    if not arr[i]:
        cnt += 1

print(cnt)