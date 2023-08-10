T = int(input())

for tc in range(1, T + 1):
    prob = input()
    stack = []
    stick = 0
    did = False
    for case in prob:
        if case == '(':
            stack.append(case)
            did = False
        elif stack and case == ')':
            out = stack.pop()
            if out == '(' and did == False:
                stick += len(stack)
                did = True
            else:
                stick += 1


    print(f'#{tc} {stick}')
