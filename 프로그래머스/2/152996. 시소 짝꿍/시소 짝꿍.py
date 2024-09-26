from collections import defaultdict

def solution(weights):
    answer = 0
    
    # 1. 중복되는 몸무게 계산
    weight_dict = defaultdict(int)
    for weight in weights:
        weight_dict[weight] += 1
    
    # 중복된 몸무게 조합 계산
    for key, value in weight_dict.items():
        if value > 1:
            answer += (value * (value - 1)) // 2
    
    # 2. 무게 비율에 따른 계산 (2:3, 3:4, 1:1)
    ratio_dict = defaultdict(int)
    for weight in weights:
        # 2:3 비율 처리
        ratio_dict[weight * 2 / 3] += 1
        # 3:4 비율 처리
        ratio_dict[weight * 3 / 4] += 1
        # 1:2 비율 처리
        ratio_dict[weight * 1 / 2] += 1
    
    # 비율이 맞는 조합의 수 더하기
    for weight in weights:
        if weight in ratio_dict:
            answer += ratio_dict[weight]
    
    return answer
