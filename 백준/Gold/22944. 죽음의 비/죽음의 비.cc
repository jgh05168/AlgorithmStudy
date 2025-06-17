/*
n x n, 모든 곳에 체력을 1씩 감소시키는 죽음의 비
시작 위치, 종료 위치는 죽음의비가 내리지 않음

죽음의 비를 잠시 막아주는 우산이 K개 존재한다.
- 우산에는 내구도 D 존재한다. 

이동 순서
1. 상하좌우 이동
	- 이동한 곳이 안전지대라면 종료
	- 이동한 곳에 우산이 있다면 우산을 든다. 
		- 이동할 때부터 우산을 들고 있었으면 새로운 우산으로 바꾼다.
		- 버린 우산은 다시 사용 불가능
2. 죽음의 비를 맞았을 때,
	- 우산 o = 내구도 1 감소
	- 우산 x = 내 체력 1 감소

안전지대로 얼마나 빠르게 이동할 수 있는지 구하자.

풀이 : 
같은 위치 한 번 더 이동하는건 매우 비효율적임
장애물 개념이 없다.

우선순위큐
*/

#include <iostream>
#include <cstring>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct node {
	int r, c;
	int life;
	int umbrella;
	int moves;

	bool operator>(const node& other) const {
		if (moves != other.moves) {
			return moves > other.moves;
		}
		int cur_life = life + umbrella;
		int new_life = other.life + other.umbrella;
		if (cur_life != new_life) {
			return cur_life < new_life;
		}
		return umbrella < other.umbrella;
	}
};

int N, H, D;
int sr, sc, er, ec;

char grid[501][501];
// {최대 life, 최대 umbrella}
pair<int, int> max_resource[501][501];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

bool isValid(int r, int c) {
	return 0 <= r && r < N && 0 <= c && c < N;
}

void init() {
	string tmp;
	cin >> N >> H >> D;
	for (int i = 0; i < N; i++) {
		cin >> tmp;
		for (int j = 0; j < N; j++) {
			grid[i][j] = tmp[j];
			if (grid[i][j] == 'S') {
				sr = i;
				sc = j;
			}
			else if (grid[i][j] == 'E') {
				er = i;
				ec = j;
			}
			max_resource[i][j] = { -1, -1 };
		}
	}
}

void simulation() {
	priority_queue<node, vector<node>, greater<node>> pq;

	pq.push({ sr, sc, H, 0, 0 });
	max_resource[sr][sc] = { H, 0 };

	int answer = -1;

	while (!pq.empty()) {
		node current = pq.top();
		pq.pop();

		int r = current.r, c = current.c;
		int life = current.life;
		int umbrella = current.umbrella;
		int moves = current.moves;

		// 더 좋은 경로 / 자원 상태 로 현재 위치를 방문했을 경우가 있다면 continue
		if (life + umbrella < max_resource[r][c].first + max_resource[r][c].second) 
			continue;
		if (life + umbrella == max_resource[r][c].first + max_resource[r][c].second && umbrella < max_resource[r][c].second)
			continue;
		

		if (r == er && c == ec) {
			if (answer == -1 || moves < answer) {
				answer = moves;
			}
			continue;
		}

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];

			if (!isValid(nr, nc)) {
				continue;
			}

			int new_life = life;
			int new_umbrella = umbrella;

			if (grid[nr][nc] == 'U') {
				new_umbrella = D;
			}

			if (!(nr == sr && nc == sc) && !(nr == er && nc == ec)) {
				if (new_umbrella > 0) {
					new_umbrella--;
				}
				else {
					new_life--;
				}
			}

			if (new_life <= 0) {
				continue;
			}

			int new_total_resource = new_life + new_umbrella;
			int cur_total_resource = max_resource[nr][nc].first + max_resource[nr][nc].second;

			if (new_total_resource > cur_total_resource || (new_total_resource == cur_total_resource && new_umbrella > max_resource[nr][nc].second)) {
				max_resource[nr][nc] = { new_life, new_umbrella };
				pq.push({ nr, nc, new_life, new_umbrella, moves + 1 });
			}
		}
	}

	cout << answer << '\n';
}

int main() {

	init();
	simulation();

	return 0;
}