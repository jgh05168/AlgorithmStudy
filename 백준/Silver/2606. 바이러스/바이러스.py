V = int(input())
E = int(input())

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

graphs = {}
visited = [False] * (V + 1)
for _ in range(E):
    v, w = map(int, input().split())
    if v in graphs.keys():
        graphs[v].append(w)
    else:
        graphs.update({v:[w]})
    if w in graphs.keys():
        graphs[w].append(v)
    else:
        graphs.update({w:[v]})



for key in graphs.keys():
    if key == 1:
        dfs(key)

cnt = - 1
for val in visited:
    if val == True:
        cnt += 1
if visited[1] == False:
    cnt = 0
# print(visited)
print(cnt)