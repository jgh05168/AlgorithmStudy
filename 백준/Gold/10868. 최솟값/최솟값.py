'''
세그먼트 트리

재귀 사용해서 세그먼트 트리 구현
    -> 특정 구간에서 최솟값을 갖도록 함
이후 그 구간에 존재하는 최솟값을 세그먼트 트리에서 찾아서 출력

!! 세그먼트 트리 다시 공부하기 !!
'''

import sys
input = sys.stdin.readline

def min_v(left, right):
    return min(left, right)

def seg_tree(tree, node, left, right):
    # leaf node
    if left == right:
        tree[node] = arr[left]
        return tree[node]

    mid = (left + right) // 2
    left_val = seg_tree(tree, 2 * node, left, mid)
    right_val = seg_tree(tree, 2 * node + 1, mid + 1, right)
    tree[node] = min_v(left_val, right_val)
    return tree[node]


def query(start, end, node, left, right):
    # left ~ right 사이에 start ~ end가 포함되지 않는다면 무한대 return(최솟값 찾기이기 때문)
    if end < left or start > right:
        return int(1e9)

    if start <= left and right <= end:      # 내가 원하는 구역에 값이 있는 경우 return
        return tree[node]

    mid = (left + right) // 2
    left_val = query(start, end, 2 * node, left, mid)
    right_val = query(start, end, 2 * node + 1, mid + 1, right)
    return min_v(left_val, right_val)


n, m = map(int, input().split())
arr = []
tree = [0 for _ in range(4*n)]
for _ in range(n):
    arr.append(int(input()))

seg_tree(tree, 1, 0, n - 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(query(a - 1, b - 1, 1, 0, n - 1))
