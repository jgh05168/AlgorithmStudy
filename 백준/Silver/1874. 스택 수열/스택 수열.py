'''
풀이:
1. 일단 1씩 입력 받으면서 stack에 저장
2. 만약 현재 수열과 같은 것을 만나면 수열에서 popleft, 스택에서도 pop
3. 같은 값이 계속 존재할 때 까지 pop
'''

import sys
input = sys.stdin.readline

stack = [0]
ans = []
used = set()
n = int(input())
for _ in range(n):
    cur_v = int(input())

    if stack and stack[-1] == cur_v:

        ans.append('-')
        stack.pop()
    else:
        for i in range(stack[-1] + 1, cur_v):
            if i in used:
                continue
            stack.append(i)
            ans.append('+')
        ans.append('+')
        ans.append('-')
    used.add(cur_v)

if not stack[-1]:
    for i in ans:
        print(i)
else:
    print("NO")