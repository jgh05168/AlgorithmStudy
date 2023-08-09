for tc in range(1, 11):
    N, string = input().split()

    stack = []

    for c in string:
        if c not in stack:
            stack.append(c)
        else:
            out = stack.pop()
            if out != c:
                stack.append(out)
                stack.append(c)

    print(f"#{tc} {''.join(stack)}")