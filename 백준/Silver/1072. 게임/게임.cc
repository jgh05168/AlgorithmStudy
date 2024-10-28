/*
1072. 게임

형택이는 모든 게임에서 지지 않는다.
이전 기록떄문에 현재 실력 증명이 안된다고 생각함.

- 게임 횟수 : X
- 이긴 게임 : Y(z%)
z는 형택이 승률이다. Y / X * 100

X, Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하기

풀이:
X <= 1000000000이기 때문에, 완탐 시도하면 시간초과난다.
: 이분탐색으로 문제 해결하기
- 게임은 항상 이기기 떄문에 X와 Y가 점진적으로 증가한다.
- z가 변하기만 하면 된다.

left : 0
right : 남은 게임 수
*/

#include <iostream>
#include <algorithm>
#define lli long long int

using namespace std;

lli x, y, z;
lli ans = 1000000000;

int main() {
	cin >> x >> y;
	z = y * 100 / x;

	// 시작하지 못하는 경우
	if (z >= 99) {
		cout << -1 << '\n';
		return 0;
	}
	
	// 이분탐색 
	lli left = 0;
	lli right = 1000000000;
	lli new_z, mid;

	while (left <= right) {
		mid = (left + right) / 2;
		// 새로운 z 구하기
		new_z = (y + mid) * 100 / (x + mid);
		// 게임 수 늘리기
		if (z >= new_z)
			left = mid + 1;
		else {
			right = mid - 1;
			ans = mid;
		}
	}

	cout << ans << '\n';

	return 0;
}