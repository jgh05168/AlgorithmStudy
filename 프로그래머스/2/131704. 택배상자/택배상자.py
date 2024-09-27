'''
1 ~ n번까지 택배상자, 벨트는 한 방향으로 진행 가능(벨트에 놓인 순서대로)
택배 기사님이 미리 순서를 알려줌
    - 현재 실어야하는 택배가 아닌 경우, 다른 보조 상자에 보관
    - 보조컨테이너는 앞뒤로 이동이 가능. stack
    - 이걸 써도 원하는 순서대로 쌓지 못하면 상자쌓기 그만.

풀이:
stack
초기 상자들 다 넣어두고 시작
'''

def solution(order):
    answer = 0
    # 1. 미리 보조컨테이너에 옮겨두고 시작
    stack = []
    for i in range(1, order[0]):
        stack.append(i)
    
    main_box = order[0]
    for box in order:
        if main_box == box:
            answer += 1
            main_box += 1
        else:
            # 현재 박스보다 배달갈 박스가 더 크다면,
            if main_box < box:
                for j in range(main_box, box):
                    stack.append(j)
                answer += 1
                main_box = box + 1
            elif stack and stack[-1] == box:
                stack.pop()
                answer += 1
            elif not stack:
                stack.append(box)
            else:
                break

    return answer