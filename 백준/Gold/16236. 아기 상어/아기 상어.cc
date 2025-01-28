/*
baby shark !

자신의 크기보다 큰 물고기 칸은 지날 수 없음
자신의 크기보다 작은 애들만 먹을 수 있음
크기가 같으면 지나갈 수만 있음

= 이동 방법 =
- 먹을 수 있는 물고기가 한마리라면 먹으러감
- 먹을 수 있는 물고기가 여러마리면 가장 가까운 물고기 먹으러감
- 거리는 지나야 하는 칸의 개수의 최솟값
- 행, 열 작은 순으로 우선순위

이동은 1초 걸리고, 자신의 크기와 같은 수의 물고기를 먹을 때마다 1 증가한다.

몇 초 만에 엄마 상어에게 도움을 요청하는지 작성

알고리즘 : 시뮬, 완탐
우선순위큐 쓰지 말고 풀어보자

배열의 크기 < 20이므로 물고기 총 개수는 400개 => 완탐 가능
배열에 물고기는 무조건 저장해야함 : 못지나가는 경우 존재하기 때문

bfs로 갈 수 있을 때 거리를 체크한다.
*/

#include <iostream>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

int n, m = 0;		// m = 물고기 마릿수
int grid[21][21] = { 0, };
int visited[21][21];
pair<int, pair<int, int>> baby_shark;
int catch_fish = 0;

int dr[4] = { -1, 0, 0, 1 };
int dc[4] = { 0, -1, 1, 0 };

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < n;
}

int find_dist() {
	memset(visited, -1, sizeof(visited));
	visited[baby_shark.second.first][baby_shark.second.second] = 0;
	queue<pair<int, int>> pq;
	pq.push({ baby_shark.second.first , baby_shark.second.second });
	int tmp_r = -1, tmp_c = -1;
	int dist = 40000;

	while (!pq.empty()) {
		int r = pq.front().first;
		int c = pq.front().second;
		pq.pop();

		if (visited[r][c] + 1 > dist)
			continue;

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && visited[nr][nc] == -1 && baby_shark.first >= grid[nr][nc]) {
				// 먹을 수 있는 물고기 찾았는지
				if (grid[nr][nc] && baby_shark.first > grid[nr][nc]) {
					if (tmp_r == -1 && tmp_c == -1) {
						tmp_r = nr, tmp_c = nc;
						dist = visited[r][c] + 1;
						continue;
					}
					else if (nr < tmp_r) {
						tmp_r = nr, tmp_c = nc;
						dist = visited[r][c] + 1;
						continue;
					}
					else if (nr == tmp_r && nc < tmp_c) {
						tmp_r = nr, tmp_c = nc;
						dist = visited[r][c] + 1;
						continue;
					}
				}
				visited[nr][nc] = visited[r][c] + 1;
				pq.push({ nr, nc });
			}
		}
	}

	baby_shark.second = {tmp_r, tmp_c};
	grid[tmp_r][tmp_c] = 0;
	return dist;
}


void init() {
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> grid[i][j];
			if (grid[i][j] == 9) {
				baby_shark.second = { i, j };
				grid[i][j] = 0;
			}
		}
	}
	baby_shark.first = 2;
}


int solution() {
	int ans = 0;
	while (1) {
		// 물고기랑 거리 계산
		int dist = find_dist();

		// 종료 조건
		if (dist == 40000)
			break;

		// 물고기 잡은 경우 처리
		ans += dist;
		catch_fish++;
		// 레벨업 조건
		if (baby_shark.first == catch_fish) {
			baby_shark.first++;
			catch_fish = 0;
		}
		
	}
	
	return ans;
}

int main() {
	init();

	int answer = 0;
	answer = solution();
	cout << answer << '\n';

	return 0;
}