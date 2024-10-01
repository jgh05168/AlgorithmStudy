'''
수 묶기

수열의 두 수를 묶는다
묶은 수는 서로 곱한 뒤 더한다
모든 수는 묶거나 묶지 않아야 한다.

풀이:
조건 1. 오름차순 정렬
조건 2. 음수는 무조건 곱한다. (홀수인 경우 0에 가까운 음수 제외하고는 다 묶기
조건 3. 0과 1은 덧셈으로 처리한다.
조건 4. 나머지는 다 묶은 뒤 더한다
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))


# 1. 세 구간으로 나눠주기(음수, 양수, 중립)
minus, plus, mid = [], [], []
for num in arr:
    if num < 0:
        minus.append(num)
    elif num > 1:
        plus.append(num)
    else:
        mid.append(num)

# 2. 오름차순 정렬
if len(minus) % 2 and mid.count(0):
    minus.append(0)
    mid.remove(0)
if minus:
    minus.sort()
if plus:
    plus.sort(reverse=True)

# 3. 곱해주고 더해주기
ans = 0
# 음수부터
if minus:
    # if len(minus) == 1:
    #     ans += minus[-1]
    # else:
    for i in range(0, len(minus) - 1, 2):
        ans += minus[i] * minus[i + 1]
    if len(minus) % 2:
        ans += minus[-1]

# 양수
if plus:
    for i in range(0, len(plus) - 1, 2):
        ans += plus[i] * plus[i + 1]
    if len(plus) % 2:
        ans += plus[-1]

# 나머지는 더해주기
if mid:
    for i in mid:
        ans += i

print(ans)