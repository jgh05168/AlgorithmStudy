dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dir_dict = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
visited = [[[0] * 11 for _ in range(11)] for _ in range(4)]


def solution(dirs):
    answer = 0
    i, j = 5, 5
    
    for order in dirs:
        ni, nj = i + dr[dir_dict[order]], j + dc[dir_dict[order]]
        if not (0 <= ni < 11 and 0 <= nj < 11):
            continue
        bi, bj = i, j
        i, j = ni, nj
        if visited[dir_dict[order]][ni][nj]:
            continue
        print(ni, nj)
        # 정방향 방문 처리
        visited[dir_dict[order]][ni][nj] = 1
        # 역방향도 방문 처리
        visited[(dir_dict[order] + 2) % 4][bi][bj] = 1
        
        answer += 1
    
    return answer