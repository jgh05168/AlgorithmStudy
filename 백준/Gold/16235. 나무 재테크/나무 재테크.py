'''
n x n
가장 처음 모든 칸에 양분은 5만큼씩 들어있다.
같은 칸에 여러 개의 나무가 심어져 있을 수도 있음
봅 : 자신의 나이만큼 양분을 먹고, 나이가 1 증가
    - 각각 나무는 나무가 있는 칸에 있는 양분만 먹을 수 있다.
    - 여러 나무가 존재한다면, 어린 나무부터 양분 섭취
    - 양분이 부족하다면 그 나무는 즉시 죽는다.
여름 : 봄에 죽은 나무가 양분으로 변한다.
    - 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
    - 소숫점 아래는 버린다.
가을 : 나무 번식
    - 나무의 나이가 5의 배수여야 번식한다.
    - 인접한 8개 칸에 나이가 1인 나무가 생긴다.
겨울 : 땅에 양분을 추가한다.
    - 각 칸에 추가되는 양분의 양은 입력으로 주어진다.

풀이 :
시뮬레이션
그냥 순서대로 구현하기
칸에는 heapq를 사용하여 나무 정보를 저장
    -> 시초가 난다. (heapq는 O(logn))
    -> deque 사용하기 (정렬을 안해주므로 O(1)의 시간복잡도)
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def spring():
    global dead_tree
    for r in range(n):
        for c in range(n):
            # 나무가 없다면 continue
            if not tree[r][c]:
                continue
            new_tree = deque()
            while tree[r][c]:
                this_tree = tree[r][c].popleft()
                # 양분 먹을 수 있는지 체크
                if this_tree <= grid[r][c]:
                    grid[r][c] -= this_tree
                    this_tree += 1
                    new_tree.append(this_tree)
                else:
                    dead_tree.append((r, c, this_tree))
            tree[r][c] = new_tree


def summer():
    global dead_tree
    while dead_tree:
        r, c, soil = dead_tree.pop()
        grid[r][c] += (soil // 2)
    dead_tree = []


def fall():
    new_tree = []
    for r in range(n):
        for c in range(n):
            for tree_idx in range(len(tree[r][c])):
                if not tree[r][c][tree_idx] % 5:
                    for d in range(len(dr)):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < n:
                            new_tree.append((nr, nc))
    for nr, nc in new_tree:
        tree[nr][nc].appendleft(1)


def winter():
    for r in range(n):
        for c in range(n):
            grid[r][c] += soil_info[r][c]


n, m, k = map(int, input().split())
grid = [[5] * n for _ in range(n)]
soil_info = [list(map(int, input().split())) for _ in range(n)]
tree = [[deque() * n for _ in range(n)] for _ in range(n)]
dead_tree = []
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

for _ in range(k):
    # 봄
    spring()

    # 여름
    summer()

    # 가을
    fall()

    # 겨울
    winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)