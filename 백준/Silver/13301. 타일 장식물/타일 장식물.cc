#include <iostream>
#include <vector>
using namespace std;

int n;
long long dp[10010];


int main() {
	cin >> n;

	dp[1] = 1;
	dp[2] = 1;
	
	for (int i = 3; i <= n; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}

	cout << dp[n] * 2 + (dp[n]+dp[n - 1]) * 2;
}