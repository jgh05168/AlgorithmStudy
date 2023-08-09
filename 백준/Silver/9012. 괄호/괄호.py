T = int(input())

for tc in range(T):
    stack = []
    ans = ''
    N = input()
    for c in N:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                ans = 'NO'
                break

            val = stack.pop()
            if not(val == '(' and c == ')'):
                stack.append(val)

        if len(stack) == 0:
            ans = 'YES'
            
    if len(stack) != 0:
        ans = 'NO'

    print(ans)