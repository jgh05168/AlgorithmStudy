/*
한 쪽 문에서 다른 쪽 문을 볼 수 있도록 거울을 설치하고 싶어짐
거울을 설치하는 최소 개수를 구하자
모든 거울은 양면거울이기 때문에 양쪽에서 반사가 일어날 수 있다.

n <= 50
풀이 : 
거울 개수 기준으로 다익스트라 진행
visited는 네 방향으로 진행. 이전에 설치 여부는 이동 위치로 판단하자.
	-> (d + 2) % 4 라면 거울이 이미 설치된 것으로 간주하고 넘어가기
*/

#include <iostream>
#include <queue>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

struct node {
	int mirror, dist, r, c;
};

int n;
pair<int, int> letsgo;
char grid[51][51];
int visited[4][51][51];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };


struct cmp {
	bool operator()(node a, node b) {
		return a.mirror > b.mirror;
	}
};


bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < n;
}


void init() {
	cin.tie(0); ios::sync_with_stdio(false);
	memset(visited, 0, sizeof(visited));
	cin >> n;
	string tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		for (int j = 0; j < tmp.size(); j++) {
			grid[i][j] = tmp[j];
			if (grid[i][j] == '#') {
				letsgo = { i, j };
			}
		}
	}
}


int solution(int sr, int sc) {
	priority_queue<node, vector<node>, cmp> pq;
	pq.push({ -1, -1, sr, sc });
	for (int i = 0; i < 4; i++) {
		visited[i][sr][sc] = 1;
	}
		

	while (!pq.empty()) {
		int mirror = pq.top().mirror, cur_d = pq.top().dist;
		int r = pq.top().r, c = pq.top().c;
		pq.pop();

		// 직진 구간이면 직진만 ㄱㄴ
		if (grid[r][c] == '.') {
			int nr = r + dr[cur_d], nc = c + dc[cur_d];
			if (isValid(nr, nc) && !visited[cur_d][nr][nc] && grid[nr][nc] != '*') {
				if (grid[nr][nc] == '#')
					return mirror;
				pq.push({ mirror, cur_d, nr, nc });
				visited[cur_d][nr][nc] = 1;
			}
		}
		else if (grid[r][c] == '!' || grid[r][c] == '#') {
			for (int d = 0; d < 4; d++) {
				if (cur_d >= 0 && abs(cur_d - d) == 2)
					continue;
				int nr = r + dr[d], nc = c + dc[d];
				int new_mirror = mirror;
				if (isValid(nr, nc) && !visited[d][nr][nc] && grid[nr][nc] != '*') {
					if (cur_d != d)
						new_mirror++;
					if (grid[nr][nc] == '#')
						return new_mirror;
					pq.push({ new_mirror, d, nr, nc });
					visited[d][nr][nc] = 1;
				}
			}
		}
		
	}

	return 0;
}


int main() {
	init();
	cout << solution(letsgo.first, letsgo.second) << '\n';
	return 0;
}