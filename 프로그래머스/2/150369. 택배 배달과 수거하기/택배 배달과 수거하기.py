'''
모두 크기가 같은 상자 사용 & 빈 재활용 상자 수거
i 번째 집은 j번째 집과 j - i만큼 떨어져 있다.

- 트럭에는 cap개 상자를 실을 수 있음
- 각 집마다 배달 및 빈 상자의 개수를 알고 있다. -> 최소 이동 거리를 구하자
각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있습니다.

풀이:
- 뒤에서부터 idx를 게산한다.
- 배달이 불가능 할 경우, 거리 계산 후 박스 들/말 계산
    - 둘 다 0보다 작거나 같으면 박스를 더 들거나 수거할 수 있는 상태
    - 양수인 경우, 수거/배달 불가능한 상태이므로 거리 계산
'''
def solution(cap, n, deliveries, pickups):
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n - 1, -1, -1):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (i + 1) * 2

    return answer