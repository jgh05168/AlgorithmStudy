'''
던진 막대기로 미네랄을 파괴할 수 있다.
R x C
네 방향 중 하나로 인접한 미네랄이 포함된 두 칸은 같은 클러스터이다.
- 턴을 번갈아가며 막대기를 던진다.
- 높이를 정한다, 막대는 땅과 수평을 이루며 날아간다
- 막대기가 날아가다 미네랄을 만나면, 그 칸에 있는 미네랄은 모두 파괴되고, 막대는 멈춘다
- 미네랄이 파괴된 이후, 남은 클러스터가 분리될 수 있따.
    - 중력의 영향을 받는다.
    - 클러스터의 모양은 변하지 않는다.
    - 다른 클러스터나 땅을 만나기 전까지 계속해서 떨어진다.
    - 다른 클러스터 위에 떨어질 수 있고, 그 이후에는 합쳐진다.

높이 1은 행렬의 바닥, R은 가장 위를 의미한다.
왼쪽 -> 오른쪽, 오른쪾 -> 왼쪽 이런 식으로 번갈아가며 던진다.
공중에 떠 있는 미네랄 클러스터는 없으며, 두 개 또는 그 이상의 클러스터가 동시에 떨어지는 경우도 없다.

풀이:
bfs, 시뮬
0. 초기 미네랄의 덩어리가 뭔지 확인한 다음, 덩어리 별 개수를 체크해야 한다.
1. 하나 부수기
2. 깨진 부분 윗부분에 미네랄이 있다면, bfs로 떨어져 나갔는지 체크(클러스터가 떨어지는 경우는 위에 아무것도 없을 때.
    2-1. 개수가 일치하지 않다면, 중력 작용
    2-2. 작용 이후, 새로운 클러스터 체크하기

'''

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

#    우  상  좌  하
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def init():
    # 0. 초기 클러스터들 맵 만들기
    cluster_dict = defaultdict(int)
    cluster_num = 1
    for i in range(n):
        for j in range(m):
            if cave[i][j] == 'x' and not clusters[i][j]:
                cluster_dict[cluster_num] = find_cluster(i, j, cluster_num)
                cluster_num += 1

    return clusters, cluster_dict

def find_cluster(sr, sc, cluster_num):
    queue = deque()
    queue.append((sr, sc))
    clusters[sr][sc] = cluster_num
    tmp = 1

    while queue:
        r, c = queue.popleft()

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not clusters[nr][nc] and cave[nr][nc] == 'x':
                queue.append((nr, nc))
                clusters[nr][nc] = cluster_num
                tmp += 1

    return tmp


def get_cluster(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    visited = [[0] * m for _ in range(n)]
    visited[sr][sc] = 1
    tmp = [(sr, sc)]

    while queue:
        r, c = queue.popleft()

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and cave[nr][nc] == 'x':
                tmp.append((nr, nc))
                queue.append((nr, nc))
                visited[nr][nc] = 1

    tmp.sort(key=lambda x: x[0], reverse=True)
    return tmp


def gravity(cluster):
    flag, move = 0, 0
    cluster = deque(cluster)
    while True:
        new_cluster = []
        bef_cluster = []
        while cluster:
            r, c = cluster.popleft()
            nr, nc = r + dr[3], c + dc[3]
            if 0 <= nr < n and 0 <= nc < m:
                # 만약 다른 클러스터를 만났다면,
                if cave[nr][nc] == 'x':
                    bef_cluster.append((r, c))
                    flag = 1
                    break
                # 아니라면, 내리기
                move = 1
                new_cluster.append((nr, nc))
                bef_cluster.append((r, c))
                cave[r][c] = '.'
            else:
                flag = 1
                break
        if flag:
            for nr, nc in bef_cluster:
                cave[nr][nc] = 'x'
            break
        else:
            for nr, nc in new_cluster:
                cave[nr][nc] = 'x'
            cluster = deque(new_cluster)

    return move



n, m = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(n)]
t = int(input())
stick_height = list(map(int, input().split()))

# 0. 초기 클러스터들 맵 만들기
clusters = [[0] * m for _ in range(n)]
clusters, cluster_dict = init()

# 1. 막대기 던지기
for tc in range(t):
    i = n - stick_height[tc]

    # 2. 가다가 만나는 클러스터 먼저 부수기
    # 방향 고려
    if not tc % 2:
        for j in range(m):
            if cave[i][j] == 'x':
                cluster_dict[clusters[i][j]] -= 1
                cave[i][j] = '.'
                break
    else:
        for j in range(m - 1, -1, -1):
            if cave[i][j] == 'x':
                cluster_dict[clusters[i][j]] -= 1
                cave[i][j] = '.'
                break

    # 3. 클러스터 찾기
    flag = 0
    for sd in range(len(dr)):       # 좌 우 상 만 확인할 것
        sr, sc = i + dr[sd], j + dc[sd]
        if 0 <= sr < n and 0 <= sc < m and cave[sr][sc] == 'x' and not flag:
            # 3-1. 같은 클러스터인지 찾기(두 개 이상의 클러스터가 동시에 떨어지는 경우는 없다)
            # 떨어진 클러스터 한 개 찾으면 그만이다 ㅋ
            cluster = get_cluster(sr, sc)
            # 만약 개수가 다르다면(떨어져 나왔다면)
            if len(cluster) != cluster_dict[clusters[sr][sc]] or not cave[i].count('x'):
                flag = gravity(cluster)
                if flag:
                    init()
                    break
            # 만약 허공에 떠있다면

for i in range(n):
    print(''.join(cave[i]))
