'''
과제마다 마감일이 존재한다.
과제마다 끝났을 떄 얻을 수 있는 점수 존재. 마감일이 지나면 점수를 받을 수 없음
- 많이 받을 수 있는 점수의 최댓값

풀이:
하루에 한 과제씩 끝낼 수 있다
우선순위큐 사용
- 길이 = 마감기한
- 만약 마감기한을 넘는데, 점수가 더 크다 ? 맨 앞 녀석과 비교
- n < 1000이기 때문에 한 번 더 반복문 돌아도 가능함
'''

import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[1], x[0]))

pq = []
due_date_list = [0] * 1001
for i in range(n):
    flag = 0
    day, value = arr[i]


    # 앞에 몇명있는지 판단하기
    if not due_date_list[day]:
        heapq.heappush(pq, (day, value))
        due_date_list[day] = 1
        continue

    # 앞에 빈자리 있는지 체크 후 넣기
    for j in range(day, 0, -1):
        if not due_date_list[j]:
            heapq.heappush(pq, (day, value))
            due_date_list[j] = 1
            break
    # 앞에 빈자리 없다면, 이미 있는애 자리 먹기
    else:
        # 첫번째 녀석과 비교
        init_day, init_value = heapq.heappop(pq)
        if init_value < value:
            heapq.heappush(pq, (day, value))
        else:
            heapq.heappush(pq, (init_day, init_value))


print(sum(i[1] for i in pq))

