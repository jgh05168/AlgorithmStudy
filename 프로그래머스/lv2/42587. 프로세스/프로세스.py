def solution(priorities, location):
    cnt = 0
    queue = [(idx, val) for idx, val in enumerate(priorities)]

    while 1:
        ans = queue.pop(0)
        # any : iterable 한 반복문 중 단 하나라도 참인 값이 존재한다면, True를 반환
        if any(ans[1] < q_val[1] for q_val in queue):
            queue.append(ans)
        else:
            cnt += 1
            if ans[0] == location:      # location과 ans의 인덱스 넘버가 같은지 확인
                return cnt              # 같으면 횟수를 바로 return


    return cnt