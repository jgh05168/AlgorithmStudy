/*
조카들에게 최대한 긴 과자를 나눠주려고 함
- 모든 조카에게 같은 길이의 막대 과자를 나눠줘야 함

매개변수탐색
풀이 : 막대 길이를 매개변수로 둔다.
- 현재 인원들에게 길이(mid)의 막대과자를 줄 수 있는지 여부를 탐색
- 이후 길이 줄여나가기
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int m, n, tmp;
vector<int> v;

int main() {
	cin.tie(0); ios::sync_with_stdio(false);
	cin >> m >> n;
	int left = 1;
	int right = 0;
	int mid, ans=0;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		v.push_back(tmp);
		if (tmp > right) right = tmp;
	}

	// 이분탐색 시작
	while (left <= right) {
		mid = (left + right) / 2;

		int cnt = 0;
		for (int i = 0; i < v.size(); i++) {
			cnt += v[i] / mid;
		}

		// 만약 나눠줄 수 있는 인원보다 작다면 길이 줄이기
		if (cnt < m) {
			right = mid - 1;
		}
		else {
			ans = mid;
			left = mid + 1;
		}
	}

	cout << ans << '\n';
	return 0;
}