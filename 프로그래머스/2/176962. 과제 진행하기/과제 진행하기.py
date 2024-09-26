'''
- 과제는 시작하기로 한 시각에 시작
- 진행중인 과제가 있는 경우, 진행중인거 멈추고 새로운거 시작
- 진행중이던 과제를 끝냈을 떄, 이전에 멈춘 과제 있다면 이어서 진행
    - 과제를 끝낸 시간에 새로운 과제가 있다면, 새로운 과제 시작
- 멈춰둔 과제가 여러개인 경우, 최근에 멈춘 과제부터 진행(stack)

풀이:
plans <= 1000
0. 배열 분으로 변경 후 시간 순으로 정렬
1. 반복문 돌면서 stack의 마지막과 시간 비교
- 진행중인 과제가 끝나는 시각과 새로운 과제 시작 시간이 같다면, 진행중인건 끝났다고 판단
'''

def solution(plans):
    answer = []

    def calc(time):
        hour, min = map(int, time.split(':'))
        return hour * 60 + min

    # 0. 시간 분으로 재배치 & 시작 시간 순으로 정렬
    plans = sorted([[a, calc(b), int(c)] for a, b, c in plans], key=lambda x: x[1])

    print(plans)
    # 1. 시간 재기
    stack = []
    for i in range(len(plans) - 1):
        stack.append([plans[i][0], plans[i][2]])
        gap = plans[i + 1][1] - plans[i][1]

        while stack and gap:
            nowTime = stack[-1][1]  # 현재 과제의 소요시간

            if nowTime <= gap:  # 현재 과제의 소요시간이 다음 과제와의 시간차이보다 작다면! (다음과제 시간 전까지 끝낼 수 있다면)
                name, time = stack.pop()  # 스택에서 제거
                gap -= time  # 다음과제까지 남은 시간으로 계산
                answer.append(name)  # 과제완료!
            else:  # 다음 과제시간까지 못 끝내면
                stack[-1][1] -= gap  # 남은 과제 시간 저장
                gap = 0  # 다음과제 해야하니까 0

    # 2. 나머지 스케줄 순차적으로 진행
    answer.append(plans[-1][0])
    while stack:
        sub, st = stack.pop()
        answer.append(sub)

    return answer
