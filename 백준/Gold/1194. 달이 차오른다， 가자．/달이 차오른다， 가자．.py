'''
키를 얻은 경우를 비트마스킹으로 구현
ex) 만약 5번 키를 얻었다면, 현재 갖고있는 key + (1 << key_numb) visited에 저장

key를 얻은 경우 새로운 층으로 이동하는 경우와 그냥 이동하는 경우를 나누어서 생각해야한다.
key_dict, door_dict 필요

bfs + 비트마스킹
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 비트마스킹으로 연산을 수행할 것이기 때문에 원래 key값 - 1로 초기화
# ex) 1 << 1 : 2(10), 1 << 6 : 32(100000)
keys_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
doors_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}


def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol, 0))
    visited[0][srow][scol] = 0

    while queue:
        row, col, get_keys = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and maze[nrow][ncol] != '#' and visited[get_keys][nrow][ncol] == -1:
                # 현재 위치가 도착지인 경우
                if maze[nrow][ncol] == '1':
                    return visited[get_keys][row][col] + 1

                # 현재 위치가 단순 이동할 수 있는 경우
                elif maze[nrow][ncol] == '.':
                    visited[get_keys][nrow][ncol] = visited[get_keys][row][col] + 1
                    queue.append((nrow, ncol, get_keys))

                # 현재 위치가 문인 경우
                elif maze[nrow][ncol].isupper():
                    door = maze[nrow][ncol]
                    if get_keys & (1 << doors_dict[door]):      # 만약 문을 열 수 있다면,
                        visited[get_keys][nrow][ncol] = visited[get_keys][row][col] + 1
                        queue.append((nrow, ncol, get_keys))

                # 열쇠를 찾은 경우
                else:
                    # 만약 열쇠를 아직 찾지 못한 경우
                    key = maze[nrow][ncol]
                    if not (get_keys & (1 << keys_dict[key])):
                        visited[get_keys + (1 << keys_dict[key])][nrow][ncol] = visited[get_keys][row][col] + 1
                        queue.append((nrow, ncol, get_keys + (1 << keys_dict[key])))
                    # 그냥 이동할 수도 있다.('.' 취급)
                    visited[get_keys][nrow][ncol] = visited[get_keys][row][col] + 1
                    queue.append((nrow, ncol, get_keys))

    return -1


N, M = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(N)]

minsik = 0
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            minsik = (i, j)
            maze[i][j] = '.'
            break

visited = [[[-1] * M for _ in range(N)] for _ in range(1 << 6)]
print(bfs(minsik[0], minsik[1]))

