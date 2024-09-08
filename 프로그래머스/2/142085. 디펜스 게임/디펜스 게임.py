'''
보유한 병사 n명으로 적의 공격을 막는 게임
- 매 라운드마다 enemy[i]마리의 적이 등장
- 남은 병사 중 적의 수 만큼을 소모하여 적을 막을 수 있음
    - ex) n = 5, enemy[i] = 2 -> 남은 병사 = 3
    - 남은 병사의 수가 더 적으면 게임 종료
- 무적권을 사용하여 병사 소모 없이 막을 수 있음
    - 총 k번 사용 가능함
n <= 10**9
k <= 500000
enemy의 길이 <= 1000000
막을 수 있는 라운드 출력

풀이:
몰려오는 병사는 정렬하면 안된다.(순서 정해져있음)
1. 일단 for문 돌면서 병사의 수 체크
2. 이후, 우선순위 큐의 라운드에 도착하면 무적권 사용. 아니면 n 사용
    - 만약 n이 적보다 적은 경우, 그냥 무적권 사용
------------ 접근 방식이 틀림 ---------------
이건 맞는 접근 방식 :

적의 수(e)를 최대힙 자료구조(heap)에 음수형식으로 저장한다.
적의 전체 수(sumEnemy)에 적의 수(e)를 누적으로 더한다.
만약 적의 전체 수(sumEnemy)가 보유한 병사(n)보다 많을 경우
무적권(k)도 존재하지 않는다면 더 이상 라운드를 진행할 수 없다(break).
최대힙 자료구조(heap)에서 지금까지 진행해온 라운드 중 적이 가장 많은 라운드를 찾아서(heappop) 적의 전체 수(sumEnemy)의 값을 차감하고, 무적권(k)의 수도 1 만큼 차감한다.
'''

import sys, heapq
input = sys.stdin.readline


def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []

    for e in enemy:
        # 일단 최대 힙으로 모든 적군 정보 저장
        heapq.heappush(heap, -e)
        # 지금까지 마주한 적군의 수를 계산해준다.(무적권 사용 여부를 판단)
        sumEnemy += e
        # 무적권이 필요할 때마다 돌려막기 진행
        if sumEnemy > n:
            if k == 0:
                break
            sumEnemy += heapq.heappop(heap)
            k -= 1
        answer += 1
    return answer