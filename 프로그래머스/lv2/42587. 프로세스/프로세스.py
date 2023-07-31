def solution(priorities, location):
    cnt = 0
    queue = [(idx, val) for idx, val in enumerate(priorities)]

    while 1:
        ans = queue.pop(0)
        if any(ans[1] < q_val[1] for q_val in queue):
            queue.append(ans)
        else:
            cnt += 1
            if ans[0] == location:
                return cnt


    return cnt