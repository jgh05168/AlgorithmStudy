'''
- 상하좌우 장애물로 막히기 전 학생들을 모두 볼 수 있음
- 장애물 뒤 학생은 보지 못함
- 3개의 장애물을 설치함
- 모두의 감시를 피할 수 있어야 성공
- N 은 최대 6

놓을 수 있는 위치에 모두 설치해보기
'''

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def watch():
    for tr, tc in teachers:
        for d in range(len(dr)):
            ntr, ntc = tr + dr[d], tc + dc[d]
            while 0 <= ntr < n and 0 <= ntc < n:
                # 방해물 만난다면 종료
                if school[ntr][ntc] == 'O':
                    break
                # 학생을 만난다면 불가능한 경우이므로 return
                if school[ntr][ntc] == 'S':
                    return
                ntr += dr[d]
                ntc += dc[d]

    print('YES')
    exit()

def dfs(i):
    if i == 3:
        watch()
    else:
        for row in range(n):
            for col in range(n):
                if school[row][col] == 'X':
                    school[row][col] = 'O'
                    dfs(i + 1)
                    school[row][col] = 'X'

n = int(input())
school = [list(input().split()) for _ in range(n)]
teachers = []
for i in range(n):
    for j in range(n):
        if school[i][j] == 'T':
            teachers.append((i, j))
dfs(0)
print("NO")

