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
        if len(stack) == 0:  # 스택이 비었는지 아닌지 유무를 확인하기 위해서는 stack == [] 대신 len(stack)을 사용하자.
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
