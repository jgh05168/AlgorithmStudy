def solution(s):
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                answer = False
                break
            stack.pop(-1)
    
        if len(stack) == 0:
            answer = True
    
    if len(stack) != 0:
        answer = False
    
    return answer