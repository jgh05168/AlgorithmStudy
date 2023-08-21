# 중위순회
def inorder(n):
    if n > N:       # n이 노드 값보다 크다면 반환
        return
    if n:
        inorder(n * 2)
        print(tree[n], end='')
        inorder(n * 2 + 1)

for tc in range(1, 11):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    tree = [0] * (N + 1)
    for i in range(N):
        info = list(input().split())
        p = int(info.pop(0))        # 현재 노드 위치 정보
        tree[p] = info.pop(0)       # 현재 노드 위치에 들어갈 값 저장
        while info:         # info에 변수가 더 남아있다면, 자식노드에 값 저장
            if ch1[p] == 0:
                ch1[p] = info.pop(0)
            else:
                ch2[p] = info.pop(0)

    print(f'#{tc} ', end='')
    inorder(1)
    print()
