'''
같은 알파벳이 적힌 칸은 두 번 지날 수 없음

최대 몇 칸 지날 수 있는지 구하시오.
(0, 0) 시작

풀이 :
알파벳은 set을 만들어 저장
dfs로 이동
최대 칸 수 저장하기

단순 dfs ?

----- 그지같은 문제 -----
sys, setrecursivelimit 쓰면 시초 or 멤초 난다.

쟤네 빼고 제출하니까 통과 ;;
'''

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(row, col, cnt):
    global ans

    ans = max(ans, cnt)
    for d in range(len(dr)):
        nr, nc = row + dr[d], col + dc[d]
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] not in alphabet:
            alphabet.add(grid[nr][nc])
            dfs(nr, nc, cnt + 1)
            alphabet.remove(grid[nr][nc])


R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
alphabet = set()

alphabet.add(grid[0][0])
ans = 0
dfs(0, 0, 1)

print(ans)

