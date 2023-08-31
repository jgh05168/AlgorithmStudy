def dnc(start, end, idx):
    if start == end:
        return
    else:
        mid = (start + end) // 2
        tree[idx].append(buildings[mid])
        dnc(start, mid, idx + 1)
        dnc(mid + 1, end, idx + 1)


K = int(input())
buildings = list(map(int, input().split()))
start, end = 0, len(buildings)
tree = [[] for _ in range((end // 2) + 1)]
dnc(start, end, 0)

for i in range(len(tree)):
    print(*tree[i])