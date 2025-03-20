/*
해야할 일이 총 n개
최대한 늦게 일을 시작할 수 있는 시간을 찾자
일하는데 걸리는 시간, 마감기한 주어짐

풀이 : 정렬, 그리디
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int answer = 1000000000;
vector<pair<int, int>> schedule;

bool cmp(pair<int, int> a, pair<int, int> b) {
	if (a.second == b.second)
		return a.first < b.first;
	return a.second < b.second;
}

void init() {
	cin >> n;
	int a, b;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		schedule.push_back({ a, b });
	}
}

void solution() {
	// 마감시간 오름차순 정렬
	sort(schedule.begin(), schedule.end(), cmp);

	// 역순 스케줄링 시작
	int cur_time = schedule.back().second;
	for (int i = n - 1; i >= 0; i--) {
		cur_time = min(cur_time, schedule[i].second) - schedule[i].first;
	}

	// 만약 current_time이 음수면 0시부터 시작해도 불가능한 경우
	if (cur_time < 0)
		answer = -1;
	else
		answer = cur_time;
}

int main() {
	init();

	solution();

	cout << answer << '\n';

	return 0;
}
