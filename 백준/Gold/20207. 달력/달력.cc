/*
20207. 달력

일정이 있는 곳에만 코팅지를 달력에 붙이려고 함
- 연속된 두 일자에 각각 일정이 1개 이상 있다면 일정이 연속되었다고 한다.
- 연속된 모든 일정은 하나의 직사각형에 포함되어야 한다.
- 연속된 일정을 모두 감싸는 가장 작은 직사각형의 크기만큼 코팅지를 오린다.

- 일정은 시작날짜와 종료날짜를 포함한다.
정렬 조건
	- 시작일이 가장 앞선 일정부터 차례대로 채워진다.
	- 시작일이 같을 경우 일정의 기간이 긴 것이 먼저 채워진다.
- 일정은 가능한 최 상단에 배치된다. -> 앞부터 채우기
- 일정 하나의 세로의 길이는 1이다.
- 하루의 폭은 1이다.

풀이:
1. 일정 정렬
2. 배열에 몇 개의 일정이 중복되었는지 값을 저장
3. 코팅지 면적 구하기
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int s, e;
int w, h;
int chart[1001] = { 0, };

bool cmp(pair<int, int> a, pair<int, int> b) {
	if (a.first == b.first)
		return a.second - a.first > b.second - b.first;
	return a.first < b.first;
}

int main() {
	cin >> n;
	vector<pair<int, int>> schedule;
	for (int i = 0; i < n; i++) {
		cin >> s >> e;
		schedule.push_back({ s, e });
	}

	// 1. 정렬(시작 일정이 빠른 거 -> 길이가 긴 거)
	sort(schedule.begin(), schedule.end(), cmp);

	// 2. 정렬된 녀석들 줄세우기
	int end = 0;
	for (int i = 0; i < n; i++) {
		for (int j = schedule[i].first; j <= schedule[i].second; j++) {
			chart[j]++;
			end = max(end, j);
		}
	}

	// 3. 넓이 구하기
	int flag = 0;
	w = 0; h = 0;
	int ans = 0;
	for (int i = 1; i <= end; i++) {
		if (!chart[i]) {
			// 계산할 일정이 있으면 계산하기
			if (flag) {
				ans += w * h;
				w = 0; h = 0;
				flag = 0;
			}
		}
		else {
			flag = 1;
			w++;
			h = max(h, chart[i]);
		}
	}
	ans += w * h;


	cout << ans << '\n';

	return 0;
}