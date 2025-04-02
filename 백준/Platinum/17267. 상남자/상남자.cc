/*
10:30 시작

영조는 위아래로만 간다.
왼쪽으로 최대 L번, 오른쪽으로 최대 R번만큼 이동할 수 있게 도와준다.
출발 위치로부터 이동해서 갈 수 있는 모든 땅의 개수를 구해보자

1000 x 1000
풀이 : 모든 grid를 방문하려고 한다면, 시간초과가 발생할 듯 함
- 위아래 이동하는 부분을 우선으로 책정
- 이후, 왼쪽, 오른쪽 이동 해보기
queue에는 r, c, l, r 정보 넣어두기
*/

#include <iostream>
#include <cstring>
#include <string>
#include <queue>

using namespace std;

struct Node {
	int r, c, left, right;
};

int n, m, start_left, start_right;
int grid[1001][1001];
int visited[1001][1001] = { 0, };

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}


pair<int, int> init() {
	int sr = 0, sc = 0;
	string tmp;
	cin >> n >> m;
	cin >> start_left >> start_right;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		for (int j = 0; j < m; j++) {
			grid[i][j] = tmp[j] - '0';
			if (grid[i][j] == 2) 
				sr = i, sc = j;
		}
	}
	return { sr, sc };
}


int bfs(int sr, int sc) {
	deque<Node> q;
	q.push_back({ sr, sc, start_left, start_right });
	visited[sr][sc] = 1;
	int ans = 0;

	while (!q.empty()) {
		int r = q.front().r, c = q.front().c, left_cnt = q.front().left, right_cnt = q.front().right;
		q.pop_front();

		ans++;

		for (int d = 0; d < 4; d++) {
			if (!left_cnt && d == 2)
				continue;
			if (!right_cnt && d == 3)
				continue;

			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && !visited[nr][nc] && !grid[nr][nc]) {
				visited[nr][nc] = 1;
				if (!d || d == 1)
					q.push_front({ nr, nc, left_cnt, right_cnt });
				else if (d == 2)
					q.push_back({ nr, nc, left_cnt - 1, right_cnt });
				else
					q.push_back({ nr, nc, left_cnt, right_cnt - 1 });
			}
		}
	}

	return ans;
}


int main() {
	pair<int, int> start = init();

	cout << bfs(start.first, start.second) << '\n';
	
	return 0;
}