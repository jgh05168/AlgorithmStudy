/*
돌 이동 조건

1. 항상 오른쪽
2. i -> j 시, (j - i) x (|Ai - Aj| + 1)
3. 한 번 건너갈 때마다 쓸 수 있는 최대 힘은 K이다.

n^2 = 2500000
*/

#include <iostream>

using namespace std;

int n, k;
int arr[5001];
int dp[5001] = { 0, };

int main() {
	cin >> n >> k;
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	dp[0] = 1;
	for (int i = 0; i < n; i++) {
		if (!dp[i])
			continue;
		for (int j = i + 1; j < n; j++) {
			int power = (j - i) * (abs(arr[i] - arr[j]) + 1);
			if (power > k)
				continue;
			dp[j] = 1;
		}
	}

	if (dp[n - 1])
		cout << "YES" << '\n';
	else
		cout << "NO" << '\n';
}