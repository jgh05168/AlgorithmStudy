'''
단품 메뉴들을 조합해서 코스요리
-> 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품 메뉴들로 구성
- 코스요리 메뉴는 최소 2가지 이상
- 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보

풀이:
음식 종류 해시맵 : 20 * (10C1 + ... + 10C10) = 20000
해시맵 별로 오름차순 해주기
'''

from collections import defaultdict

food_dict = defaultdict(int)


def solution(orders, courses):
    global food_dict
    answer = []

    def comb_menu(new_menu, target_depth, idx, course):
        global food_dict
        if len(new_menu) == target_depth:
            return
        else:
            if idx == len(course):
                return
            for i in range(idx, len(course)):
                if ''.join(new_menu + [course[i]]) in visited:
                    continue
                visited.add(''.join(new_menu + [course[i]]))
                food_dict[''.join(new_menu + [course[i]])] += 1
                comb_menu(new_menu + [course[i]], target_depth, i + 1, course)

    # 1. 음식 종류 해시맵
    for order in orders:
        order = sorted(list(order))
        visited = set()
        for i in range(len(order) - 1):
            visited.add(order[i])
            comb_menu([order[i]], len(order) - i, i + 1, order)

    comb_menu_list = defaultdict(list)
    # 2. 2명 이상의 손님에게서 주문된 음식 조합을 저장
    for key, value in food_dict.items():
        if value < 2 or len(key) not in courses:
            continue
        comb_menu_list[len(key)].append((key, value))

    for c in courses:
        if comb_menu_list[c]:
            comb_menu_list[c].sort(key=lambda x: x[1], reverse=True)

    print(comb_menu_list)
    for c in comb_menu_list.keys():
        if comb_menu_list[c]:
            answer.append(comb_menu_list[c][0][0])
            idx = 1
            cnt = comb_menu_list[c][0][1]
            tmp_n = len(comb_menu_list[c])
            while tmp_n > idx and comb_menu_list[c][idx][1] == cnt:
                answer.append(comb_menu_list[c][idx][0])
                idx += 1

    answer.sort()

    return answer
