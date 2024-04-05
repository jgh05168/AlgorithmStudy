def solution(s):
    
    answer = [0, 0]
    while s != "1":
        total_len = len(s)
        new_s = len(''.join(s.split("0")))
        answer[0] += 1
        answer[1] += total_len - new_s
        s = ''.join(list(bin(int(new_s)))[2:])
    return answer