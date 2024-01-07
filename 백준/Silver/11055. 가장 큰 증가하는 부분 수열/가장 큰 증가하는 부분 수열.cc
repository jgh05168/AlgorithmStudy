#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	cin >> n;
	int arr[1001] = { 0, };
	int i = 0;
	int dp[1001] = { 0, };

	for (i = 0; i < n; i++) {
		cin >> arr[i];
	}

	int ans = arr[0];

	for (i = 0; i < n; i++) {
		dp[i] = arr[i];
		for (int j = 0; j < i; j++) {
			if (arr[j] < arr[i]) {	// 이전 값들이 현재 값보다 작은 경우만 업데이트
				dp[i] = max(dp[i], dp[j] + arr[i]);
			}
			ans = max(ans, dp[i]);
		}
	}


	cout << ans;

	return 0;
}