#include <iostream>
#include <vector>

using namespace std;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N, MOD = 1'000'000'007;
	cin >> N;

	int dist[3][1516];
	dist[0][1] = 0;
	dist[0][2] = 1; dist[1][2] = 1; dist[2][2] = 0;

	for (int i = 3; i < N + 1; i++) {
		dist[0][i] = (dist[2][i - 1] + dist[1][i - 1]) % MOD;
		dist[1][i] = (dist[0][i - 1] + dist[2][i - 1]) % MOD;
		dist[2][i] = (dist[1][i - 1] + dist[0][i - 1]) % MOD;
	}

	cout << dist[0][N];

	return 0;
}