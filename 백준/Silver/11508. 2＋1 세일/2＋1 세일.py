'''
- 가장 싼 것 무료로 지불, 나머지는 제품 가격만 지불
- 한 번에 3개의 유제품을 사지 않는 다면 할인 없이 정가 지불

(큰 작 작) (큰 작 작) (작 작) 이런 식이 최소비용이 된다.

오름차순 정렬 후 뒤에서부터 pop하며 가장 싼 비용 제외 나머지 비용들을 더한다.
'''


import sys
input = sys.stdin.readline

deck = []
n = int(input())
for _ in range(n):
    deck.append(int(input()))

deck.sort()

min_val = 0
while len(deck) >= 3:
    for _ in range(2):
        min_val += deck.pop()
    deck.pop()
min_val += sum(deck)

print(min_val)

