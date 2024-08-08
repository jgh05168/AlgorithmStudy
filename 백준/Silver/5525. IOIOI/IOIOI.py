'''
I와 O가 교대로 나오는 경우 그냥 세버리기
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

ans = 0
sub_str = deque()
for i in range(m):
    if s[i] == 'I':
        if sub_str and sub_str[-1] == 'O':
            sub_str.append(s[i])
        else:
            sub_str = deque([s[i]])
    else:
        if sub_str and sub_str[-1] == 'I':
            sub_str.append(s[i])
        else:
            sub_str = deque()
    # 계산
    if len(sub_str) > n * 2 + 1:
        sub_str.popleft()
    if len(sub_str) == n * 2 + 1 and sub_str[0] == 'I' and sub_str[-1] == 'I':
        ans += 1
print(ans)