'''
n개의 집에 택배 배달 가려고 한다.
배달 다니면서 빈 택배상자들 수거
트럭에는 재활용 택배상자를 최대 cap개 실을 수 있음

각 집마다 배달할 택배상자 개수와 수거 개수를 알고있을 때, 최소이동거리 구하기

풀이:
돌아오는 거리는 최대한 먼 곳 x 2이다.
n - 1부터 계산해보기, 택배상자의 개수를 cap만큼 미리 체크해야된다.
n <= 100000이므로 원트에 끝내야 됨
배달과 수거 인덱스를 따로 생각해주기
'''

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 뒤에서부터 돌아보기
    dval, pval = 0, 0
    for idx in range(n - 1, -1, -1):
        dval += deliveries[idx]
        pval += pickups[idx]
        
        
        # cap만큼 더 담을 수 없는 경우, answer 계산 후 cap만큼 빼주기
        while dval > 0 or pval > 0:
            dval -= cap
            pval -= cap
            answer += (idx + 1) * 2
        
    
    return answer