'''
n개의 빌딩
i번째 빌딩의 키가 h, 모든 빌딩은 오른쪽만 볼 수 있다.
관리인이 옥상을 확인할 수 있는 총 수를 구하자

풀이:
뒤에서부터 진행하기 : 마지막 관리인은 아무것도 보지 못함
- 현재 건물 관리인보다 작을 때까지 pop하며 개수 추가해주기
-------------------------------------틀림
스택에는 건물의 내림차순 정보를 저장해주도록 하자
해당 건물이 높이가 작으면 stack에서 pop
크면 스탑해고 해당 건물을 스택에 추가

'''

import sys
input = sys.stdin.readline

n = int(input())
buildings = []
for _ in range(n):
    buildings.append(int(input()))

stack = []
ans = 0
for i in range(n):
    tmp = 0
    while stack and stack[-1] <= buildings[i]:
        stack.pop()
    stack.append(buildings[i])
    ans += len(stack) - 1

print(ans)