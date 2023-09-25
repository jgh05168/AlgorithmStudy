def dfs(u, visited, computers):
    visited[u] = 1
    for v in range(len(computers[u])):
        if computers[u][v] and v != u and not visited[v]:
            dfs(v, visited, computers)


def solution(n, computers):
    visited = [0] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            cnt += 1

    return cnt

# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))