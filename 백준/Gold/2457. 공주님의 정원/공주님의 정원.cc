/*
2457. 공주님의 정원

- 꽃은 모두 같은 해에 피어서 같은 해에 진다.
- 하나의 꽃은 피는 날과 지는 날이 정해져있다.
다음의 두 조건을 만족하는 꽃들을 선택하자
1. 공주가 가장 좋아하는 계절인 3 ~ 11월까지는 매일 꽃이 한 가지 이상 피어있도록 한다.
2. 정원이 넓지 않으므로 심는 꽃의 수를 최대한 적게 한다.

선택한 꽃들의 최소 개수 출력

풀이 : 
그리디하게 접근
N <= 100000 
날짜를 일로 통일하자. -> 계산해서 변환해주기
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define INIT cin.tie(0); ios::sync_with_stdio(false);

using namespace std;

int calendar[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
int total_days[13] = { 0, };
int n, sm, sd, em, ed;
vector<pair<int, int>> flowers;

pair<int, int> calc(int sm, int sd, int em, int ed) {
	int startSum = 0;
	int endSum = 0;
	// 출발일
	startSum += total_days[sm - 1] + sd - 1;
	endSum += total_days[em - 1] + ed - 1;

	return { startSum, endSum };
}

int main() {
	INIT;

	// 날짜 누적합 구하기
	for (int i = 1; i < 13; i++) {
		total_days[i] = total_days[i - 1] + calendar[i];
	}

	// 입력 받기
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> sm >> sd >> em >> ed;
		// 구한 누적합에 맞게 피는날, 지는날 구하기
		flowers.push_back(calc(sm, sd, em, ed));
	}

	// 3월 1일 이전 꽃들은 언제바뀌든지 상관없다. 그치만 이후로는 쭉 피어있어야 함
	// 꽃 정렬(시작날짜 빠른 순)
	sort(flowers.begin(), flowers.end());

	// 그리디 시작
	vector<pair<int, int>> ans;
	int start, end;
	pair<int, int> tmp = { 0, 0 };
	ans.push_back(flowers[0]);
	for (int i = 1; i < flowers.size(); i++) {
		start = flowers[i].first; end = flowers[i].second;
		// 11월 30일이 지난 경우, continue
		if (start > total_days[11]) continue;

		// 3월 1일이 지나지 않은 경우, 마지막날이 최대한 늦은 녀석으로 선택
		if (start < total_days[2] + 1) {
			if (ans.back().second < end) {
				ans.pop_back();
				ans.push_back({ start, end });
			}
		}
		else {
			// 무조건적으로 연결되어 있어야 한다.
			// 만약 마지막 녀석의 end보다 start가 더 크다면, tmp 업데이트 후 비교하기
			if (ans.back().second < start) {
				// tmp가 ans와 확실히 연결되는지 체크
				// 만약 연결되지 않는다면, 불가능한 경우임
				if (tmp.first > ans.back().second)
					break;
				// 연결되는 경우, 계속 진행
				ans.push_back(tmp);
				if (tmp.second < end)
					tmp = { start, end };
			}
			else {
				if (tmp.second < end)
					tmp = { start, end };
			}
		}
	}
	// tmp로 11월 30일이 결정되는지 확인
	if (ans.back().second >= tmp.first && ans.back().second < total_days[11] && tmp.second >= total_days[11]) {
		ans.push_back(tmp);
	}

	if (ans.front().first > total_days[2] || ans.back().second < total_days[11] || ans.back().second < total_days[3])
		cout << 0 << '\n';
	else
		cout << ans.size() << '\n';


	return 0;
}