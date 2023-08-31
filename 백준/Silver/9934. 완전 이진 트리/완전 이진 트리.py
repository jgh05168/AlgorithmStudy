
# merge & sort와 같이 이진트리로 분할하여 값을 저장
def dnc(start, end, idx):
    if start == end:
        return
    else:
        mid = (start + end) // 2
        tree[idx].append(buildings[mid])        # 현재 레벨에 맞는 노드 값 넣어주기
        dnc(start, mid, idx + 1)                # 왼쪽 자식노드 탐색
        dnc(mid + 1, end, idx + 1)              # 오른쪽 자식노드 탐색


K = int(input())
buildings = list(map(int, input().split()))
start, end = 0, len(buildings)
tree = [[] for _ in range((end // 2) + 1)]      # 레벨 별 빈 트리 생성
dnc(start, end, 0)

for i in range(len(tree)):
    print(*tree[i])
