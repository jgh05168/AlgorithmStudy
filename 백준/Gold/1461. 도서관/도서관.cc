/*
도서관

사람들이 마구 놓은 책을 원래 자리에 둬야됨
- 세준이는 현재 0에 위치함
- 마구 놓은 책도 전부 0에 있음
- 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔두는 최소 걸음 수를 계산
책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다.

풀이:
n <= 50
위치 <= |10000|
정렬 후 그리디 알고리즘으로 해결하면 어떨까 ?
양수 음수 나누기
	- 둘 다 하나만 남았을 땐 어차피 0에 들러야한다
가까운 애들부터 놓기(처음에는 나누어 떨어지지 않는 수만큼 들기)
3개씩 끊어 계산했을 때 마지막 값이 더 작은 쪽부터 가져가기

*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m, tmp;

int main() {
	cin >> n >> m;
	vector<int> left_library, right_library;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		if (tmp > 0) right_library.push_back(tmp);
		else left_library.push_back(tmp);
	}

	// 각자 정렬하기
	sort(right_library.begin(), right_library.end());
	sort(left_library.begin(), left_library.end());

	// 가져가기 시작
	int ans = 0;
	int start = 0;
	int end = right_library.size() - 1;
	// 먼저 모든 스텝 확인해보기
	while (start + m < left_library.size()) {
		ans += abs(left_library[start] * 2);
		start += m;
	}
	while (end - m > -1) {
		ans += right_library[end] * 2;
		end -= m;
	}

	// 덜빠진 부분 생각하기
	if (start < left_library.size() && end >= 0)
		ans += (right_library[end] + abs(left_library[start])) * 2;
	else if (start < left_library.size() && end < 0)
		ans += abs(left_library[start]) * 2;
	else
		ans += right_library[end] * 2;

	// 가장 긴 부분은 값을 빼주어야한다(책을 다 정리하면 멈추기 때문)
	if (left_library.empty())
		ans -= right_library.back();
	else if (right_library.empty())
		ans -= abs(left_library[0]);
	else {
		// 둘 다 존재한다면 두 수 비교 후 큰 값 빼주기
		if (abs(left_library[0]) > right_library.back())
			ans -= abs(left_library[0]);
		else
			ans -= right_library.back();
	}

	cout << ans << '\n';

	return 0;
}