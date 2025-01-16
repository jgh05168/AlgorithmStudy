/*
5 x 5 x 5
주어진 판들은 시계 or 반시계 방향으로 회전 가능함
회전을 완료한 후, 참가자는 판 5개를 쌓는다. -> 순서는 자유롭게 정할 수 있음
참가자는 칸에서 변으로 인접한 칸이 들어갈 수 있는 칸인 경우, 그 칸으로 이동 가능함
본인이 설계한 미로를 가장 적은 이동 횟수로 탈출한 사람이 우승한다. 
가장 적은 이동 횟수를 구해보자

풀이 : 시뮬레이션, BFS
rotate, 조합 필요한데 시계나 반시계나 두 방향 중 한 방향으로만 돌리면 된다.(결국 같음)
각 판 선택해서 회전하고 & 조합 만들고 & bfs 진행
-> 재귀 + 조합 재귀 + bfs
입구와 출구가 정해져있지 않으므로 총 4번 진행해봐야함
4^5 * 2^5 * 4 * 5 * 5 * 5
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#define INF 5 * 5 * 5 * 5

using namespace std;

struct Node {
	int h, r, c;
};

int n = 5, ans = INF;
int visited[5][5][5];
int selected[5];
vector<vector<vector<int>>> grid;
Node entrance = {4, 0, 0};

int dr[6] = { 0, 1, 0, -1, 0, 0 };
int dc[6] = { 1, 0, -1, 0, 0, 0 };
int dh[6] = { 0, 0, 0, 0, -1, 1 };

void init() {
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

	int tmp;
	for (int i = 0; i < n; i++) {
		vector<vector<int>> tmp_grid(n);
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				cin >> tmp;
				tmp_grid[j].push_back(tmp);
			}
		}
		grid.push_back(tmp_grid);
		tmp_grid.clear();
	}
}


bool canMove(Node u) {
	return 0 <= u.h && u.h < n && 0 <= u.r && u.r < n && 0 <= u.c && u.c < n;
}


void bfs(Node entrance, vector<vector<vector<int>>> grid) {
	Node exit = { abs(entrance.h - 4), abs(entrance.r - 4), abs(entrance.c - 4) };
	// 입구 혹은 출구가 막혔는지 확인
	if (!grid[entrance.h][entrance.r][entrance.c] || !grid[exit.h][exit.r][exit.c])
		return;

	memset(visited, -1, sizeof(visited));
	queue<Node> queue;
	queue.push(entrance);
	visited[entrance.h][entrance.r][entrance.c] = 0;

	while (!queue.empty()) {
		Node u = queue.front();
		queue.pop();

		if (ans <= visited[u.h][u.r][u.c])
			continue;

		for (int d = 0; d < 6; d++) {
			Node v = { u.h + dh[d], u.r + dr[d], u.c + dc[d] };
			if (canMove(v) && visited[v.h][v.r][v.c] == -1 && grid[v.h][v.r][v.c]) {
				// 도착지인 경우 종료
				if (v.h == exit.h && v.r == exit.r && v.c == exit.c) {
					ans = min(ans, visited[u.h][u.r][u.c] + 1);
					return;
				}
				queue.push(v);
				visited[v.h][v.r][v.c] = visited[u.h][u.r][u.c] + 1;
			}
		}
	}
}


void build_cube(int depth, vector<vector<vector<int>>> cube, vector<vector<vector<int>>> grid) {
	if (depth == 5) {
		// bfs 진행
		// (0, 0, 0 / 4, 4, 4), (0, 0, 4 / 4, 4, 0), (0, 4, 0 / 4, 0, 4), (0, 4, 4 / 4, 0, 0)
		bfs(entrance, cube);
		return;
	}
	for (int i = 0; i < n; i++) {
		if (!selected[i]) {
			selected[i] = 1;
			cube.push_back(grid[i]);
			build_cube(depth + 1, cube, grid);
			cube.pop_back();
			selected[i] = 0;
		}
	}
}


vector<vector<int>> rotate(vector<vector<int>> grid) {
	vector<vector<int>> new_grid(n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			new_grid[i].push_back(0);
	}
	// rotate 시작
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			new_grid[j][n - i - 1] = grid[i][j];
		}
	}

	return new_grid;
}


void rotate_grid(int depth, vector<vector<vector<int>>> grid) {
	if (depth == 5) {
		// 모든 애들 다 돌렸으면 층 새로 쌓기
		memset(selected, 0, sizeof(selected));
		vector<vector<vector<int>>> tmp_cube;
		build_cube(0, tmp_cube, grid);
		return;
	}
		
	for (int i = 0; i < 4; i++) {
		grid[depth] = rotate(grid[depth]);
		rotate_grid(depth + 1, grid);

	}
}



int main() {
	init();

	// rotate 먼저 진행
	rotate_grid(0, grid);

	if (ans == INF)
		ans = -1;
	cout << ans << '\n';

	return 0;
}