
def bfs(s):
    visited = [0] * 101
    queue = []
    queue.append(s)
    visited[s] = 1
    visit_cnt = 0


    while queue:
        v = queue.pop(0)
        if v in adj_l.keys():
            for w in adj_l[v]:
                if visited[w] == 0:
                    queue.append(w)
                    visited[w] = visited[v] + 1
                    if visit_cnt < visited[w]:
                        visit_cnt = visited[w]

    val = 0
    for idx in range(len(visited)):
        if visited[idx] == visit_cnt and val < idx:
            val = idx

    return val

for tc in range(1, 11):
    length, s_node = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_l = {}

    for i in range(len(arr) // 2):
        a, d = arr[i * 2], arr[i * 2 + 1]
        if a in adj_l.keys():
            adj_l[a].append(d)
        else:
            adj_l.update({a: [d]})

    print(f'#{tc} {bfs(s_node)}')

