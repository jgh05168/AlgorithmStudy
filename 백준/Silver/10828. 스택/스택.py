import sys
input = sys.stdin.readline

N = int(input())

stack = []

for test_case in range(0, N):
    order = list(map(str, input().split()))

    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:  # 수정: 빈 스택인지 확인
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(stack) == 0:  # 수정: 빈 스택인지 확인
            print(-1)
        else:
            print(stack[-1])
