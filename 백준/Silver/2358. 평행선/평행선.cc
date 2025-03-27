/*
두 개 이상의 점을 지나면서 x/y 축에 평행한 직선 몇 갠지 찾아보자

풀이 : x 해시맵 y 해시맵 따로 만들어둔 뒤 모든 좌표 저장
이후,  x, y 돌면서 정답 없데이트
*/


#include <iostream>
#include <cstring>
#include <map>

using namespace std;

int n, r, c, ans = 0;
map<int, int> x, y;
map<pair<int, int>, int> coord;

int main() {
	cin >> n;
	for (int i = 0, r, c; i < n; i++) {
		cin >> r >> c;
		x[r]++;
		y[c]++;
	}

	for (auto coord : x) {
		if (coord.second >= 2) {
			ans++;
		}
	}
	for (auto coord : y) {
		if (coord.second >= 2) {
			ans++;
		}
	}
	cout << ans << '\n';
	return 0;
}