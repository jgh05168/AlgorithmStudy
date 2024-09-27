'''
수확한 귤 중 k개를 골라 상자에 담기
귤을 크기별로 분류했을 때, 서로 다른 종류의 수를 최소화

풀이:
해시맵 사용하여 귤 크기별로 개수를 센다
k개만큼 담기
'''

from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    
    tangerine_dict = defaultdict(int)
    for t in tangerine:
        tangerine_dict[t] += 1
    
    tangerines = sorted(list(zip(tangerine_dict.keys(), tangerine_dict.values())), key=lambda x: x[1], reverse=True)
    
    tmp = 0
    for key, value in tangerines:
        answer += 1
        tmp += value
        if tmp >= k:
            break
    
    
    return answer