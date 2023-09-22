'''
사람 번호 : iterable
아는 관계 혹은 몇 사람을 거쳐도 알 수 있는 관계 = 무리

문제 : 몇 개의 무리 존재하는가?

그래프 탐색 문제
'''


def dfs(u):
    if visited[u]:
        return

    visited[u] = 1
    for v in people[u]:
        if not visited[v]:
            dfs(v)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N : 사람 수, M : 관계 수
    people = [[] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        x, y = map(int, input().split())
        people[x].append(y)
        people[y].append(x)

    cnt = 0
    for person in range(1, N + 1):
        if not visited[person]:
            dfs(person)
            cnt += 1

    print(f'#{tc} {cnt}')