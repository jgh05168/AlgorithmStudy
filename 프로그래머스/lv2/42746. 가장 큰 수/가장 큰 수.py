
def solution(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 4 ,reverse=True)       # sort / sorted 함수 사용 시 key = lambda x : 조건 을 사용하여 쉽게 정렬할 수 있다.


    return str(int(''.join(numbers)))





