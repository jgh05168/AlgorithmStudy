/*
근처 빵집의 가스관에 몰래 파이프를 설치해 훔쳐서 사용하기로 함
R x C
첫째 열은 빵집의 가스관, 마지막열은 빵집
건물이 있는 경우, 파이프 설치 불가능
각 칸은 오른쪽 대각선 방향으로 연결 가능, 

파이프라인의 경로는 겹칠 수 없고, 서로 접할 수 없다.

파이프라인의 최대 개수 구하기

풀이 : dfs
최대한 윗쪽 방향으로 이동해보기
visited 체크 확실히 하기
*/

#include <iostream>
#include <stack>
#include <vector>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m;
int visited[10001][501] = { 0, };
char grid[10001][501];

int dr[3] = { -1, 0, 1 };
int dc[3] = { 1, 1, 1 };

bool canGo(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}

int dfs(int r, int c) {
	if (c == m - 1)
		return 1;
	int nr, nc;
	for (int d = 0; d < 3; d++) {
		nr = r + dr[d];
		nc = c + dc[d];
		if (canGo(nr, nc) && !visited[nr][nc] && grid[nr][nc] == '.') {
			visited[nr][nc] = 1;
			int flag = dfs(nr, nc);
			if (flag)
				return 1;
			// 그리디로 해결하기 위해 이놈 없애주기
			// visited[nr][nc] = 0;
		}
	}

	return 0;
}

int main() {
	INIT;
	cin >> n >> m;
	char tmp;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> tmp;
			grid[i][j] = tmp;
		}
	}
	int ans = 0;
	// 하나씩 이동 시작
	for (int sr = 0; sr < n; sr++) {
		if (grid[sr][0] == '.')
			ans += dfs(sr, 0);
	}

	cout << ans << '\n';

	return 0;
}