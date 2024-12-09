import sys
sys.setrecursionlimit(10**8)


def dfs(node,prv):
    for nxt in relation[node]:
        if nxt == prv:
            continue
        parent[nxt] = node
        dfs(nxt, node)


n = int(input())
relation = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
child = [[] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
child_num = [1 for _ in range(n+1)]

# 입력
for i in range(n-1):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

# 출력
dfs(1, 0)

for answer in parent[2:]:
    print(answer)
