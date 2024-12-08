'''
루트 노드부터 시작하여, 최대한 많은 수의 양을 모으는 경우를 구하자

-> dfs, bfs 두 방법 모두 가능할듯
일단 양과 늑대의 수를 구해야 한다.
bfs로 해보기 
1. 현재 큐에는 있지만 가보지 않은 경우에 대한 정보를 담은 큐도 필요함
2. 현재 위치에서 가볼만한 다음 위치를 저장해놓기 위한 배열 필요함
'''

from collections import deque

def solution(info, edges):
    answer = 0
    n = len(info)
    graph = [[] * n for _ in range(n)]
    for s, e in edges:
        graph[s].append(e)
    
    queue = deque([(0, 0, 0, set())])      # 노드, 양, 늑대, 방문 배열
    visited = [0] * n
    wait_queue = deque()
    
    while queue:
        u, sheeps, wolves, path = queue.popleft()
        # 먼저, 현재 위치의 양, 늑대 정보 업데이트
        if not info[u]:
            sheeps += 1
        else:
            wolves += 1
        # continue 조건    
        if sheeps <= wolves:
            continue
        answer = max(answer, sheeps)
        
        tmp_path = set(graph[u])
        tmp_path.update(path)
        # print(u, sheeps, wolves)
        for v in tmp_path:
            queue.append((v, sheeps, wolves, tmp_path.difference(set([v]))))

    return answer