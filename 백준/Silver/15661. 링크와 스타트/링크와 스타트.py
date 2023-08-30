# import sys
# input = sys.stdin.readline
#

def calc(team):
    # print(team)
    val = 0
    for i in range(len(team) - 1):
        for j in range(i + 1, len(team)):
            # print(team[i], team[j])
            val += arr[team[i]][team[j]] + arr[team[j]][team[i]]

    return val


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
people = [i for i in range(N)]
min_val = 100000000000


for i in range(1, (1 << N) // 2):
    start = []
    link = []
    # 부분집합 각각에 대해서 팀을 나눠줘야한다.
    for j in range(N):
        if i & (1 << j):
            start.append(people[j])     # 부분집합인 경우
        else:
            link.append(people[j])      # 부분집합이 아닌 경우

    # 순열을 사용해서 start와 link 각각의 능력치를 구해주기기
    if len(start) == 1:
        start_v = 0
        link_v = calc(link)
    elif len(link) == 1:
        start_v = calc(start)
        link_v = 0
    else:
        start_v = calc(start)
        link_v = calc(link)

    if min_val > abs(start_v - link_v):
        min_val = abs(start_v - link_v)

print(min_val)