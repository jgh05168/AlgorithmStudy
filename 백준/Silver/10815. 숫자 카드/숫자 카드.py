'''
숫자카드 n개

정수 m개 적혀있을 때 상근이가 갖고있는지 아닌지 판단.

[풀이]
이미 있는 카드는 정렬
구해야 할 카드는 처음부터 이분탐색 해보기
'''

import sys
input = sys.stdin.readline

def bin_search(start, end, card):
    # 종료조건
    if start >= end:
        ans.append(0)
        return

    mid = (start + end) // 2
    if card == cards[mid]:
        ans.append(1)
        return
    elif card < cards[mid]:
        bin_search(start, mid, card)
    else:
        bin_search(mid + 1, end, card)


n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
calc_cards = list(map(int, input().split()))

ans = []
for card in calc_cards:
    bin_search(0, n, card)

print(*ans)