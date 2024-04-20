'''
1. 각 그룹의 앞자리의 0의 전체 또는 일부를 축약할 수 있다.
2. 만약 0으로만 이루어져 있는 그룹이 있을 경우 그 중 한 개 이상 연속된 그룹을 하나 골라 콜론 2개(::)로 바꿀 수 있다.
    -> 이건 오직 한 번만 사용 가능하다.
'''

import sys
input = sys.stdin.readline

ipv6 = list(input().rstrip().split(':'))
ans = []
flag = 0
n = len(ipv6)
had_n = 0
for i in range(n):
    if ipv6[i]:
        had_n += 1

for idx in range(n):
    if ipv6[idx] == '':
        if not flag:
            for i in range(8 - had_n):
                ans.append("0000")
            flag = 1
    elif len(ipv6[idx]) < 4:
        ans.append('0' * (4 - len(ipv6[idx])) + ipv6[idx])
    else:
        ans.append(ipv6[idx])

for i in range(8):
    if i == 7:
        print(ans[i])
    else:
        print(f'{ans[i]}:', end='')