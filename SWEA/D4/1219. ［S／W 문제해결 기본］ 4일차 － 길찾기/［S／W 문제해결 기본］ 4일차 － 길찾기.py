def dfs(v):
    visited = [False] * 100     # 방문 여부를 확인하는 리스트
    visited[v] = True
    stack = []                  # 빈 스택 생성

    while True:
        for w in graph[v]:
            if w == 99:         # 문제에서 도착점의 값 = 99라고 알려줌
                return 1        # 도착지에 도착했다면, 1 반환
            if visited[w] == False:     # 방문하지 않았다면, 
                stack.append(v)         # 이전 노드를 stack에 저장
                v = w                   # 현재 노드 정보 업데이트
                visited[v] = True       # 방문했다고 check
                break
        else:
            if stack:               # stack에 값이 존재한다면 -> 더이상 갈 노드가 없으면
                v = stack.pop()
            else:
                return 0            # dfs를 다 돌았는데 도착지가 없으니 0 반환


for i in range(10):
    tc, N = map(int, input().split())

    arr = list(map(int, input().split()))       # 정점, 간선 set를 한줄로 받아옴
    graph = [[] for _ in range(100)]            # 빈 인접리스트 생성
    for i in range(0, len(arr), 2):
        v, w = arr[i], arr[i + 1]               # v, w로 나누어줌
        graph[v].append(w)

    print(f'#{tc} {dfs(0)}')
