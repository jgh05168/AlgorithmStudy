V = int(input())
E = int(input())

# dfs(재귀)
def dfs(v):
    if visited[v] == True:
        return
    else:
        visited[v] = True
        if v not in graphs.keys():
            return
        for w in graphs[v]:
            if visited[w] == False:
                dfs(w)

graphs = {}     # 인접리스트 생성을 위한 딕셔너리
visited = [False] * (V + 1)     # 방문한 노드인지 확인하는 리스트
for _ in range(E):
    v, w = map(int, input().split())        # 현재노드, 인접노드 input
    # 무방향 그래프이기 때문에 양 쪽 모두에 대한 간선을 연결해 주어야 한다.
    # 정방향
    if v in graphs.keys():
        graphs[v].append(w)
    else:
        graphs.update({v: [w]})
    # 역방향
    if w in graphs.keys():
        graphs[w].append(v)
    else:
        graphs.update({w: [v]})

for key in graphs.keys():       # 1번 노드부터 탐색 시작
    if key == 1:
        dfs(key)

cnt = - 1       # 시작 노드 1을 제외하기 위해 초기값을 -1로 설정
for val in visited:
    if val == True:         # 1에서 시작되는 노드에 방문했을 시
        cnt += 1
if visited[1] == False:     # 만약 시작노드 1이 없다면?
    cnt = 0                 # 바이러스에 감염된 pc가 없으므로 0으로 값 재설정
# print(visited)
print(cnt)