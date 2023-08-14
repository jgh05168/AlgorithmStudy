
def inf2post(expression):
    operand = []
    post = []
    for c in expression:
        if not c.isdigit():
            if not operand:
                operand.append(c)
            else:
                post.append(operand.pop())
                operand.append(c)
        else:
            post.append(c)
    while operand:
        post.append(operand.pop())
    return post

def calc(expression):
    total = 0
    stack = []
    for c in expression:
        if c.isdigit():
            stack.append(c)
        elif c == '+':
            x, y = int(stack.pop(-2)), int(stack.pop())
            stack.append(str(x + y))

    return int(stack[-1])

for tc in range(1, 11):
    length = int(input())
    expression = input()

    post = inf2post(expression)

    print(f'#{tc} {calc(post)}')
