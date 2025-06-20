/*
각 칸에는 4개의 인접한 곳으로 이동할 수 있는 문이 있음
이 4개의 문은 한 번에 한개만 열린다 ? 
	- 서로간에 이동은 별개로 작동한다.
	- 반대편 문이 안열려있어도 갈 수 있음
미로에는 K개의 보물상자가 있음
문이 열린 방향으로 한 칸 움직이거나, 원하는 방향의 문이 열릴 때까지 기다릴 수 있다.

풀이 : 비트마스킹
보물의 총 개수 : 8개이므로 비트마스킹 visited 사용 ㄱㄴ
모든 이동 마치고, 모든 문 돌려야한다. = 최대 10000

그럼 : 10000 * 10000 = 100000000 시간복잡도를 갖는다. . .

*/

#include <iostream>
#include <cstring>
#include <string>
#include <queue>

using namespace std;

int n, m, k;
int grid[101][101];
int visited[1 << 8][101][101];
int stay[1 << 8][4][101][101];
int treasure_map[101][101];

// 우 하 좌 상
int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

int isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}



int init() {
	memset(visited, -1, sizeof(visited));
	memset(stay, 0, sizeof(stay));
	memset(treasure_map, -1, sizeof(treasure_map));

	cin >> n >> m;
	if (!n && !m)
		return 0;

	string tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		for (int j = 0; j < m; j++) {
			if (tmp[j] == 'E')
				grid[i][j] = 0;
			else if (tmp[j] == 'S')
				grid[i][j] = 1;
			else if (tmp[j] == 'W')
				grid[i][j] = 2;
			else
				grid[i][j] = 3;
		}
	}

	cin >> k;
	int r, c;
	for (int i = 0; i < k; i++) {
		cin >> r >> c;
		treasure_map[r - 1][c - 1] = i;
	}

	return 1;
}


int simulation() {
	queue<pair<int, pair<int, int>>> q;			// 보물 , { r, c }
	q.push({ 0, { 0, 0 } });
	visited[0][0][0] = 0;
	int move = 0;

	while (!q.empty()) {
		int treasure_cnt = q.front().first;
		int r = q.front().second.first, c = q.front().second.second;
		q.pop();

		if (r == n - 1 && c == m - 1 && treasure_cnt == (1 << k) - 1)
			return visited[treasure_cnt][r][c];

		// 이동하는 경우
		int d = (grid[r][c] + visited[treasure_cnt][r][c]) % 4;
		int nr = r + dr[d], nc = c + dc[d];
		if (isValid(nr, nc)) {
			int new_treasure_cnt = treasure_cnt;
			if (treasure_map[nr][nc] != -1)
				new_treasure_cnt |= (1 << treasure_map[nr][nc]);
			if (visited[new_treasure_cnt][nr][nc] == -1) {
				visited[new_treasure_cnt][nr][nc] = visited[treasure_cnt][r][c] + 1;
				q.push({ new_treasure_cnt, {nr, nc} });
			}
		}
					
		// 이동하지 않는 경우
		// 네 번 모두 해당 자리에 가만히 있었다면, continue
		if (stay[treasure_cnt][d][r][c])
			continue;
		q.push({ treasure_cnt, { r, c } });
		visited[treasure_cnt][r][c]++;
		stay[treasure_cnt][d][r][c] = 1;

	}
	
	return -1;
}


int main() {
	while (1) {
		int gamestart = init();
		if (!gamestart)
			break;

		cout << simulation() << '\n';
	}
	
}
