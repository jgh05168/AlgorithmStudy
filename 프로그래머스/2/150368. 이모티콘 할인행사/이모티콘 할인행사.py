'''
이모티콘 플러스 서비스 가입자 수를 늘리려고 함
목표 우선순위 : 
1. 서비스 가입자 최대
2. 판매액 최대

n명에게 이모티콘 m개를 할인하여 판매
이모니콘 별 할인율은 다름

이모티콘 사거나 서비스 가입 기준
- 자신의 기준에 따라 일정 비율 이상 할인하는 이모니콘 모두 구매
- 구매 비용의 합이 일정 가격 이상이 된다면 구매 모두 취소 후 서비스에 가입

풀이법 : 완전탐색, 백트래킹
이모티콘마다 할인율은 다를 수 있음 & 할인율은 총 4개 중 하나로 설정
=> 할인율과 이모티콘 가격 배열 만들어놓기
'''

def solution(users, emoticons):
    
    def dfs(depth, e, m):
        if depth == m:
            discount_emoticons.append(e)
            return
        else:
            for rate in [10, 20, 30, 40]:
                tmp_cost = emoticons[depth] * (100 - rate) // 100
                dfs(depth + 1, e + [(rate, tmp_cost)], m)

                
    answer = [0, 0]
    n = len(users)
    m = len(emoticons)
    # 할인율 -> 사람 -> 이모티콘
    
    discount_emoticons = []
    dfs(0, [], m)
    
    # 이제 돌면서 선택해보기
    for idx in range(len(discount_emoticons)):
        tmp_service = 0
        tmp_amount = 0
        for user in range(n):
            discount_rate, budget = users[user]
            tmp = 0
            for rate, emoticon in discount_emoticons[idx]:
                if discount_rate > rate:
                    continue
                tmp += emoticon
                if tmp >= budget:
                    tmp_service += 1
                    break
            else:
                tmp_amount += tmp
        if tmp_service > answer[0]:
            answer = [tmp_service, tmp_amount]
        elif tmp_service == answer[0]:
            answer = [tmp_service, max(tmp_amount, answer[1])]
        
    
    return answer