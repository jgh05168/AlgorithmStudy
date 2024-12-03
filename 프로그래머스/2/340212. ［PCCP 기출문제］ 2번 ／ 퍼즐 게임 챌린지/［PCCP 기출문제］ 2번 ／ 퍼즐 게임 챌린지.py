'''
n개의 퍼즐을 제한 시간 내에 풀어야함
난이도와 소요시간 주어짐
숙련도(level)에 따라 틀리는 횟수가 바뀜

diff <= level이면 퍼즐을 틀리지 않고 cur만큼의 시간을 사용해 해결
else, 퍼즐을 diff - level번 틀린다. 
    - 틀릴 때마다 time_cur 만큼의 시간을 사용함
    - time_prev 만큼의 시간을 사용해 이전 퍼즐을 다시 풀고와야 함
        - 이전 퍼즐을 다시 풀 떄는 틀리지 않는다.
    - 틀린 이후에 다시 퍼즐을 풀면 time_cur 만큼의 시간을 사용하여 해결한다.
    == (diff - level) x (time_cur + time_prev) + time_cur

제한시간 내 퍼즐을 모두 해결하기 위한 숙련도의 최솟값 구하기
n <= 300000
- for문을 사용해 접근하는 경우, 모든 limit까지의 경우를 탐색해야 하기 때문에 시간초과가 난다.
-> 이분탐색적으로 접근

'''

def solution(diffs, times, limit):
    answer = 0
    n = len(diffs)
    
    left, right = diffs[0], max(diffs)
    answer = right
    
    while left <= right:
        level = (left + right) // 2
        tmp = limit
        for i in range(n):
            if diffs[i] <= level:
                tmp -= times[i]
            else:
                tmp -= ((diffs[i] - level) * (times[i] + times[i - 1]) + times[i])
        # 이분탐색 체크해주기
        if tmp < 0:
            left = level + 1
        else:
            answer = min(answer, level)
            right = level - 1
    
    return answer