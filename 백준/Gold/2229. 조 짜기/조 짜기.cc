/*
가급적 실력차이가 많이 나도록 조를 편성
- 각 조가 잘 짜여진 정도 : 높은 점수와 낮은 점수의 차
- 조가 한 명으로 구성되는 경우, 잘짜여진 정도는 0
- 전체적으로 잘짜여진 정도 : 각 조의 점수의 총합

전체적으로 잘짜여진 정도의 최댓값 구하기

*/

#include <iostream>
#include <algorithm>

using namespace std;

int dp[1002] = { 0, };
int n;
int students[1002] = { 0, };

int main() {
	cin >> n;
	int tmp;
	for (int i = 1; i < n + 1; i++) {
		cin >> tmp;
		students[i] = tmp;
	}

	// dp 시작
	for (int i = 2; i <= n; i++) {
		int tmp_max = dp[i - 1];
		int diff = 0;
		for (int j = i - 1; j > 0; j--) {
			diff = max(diff, abs(students[i] - students[j]));
			tmp_max = max(tmp_max, dp[j - 1] + diff);
		}
		dp[i] = tmp_max;
	}

	cout << dp[n] << '\n';


	return 0;
}