/*
부피가 A, B, C인 세 개의 물통이 있음
첫 번째 물통이 비어 있을 때, 세 번째 물통에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오

풀이 : DP
담겨있을 수 있는 물의 양을 구하는 것임
	 - 경우의 수 체크한 다음
3차원 DP로 풀이하기
*/

#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int a, b, c;
int dp[201][201][201];

bool isValid(int x, int n) {
	return 0 <= x && x <= n;
}

void topDown(int i, int j, int k) {
	if (!isValid(i, a) || !isValid(j, b) || !isValid(k, c))
		return;
	if (dp[i][j][k] != -1)
		return;

	dp[i][j][k] = 1;
	
	int remain;
	// i 기준
	remain = b - j;
	if (i > remain) {
		topDown(i - remain, b, k);
	}
	else
		topDown(0, i + j, k);
	remain = c - k;
	if (i > remain) {
		topDown(i - remain, j, c);
	}
	else
		topDown(0, j, i + k);

	// j 기준
	remain = a - i;
	if (j > remain) {
		topDown(a, j - remain, k);
	}
	else
		topDown(i + j, 0, k);
	remain = c - k;
	if (j > remain) {
		topDown(i, j - remain, c);
	}
	else
		topDown(i, 0, j + k);

	// k 기준
	remain = a - i;
	if (k > remain) {
		topDown(a, j, k - remain);
	}
	else
		topDown(i + k, j, 0);
	remain = b - j;
	if (k > remain) {
		topDown(i, b, k - remain);
	}
	else
		topDown(i, j + k, 0);
}

int main() {
	cin >> a >> b >> c;
	memset(dp, -1, sizeof(dp));

	topDown(0, 0, c);

	vector<int> answer;

	for (int i = 0; i < b + 1; i++) {
		for (int j = 0; j < c + 1; j++) {
			if (i + j == c && dp[0][i][j] != -1)
				answer.push_back(j);
		}
	}

	sort(answer.begin(), answer.end());
	for (auto ans : answer)
		cout << ans << ' ';
	
	return 0;
}