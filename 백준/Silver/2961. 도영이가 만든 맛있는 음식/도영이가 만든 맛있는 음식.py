'''
재료 n개, 신맛 s와 쓴맛 b를 알고있음
음식의 신맛은 재료 신맛의 곱, 쓴맛은 합이다.

요리의 신맛과 쓴맛의 차이를 작게 만들고자 함
재료는 적어도 하나 사용하애함

풀이 :
재귀, 여러 음식 뽑아본 뒤, 최솟값으로 저장
'''

def dfs(depth, s, b):
    global ans
    if b:
        ans = min(ans, abs(s - b))
    for i in range(depth, n):
        if not selected[i]:
            selected[i] = 1
            dfs(depth + 1, s * ingredients[i][0], b + ingredients[i][1])
            selected[i] = 0
            
n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)
selected = [0] * n
dfs(0, 1, 0)

print(ans)