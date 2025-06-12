/*
n x n, 왼쪽 위 목초지 & 오른쪽 아래 헛간
오른쪽 or 아래로만 걸어갈 것임. 

걷는 방향을 최대 K번 바꿀 수 있다.

dp를 쓸 수도 있을 것 같음.
그냥 가는가 vs 방향을 바꿔서 가는가
방향을 바꾸는 경우에는 비교 조건을 추가해야한다. (K를 다 쓰고, 방향에 맞게 걸어가지 못하는 경우)
+ 방향 & k 카운트에 따라서 dp 배열에 저장해야함
*/

#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int t, n, k;
int dp[2][4][51][51];
char grid[51][51];

int dr[2] = { 0, 1 };
int dc[2] = { 1, 0 };

bool isValid(int r, int c) {
	return r < n && c < n;
}


void init() {
	cin >> n >> k;
	string tmp;
	
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		for (int j = 0; j < n; j++) {
			grid[i][j] = tmp[j];
		}
	}

	memset(dp, -1, sizeof(dp));
}


int topDown(int r, int c, int cnt_k, int d) {
	if (cnt_k > k)
		return 0;
	if (r == n - 1 && c == n - 1)
		return 1;
	int &ret = dp[d][cnt_k][r][c];
	if (ret != -1)
		return ret;

	ret = 0;
	int nr = r + dr[d], nc = c + dc[d];
	if (isValid(nr, nc) && grid[nr][nc] == '.') {
		ret += topDown(nr, nc, cnt_k, d);
	}

	int nd = (d + 1) % 2;
	nr = r + dr[nd], nc = c + dc[nd];
	if (isValid(nr, nc) && grid[nr][nc] == '.') {
		ret += topDown(nr, nc, cnt_k + 1, nd);
	}

	return ret;
}


void simulation() {
	int answer = 0;

	if (grid[0][1] == '.')
		answer += topDown(0, 1, 0, 0);
	if (grid[1][0] == '.')
		answer += topDown(1, 0, 0, 1);

	cout << answer << '\n';
}


int main() {
	cin >> t;

	while (t--) {
		init();

		simulation();
	}

}