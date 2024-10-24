/*
집에서 학교로 가는 길의 경우의 수를 구하기
도로가 공사중인 경우, 지나갈 수 없음
- 항상 최단거리로만 이동한다 -> 항상 도로를 정확하게 N + M개 거친다.
	-> 이보다 길어지는건 최단거리가 아님

풀이:
누적합 방식으로 더해가기
이동할 수 없는 구간에 대해서 체크해주기 -> 중복되는 구간이 존재함
	= 두 경로에서 중복되는 지점이 공사중인 경우, 덧셈을 진행해주면 안된다.
		|
		v
	--> 0(중복된 불가능한 구간)

=> 나처럼 불가능한 배열을 2배로 늘려서 체크해도 괜찮고, 3차원 배열로(위에서 오는 방향, 옆에서 오는 방향)(101, 101, 2) 체크해도 무방하다.
*/

#include <iostream>
#include <algorithm>
#define lli unsigned long long int

using namespace std;

int n, m, k;
int a, b, c, d;
lli dp[102][102] = { 0, };
lli arr[202][202] = { 0, };


int main() {
	cin.tie(0); ios::sync_with_stdio(false);
	cin >> n >> m >> k;
	for (int i = 0; i < k; i++) {
		cin >> a >> b >> c >> d;
		arr[b + d][a + c] = 1;
	}

	// (0, 0) -> (m, n)
	// dp 초기화 ( 한 방향으로만 가는 경우에 대해서 )
	dp[0][0] = 1;
	for (int i = 1; i <= m; i++) {
		if (arr[2 * i - 1][0] == 1)
			break;
		dp[i][0] = 1;
	}
	for (int i = 1; i <= n; i++) {
		if (arr[0][2 * i - 1] == 1)
			break;
		dp[0][i] = 1;
	}

	// 길찾기 시작
	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= n; j++) {
			if (arr[2 * i - 1][2 * j] == 0)
				dp[i][j] += dp[i - 1][j];
			if (arr[2 * i][2 * j - 1] == 0)
				dp[i][j] += dp[i][j - 1];
		}
	}

	cout << dp[m][n] << '\n';

	return 0;
}