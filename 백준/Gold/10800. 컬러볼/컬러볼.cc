/*
각 플레이어는 특정한 색과 크기를 가진 공을 하나 조종함
목표 : 자기 공보다 크기가 작고 색이 다른 공을 잡아, 그 크기만큼 점수를 얻는 것
- 본인의 공의 색과 크기는 변하지 않음

각 플레이어가 사로잡을 수 있는 모든 공들의 크기의 합을 출력하자.

풀이 : 
N <= 20만
O(n) / O(nlogn) 으로 풀어내야함. 완탐 불가능
조건 : 같은 색 공들은 배제해야함, 

그냥 전처리 해야할듯 ?
크기별로 같은 녀석들 몇 개 있는지 체크. 나랑 같은 색이 몇 개 있는지 체크하는 배열을 생성하기. 
누적합 사용 ?
*/

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int n, c, s, m = 0;
vector<pair<int, pair<int, int>>> color_balls;
int DAT[200001] = { 0, };
int prefixSum[200001] = { 0, };

bool cmp(pair<int, pair<int, int>> a, pair<int, pair<int, int>> b) {
	if (a.second.second == b.second.second) {
		if (a.second.first == b.second.first)
			return a.first < b.first;
		return a.second.first < b.second.first;
	}
	return a.second.second < b.second.second;
}

void init() {
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> c >> s;
		color_balls.push_back({ i, {c, s} });
		DAT[s] += 1;
		m = max(m, s);
	}

	// 누적합 진행
	for (int i = 1; i < m; i++) {
		if (DAT[i] > 0)
			prefixSum[i] += i * DAT[i];
		prefixSum[i] += prefixSum[i - 1];
	}
	memset(DAT, 0, sizeof(DAT));

	// 정렬
	sort(color_balls.begin(), color_balls.end(), cmp);
}


void simulation() {
	vector<pair<int, int>> ans;
	for (int i = 0; i < n; i++) {
		int cnt_ball = prefixSum[color_balls[i].second.second - 1] - DAT[color_balls[i].second.first] > 0 ? prefixSum[color_balls[i].second.second - 1] - DAT[color_balls[i].second.first] : 0;
		if (i > 0 && color_balls[i].second == color_balls[i - 1].second)
			cnt_ball = ans.back().second;
		ans.push_back({ color_balls[i].first, cnt_ball });
		DAT[color_balls[i].second.first] += color_balls[i].second.second;
	}
	sort(ans.begin(), ans.end());

	for (int i = 0; i < n; i++) {
		cout << ans[i].second << '\n';
	}
}


int main() {
	init();

	simulation();

}