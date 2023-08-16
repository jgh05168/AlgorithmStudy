def infix2post(exp):
    operand = []
    post = []
    for c in exp:
        if c.isdigit():
            post.append(c)
        else:
            if operand == []:
                operand.append(c)
            else:
                if c == '*':
                    operand.append(c)
                else:
                    while operand:
                        post.append(operand.pop())
                    operand.append(c)
    while operand:
        post.append(operand.pop())
    return post

def postcalc(post):
    stack = []
    for c in post:
        if c.isdigit():
            stack.append(c)
        elif c == '*':
            x, y = int(stack.pop(-2)), int(stack.pop())
            stack.append(str(x * y))
        elif c == '+':
            x, y = int(stack.pop(-2)), int(stack.pop())
            stack.append(str(x + y))

    return int(stack[-1])

for tc in range(1, 11):
    length = int(input())

    exp = input()
    post = infix2post(exp)

    print(f'#{tc} {postcalc(post)}')