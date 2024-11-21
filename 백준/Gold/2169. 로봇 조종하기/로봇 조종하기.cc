/*
왼쪽, 오른쪽, 아래쪽으로는 이동 가능
한 번 탐사한 지역을 다시 탐사하지는 않음

풀이:
DP
먼저 오른쪽으로 이동해가면서 더하기
그다음, 왼쪽으로 이동해가면서, 최댓값으로 업데이트해주기
	- 먼저 계산한다음 오른쪽에서 온 값과 비교
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m;
int arr[1001][1001];
int dp[1001][1001] = { 0, };

int main() {
	cin >> n >> m;
	vector<int> right(m + 1);
	vector<int> left(m + 1);
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < m + 1; j++)
			cin >> arr[i][j];
	}

	// 0. 첫번째 줄 초기화
	dp[1][1] = arr[1][1];
	for (int i = 2; i < m + 1; i++)
		dp[1][i] = dp[1][i - 1] + arr[1][i];

	// 1. DP 시작
	for (int i = 2; i < n + 1; i++) {
		// 왼쪽 오른쪽 나눠서 계산한 뒤에 합치기
		right[1] = dp[i - 1][1] + arr[i][1];
		left[m] = dp[i - 1][m] + arr[i][m];

		// 2. 오른쪽부터 먼저 채우기
		for (int j = 2; j < m + 1; j++)
			right[j] = max(right[j - 1], dp[i - 1][j]) + arr[i][j];
		// 3. 왼쪽 값 채우기
		for (int j = m - 1; j > 0; j--)
			left[j] = max(left[j + 1], dp[i - 1][j]) + arr[i][j];
		// 4. dp테이블 최댓값으로 업데이트
		for (int j = 1; j < m + 1; j++)
			dp[i][j] = max(left[j], right[j]);

		// 5. left, right 초기화
		for (int i = 1; i < m + 1; i++) {
			right[i] = 0;
			left[i] = 0;
		}
	}

	cout << dp[n][m] << '\n';

	return 0;
}