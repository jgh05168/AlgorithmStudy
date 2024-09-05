/*
2157 여행

- 번호가 증가하지 않으면 저장 x
- bottom-up 방식으로 m을 늘려가면서 순회
- 점화식 : dp[m + 1][next] = max({dp[m + 1][next], dp[m][cur] + new_cost});
- 마지막에 n을 순회하며 최댓값 찾아서 출력
*/
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

#define ll long long
#define X first
#define Y second
#define pii pair<int, int>
#define pll pair<ll, ll>

using namespace std;

int N, M, K;
vector<pii> adj[305];
int dp[305][305];

void input() {
	cin >> N >> M >> K;
	for (int i = 0; i < K; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		if (a < b) adj[a].push_back({ b, c });

	}
}

void solve() {
	// 전처리
	for (int i = 0; i < adj[1].size(); i++) {
		int nx = adj[1][i].X;
		int nw = adj[1][i].Y;

		dp[nx][2] = max(dp[nx][2], nw);
	}

	// bottom-up
	for (int i = 2; i <= M; i++) {
		for (int j = 1; j <= N; j++) {

			if (dp[j][i] != 0) {

				for (int k = 0; k < adj[j].size(); k++) {
					int nx = adj[j][k].X;
					int nw = adj[j][k].Y;

					dp[nx][i + 1] = max(dp[nx][i + 1], dp[j][i] + nw);
				}

			}

		}
	}

	int result = 0;
	for (int i = 2; i <= M; i++)
		result = max(result, dp[N][i]);

	cout << result;
}

int main() {
	// (void)freopen("input.txt", "r", stdin);

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	input();
	solve();

	return 0;
}