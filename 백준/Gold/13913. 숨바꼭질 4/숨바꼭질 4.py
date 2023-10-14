'''
수빈이 -> 동생 가장 빠른 시간

걷는다 ? 1초 후에 x + 1, x-1로 이동 가능
순간이동 ? 1초 후에 2*X의 위치로 이동

BFS - 3가지 경우에 대해서 해보기.

'''

from collections import deque
import sys
input = sys.stdin.readline

dd = [1, -1]

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        cur_loc = queue.popleft()

        if cur_loc == sister:
            return cur_loc

        # 걷는 경우
        for d in range(len(dd)):
            next = cur_loc + dd[d]
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = visited[cur_loc] + 1
                queue.append(next)
                move[next] = cur_loc

        # 순간이동의 경우
        next = cur_loc * 2
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = visited[cur_loc] + 1
            queue.append(next)
            move[next] = cur_loc



subin, sister = map(int, input().split())
visited = [0] * 100001
move = [0] * 100001
subin = bfs(subin)

a = []
temp = subin
for _ in range(visited[sister] + 1):
    a.append(temp)
    temp = move[temp]


print(visited[sister])
print(*a[::-1])