/*
버튼은 네가지가 존재함.
버튼을 누르면 두 동전이 같은 방향으로 이동

- 이동하려는 칸이 벽면이면, 동전 이동 불가
	-> 동전이 겹치면 안되는 것에 주의
- 이동 방향에 칸이 없으면, 동전 떨어짐
- 그 외 경우에는, 이동하려는 방향마다 한 칸 이동함

재귀함수로 진행
*/

#include <iostream>
#include <vector>
#include <algorithm>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m;
char grid[21][21];
int answer = 40000;

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

int check_move(int r, int c) {
	if (0 <= r && r < n && 0 <= c && c < m)
		return 1;
	return 0;
}

void dfs(int depth, pair<int, int> coin1, pair<int, int> coin2, int alive) {
	// 종료조건
	if (answer < depth || depth > 10)
		return;
	// 완료조건
	if (alive == 1) {
		answer = depth;
		return;
	}
	// dfs 시작
	pair<int, int> ncoin1, ncoin2;
	for (int d = 0; d < 4; d++) {
		ncoin1.first = coin1.first + dr[d];
		ncoin1.second = coin1.second + dc[d];
		ncoin2.first = coin2.first + dr[d];
		ncoin2.second = coin2.second + dc[d];
		
		int new_alive = check_move(ncoin1.first, ncoin1.second) + check_move(ncoin2.first, ncoin2.second);
		int move_flag = 0;
		if (grid[ncoin1.first][ncoin1.second] == '#') {
			ncoin1 = coin1;
			move_flag++;
		}
		if (grid[ncoin2.first][ncoin2.second] == '#') {
			ncoin2 = coin2;
			move_flag++;
		}

		if (move_flag < 2 && new_alive)
			dfs(depth + 1, ncoin1, ncoin2, new_alive);
	}
}

int main() {
	INIT;
	cin >> n >> m;
	vector<pair<int, int>> coins;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> grid[i][j];
			if (grid[i][j] == 'o') {
				coins.push_back({ i, j });
				grid[i][j] = '.';
			}
		}
	}

	dfs(0, coins[0], coins[1], 2);

	if (answer == 40000)
		answer = -1;
	cout << answer << '\n';

}