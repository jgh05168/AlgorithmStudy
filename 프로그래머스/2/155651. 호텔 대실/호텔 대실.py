'''
최소한의 객실을 사용하여 예약 손님 받기
한 번 사용한 객실은 퇴실시간 기준 10분 청소를 함

n < 1000

풀이:
그리디
1. 퇴실 시간을 기준으로 정렬
마지막 타임을 비교한 배열을 생성하여 채워넣어주기
'''

import sys
input = sys.stdin.readline

def solution(book_time):
    n = len(book_time)
    answer = []
    
    def change_min(str_time: str) -> int:
        return int(str_time[0:2]) * 60 + int(str_time[3:])
	
    book_times = sorted([[change_min(i[0]), change_min(i[1]) + 10] for i in book_time])
    
    
    for i in range(n):
        check_in = book_times[i][0]
        check_out = book_times[i][1]
        # 아직 아무도 입실을 안했다면 넣기
        if not answer:
            answer.append([check_in, check_out])
        # 누가 입실했다면,
        else:
            # 비교과정
            for j in range(len(answer)):
                reserve_in, reserve_out = answer[j]
                # 입실이 가능한 경우에만 입실시키기
                if reserve_out <= check_in:
                    answer[j] = [check_in, check_out]
                    break
            # 입실이 불가능하다면, 새 방 배정
            else:
                answer.append([check_in, check_out])
                
    return len(answer)