from collections import deque
import sys
input = sys.stdin.readline

r,c,n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

n=n-1

def search():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                queue.append((i,j))

def bombset():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = 'O'

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        graph[x][y] = '.'

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'O':
                graph[nx][ny] = '.'
                
while n:
    queue = deque()
    search()
    bombset()
    n-=1
    if n==0:
        break
    bfs()
    n-=1

for bomb in graph:
    print(*bomb, sep = '')
