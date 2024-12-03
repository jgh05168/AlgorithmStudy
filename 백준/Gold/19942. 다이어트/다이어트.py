'''
식재료 n개 중 몇 개 선택하여 영양분이 일정 이상이여야 함
조건을 만족하면서, 비용이 최소가 되는 선택을 하고자 함

최저 영양소 기준을 만족하는 최소 비용 식재료 집합

풀이 : 백트래킹
-> 가지치기 필요함 : 가지치기 안하면 14!이므로 무조건 시간초과다
1. 값이 ans보다 커지면 리턴
2. 최소 영양성분을 충족했다면 리턴
'''

def dfs(depth, idx, p, f, s, v, total_v, ingredient_list):
    global ans, ans_list
    if total_v >= ans:
        return
    if depth > n:
        return
    if p >= nutrition[0] and f >= nutrition[1] and s >= nutrition[2] and v >= nutrition[3]:
        ans = total_v
        ans_list = ingredient_list
        return
    for i in range(idx, n):
        if not selected[i]:
            if not sum(table[i][:-1]):
                continue
            selected[i] = 1
            dfs(depth + 1, i + 1, p + table[i][0], f + table[i][1], s + table[i][2], v + table[i][3], total_v + table[i][4], ingredient_list + [i + 1])
            selected[i] = 0


n = int(input())
nutrition = list(map(int, input().split()))
table = [list(map(int, input().split())) for _ in range(n)]
selected = [0] * n

ans = int(1e9)
ans_list = []

dfs(0, 0, 0, 0, 0, 0, 0, [])
if ans == int(1e9):
    print(-1)
else:
    print(ans)
    print(*ans_list)