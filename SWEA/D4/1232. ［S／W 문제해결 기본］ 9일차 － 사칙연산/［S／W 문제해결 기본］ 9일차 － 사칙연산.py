# 후위순회
def postorder(n):
    if n:
        postorder(lchild[n])    # 왼쪽 자식노드 존재 확인
        postorder(rchild[n])    # 오른쪽 자식노드 존재 확인
        # n이 연산자인지 피연산자인지 확인
        if tree[n].isdigit():   # 피연산자라면, stack에 저장
            stack.append(int(tree[n]))
        else:                   # 연산자라면
            case = tree[n]      # 연산자 case에 저장
            # 사칙연산 수행 후 tree의 연산자 자리에 계산된 값으로 업데이트
            if case == '+':
                x, y = stack.pop(-2), stack.pop()
                stack.append(x + y)
                tree[n] = str(x + y)
            elif case == '-':
                x, y = stack.pop(-2), stack.pop()
                stack.append(x - y)
                tree[n] = str(x - y)
            elif case == '*':
                x, y = stack.pop(-2), stack.pop()
                stack.append(x * y)
                tree[n] = str(x * y)
            elif case == '/':
                x, y = stack.pop(-2), stack.pop()
                stack.append(x // y)
                tree[n] = str(x // y)






for tc in range(1, 11):
    N = int(input())
    # 트리 생성, 왼쪽 / 오른쪽 자식노드 리스트 생성
    tree = [0] * (N + 1)
    lchild = [0] * (N + 1)     
    rchild = [0] * (N + 1)
    stack = []
    for i in range(N):
        info = list(input().split())
        tree[int(info[0])] = info[1]
        # 왼쪽 자식노드만 존재하는 경우
        if len(info) == 3:
            lchild[int(info[0])] = int(info[2])
        # 오른쪽 자식노드 역시 존재하는 경우
        elif len(info) == 4:
            lchild[int(info[0])] = int(info[2])
            rchild[int(info[0])] = int(info[3])
    postorder(1)
    print(f'#{tc} {stack[0]}')