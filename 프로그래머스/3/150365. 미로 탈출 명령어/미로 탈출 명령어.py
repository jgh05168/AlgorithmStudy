'''
1. 격자 바깥으로 나가기 불가능
2. 이동하는 총 거리가 k여야 함. 같은 격자를 2번 이상 방문해도 괜찮음
3. 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 한다.

d, l, r, u 순으로 이동해보기

풀이 : dfs, 이동거리가 총 k가 되었을 때만 빠져나오도록 함
k를 넘어서면 continue -> 재귀 깊이 총 2500보다 작다
같은자리 있을 수는 없지만, 뺑뺑 돌 수는 있음
'''

import sys
sys.setrecursionlimit(10**7)

dir_dict = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

answer = 'z'

def dfs(depth, r, c, er, ec, path, k, n, m):
        global answer
        if depth + abs(r - er) + abs(c - ec) > k:
            return
        if depth == k and (r, c) == (er, ec):
            answer = path
            return
        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and path < answer:
                dfs(depth + 1, nr, nc, er, ec, path + dir_dict[d], k, n, m)
            

def solution(n, m, x, y, r, c, k):
    global answer
    
    # 굳이 grid 만들 필요 없음
    er, ec = r - 1, c - 1
    # 초반부터 종료조건 걸기
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    
    dfs(0, x - 1, y - 1, er, ec, "", k, n, m)
    
    return answer