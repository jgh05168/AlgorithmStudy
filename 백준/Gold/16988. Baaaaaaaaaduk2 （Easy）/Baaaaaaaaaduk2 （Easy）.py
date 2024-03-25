'''
바둑의 룰
1. 양 선수가 돌을 2개씩 둔다.
2. 상하좌우 인접해야 같은 그룹으로 친다.
3. 돌을 잡을 때는 빈 공간이 없어야 함
4. 스스로 잡히는 칸에도 들어갈 수 있다.
    = 본인이 두는 말은 아무리 둘러싸여있어도 잡히지 않음

돌 2개를 두어 상대 돌을 최대한 많이 죽이게끔 하는 프로그램
돌 2개를 두어 죽일 수 있는 상대 돌의 최대 갯수를 구하자

풀이 :
bfs와 브루트포스를 사용
1. 둘 수 있는 자리에 둬 본 다음 주변이 둘러싸여있는지 판단하기
주의) 빈틈없이 에워싸여야 딸 수 있는 것으로 간주한다.

내 돌 : 1
상대 돌 : 2

탐색을 진행할 땐 두 돌을 모두 놓은 뒤, 인접 위치를 탐색
20^4 = 160000

갇혀있는지 탐색하려면..
두번째 놓은 돌에서 인접한 상대방 돌을 찾아 그 부분을 시작으로 bfs 탐색
    - 상하좌우로 이동하며 상대방 돌을 찾고, 만약 0을 발견하면 죽일 수 없는 것임
    - 우리 돌을 만난다면 queue에 저장 x
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol, visited):
    queue = deque()
    queue.append((srow, scol))
    visited[srow][scol] = 1
    cnt = 1
    flag = 0
    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if not (0 <= nrow < n and 0 <= ncol < m):
                continue
            if not game[nrow][ncol]:        # 여기서 그냥 return 0 하면 다음 탐색떄 걸린다
                flag = 1
            if visited[nrow][ncol]:
                continue
            elif game[nrow][ncol] == 2:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = 1
                cnt += 1

    if not flag:
        return cnt
    else:
        return 0

def my_stone(stone_cnt, my_list):
    global max_stone
    if stone_cnt == 2:
        # 4방향에 대해 bfs 돌리며 딸 수 있는 stone 체크 -- 실패
        # 그냥 모든 상대방 돌에 대해 탐색해보기
        tmp = 0
        visited = [[0] * m for _ in range(n)]
        for srow in range(n):
            for scol in range(m):
                if game[srow][scol] == 2 and not visited[srow][scol]:
                    tmp += bfs(srow, scol, visited)
        max_stone = max(max_stone, tmp)
        return

    for row in range(n):
        for col in range(m):
            if not game[row][col] and not selected[row][col]:
                selected[row][col] = 1
                game[row][col] = 1
                my_stone(stone_cnt + 1, my_list + [(row, col)])
                game[row][col] = 0
                selected[row][col] = 0


n, m = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(n)]
selected = [[0] * m for _ in range(n)]
max_stone = 0
my_stone(0, [])

print(max_stone)