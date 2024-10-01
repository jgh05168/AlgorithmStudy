'''
n 덩어리의 고기를 이미 잘라놓고 판매중 = 이미 정해진 무게와 가격이 있음
    - 어떤 덩어리를 샀을 땐, 그 덩어리보다 싼 고기들은 덤으로 얻을 수 있음
    - 각 고기들은 비용과 무게와의 관계가 서로 비례하지 않을 수 있음
어느 부위든 자신이 원하는 양만 구매하면 된다고 함
가격이 더 싸면 필요한 양보다 더 살 수도 있음

풀이:
1. 해시맵 기준 몇 개의 조합이 있는지 확인
2. set으로 중복 제거
3. 덩어리 순으로 정렬
4. 무게 누적해서 더해주기
'''

from collections import defaultdict

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
meats = [tuple(map(int, input().split())) for _ in range(n)]

price_dict = defaultdict(int)

# 1. 가격별 해시맵 생성
for price in meats:
    price_dict[price] += 1

# 2. set으로 중복 제거
meats = list(set(meats))

# 3. 가격 작은 순으로 정렬
meats.sort(key=lambda x: (x[1], -x[0]))

# 4. 무게 누적해서 더해주기
# 가격별 min 무게 찾아놓기
# 무게 넘어가는 순간부터 min으로 측정하기
ans = float('inf')
tmp_w = 0
cur_cost = 0
get_cnt = 1
for i in range(len(meats)):
    flag = 0
    if meats[i][1] != cur_cost:
        get_cnt = 1  # 같은 가격대가 아니라면 업데이트 해주기
    else:
        get_cnt += 1

    tmp_w += meats[i][0]
    if tmp_w >= m and meats[i][1] >= cur_cost:
        ans = min(ans, meats[i][1] * get_cnt)
        flag = 1
    else:
        cur_cost = meats[i][1]
    price_dict[meats[i]] -= 1

    # 같은 가격대가 여러개 있는 경우
    if price_dict[meats[i]] and not flag:
        while price_dict[meats[i]]:
            tmp_w += meats[i][0]
            get_cnt += 1
            if tmp_w >= m and meats[i][1] >= cur_cost:
                ans = min(ans, meats[i][1] * get_cnt)
            cur_cost = meats[i][1]
            price_dict[meats[i]] -= 1



if ans == float('inf'):
    print(-1)
else:
    print(ans)
