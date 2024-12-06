'''
1. 징검다리는 일렬로 놓여있고, 각 징검다리 디딤돌에는 숫자가 젹혀있으며, 밟을때마다 1씩 줄어든다
2. 숫자가 0이되면 더이상 밟을 수 없음. 이때는 그 다음 디딤돌로 여러칸 건너 뛸 수 있음
    - 무조건 다음 중 가까운 칸으로 건넌다.

stones <= 200000
풀이:
정렬하면 안된다.
이분탐색으로 풀이 가능할듯 ?
left = 1, right = max(stones)
건너면서 돌멩이 없어지는 경우에 cnt += 1 진행
'''

def solution(stones, k):
    answer = 0
    n = len(stones)
    
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2    # 사람 수
        cnt = 0     # 현재 망가진 웅덩이 개수
        for i in stones:
            if i - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            # 효율성 통과를 위한 break(임계값 k를 넘어가면 굳이 뒤에 부분 체크할 필요 없음)
            if cnt >= k:
                break
        if cnt >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

