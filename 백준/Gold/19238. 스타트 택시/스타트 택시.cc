/*
10 : 40 시작

n x n크기의 격자에서 m명의 승객을 태우는 것이 목표
각 칸은 비어있거나 벽이 놓여있음
택시는 상하좌우 이동 가능
특정 위치로 이동할 때, 최단 경로로만 이동한다.

승객 태우기
1. 한 명의 승객만 탑승 가능
2. 태울 승객을 고를 땐, 현재 위치에서 최단 거리가 가장 짧은 승객을 고름
	- 여러명인 경우, 행, 열 작은 순서대로 고른다.(상, 좌, 우, 하)
	- 택시와 승객이 같은 위치인 경우도 있음

이동
1. 연료는 한 칸 이동할 때마다 1만큼 소모된다
2. 승객을 목적지까지 이동시키면 이동하면서 소모한 연료의 2배가 충전된다.
3. 이동 중 연료가 다 떨어지면 업무 끝
	- 도착과 동시에 연료가 떨어지는 것은 성공한 것으로 친다.


풀이 : BFS
- 연료의 양은 무한하다. (long long)
- 태울 녀석 찾을 때 bfs 한 번, 목적지로 이동할 때 한 번
*/

#include <iostream>
#include <cstring>
#include <queue>
#define ll long long

using namespace std;

struct taxiInfo {
	int r, c, fuel;
};

struct passenger {
	int er, ec;
};

int n, m;
taxiInfo taxi;
int grid[21][21];
int visited[21][21];
int passenger_map[21][21];
passenger passenger_list[401];

int dr[4] = { -1, 0, 0, 1 };
int dc[4] = { 0, -1, 1, 0 };


bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < n;
}


void init() {
	cin >> n >> m >> taxi.fuel;
	// grid 입력
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> grid[i][j];
		}
	}
	// 택시 위치 입력
	cin >> taxi.r >> taxi.c;
	taxi.r--; taxi.c--;

	int sr, sc, er, ec;
	// 손님 위치 입력
	for (int i = 1; i < m + 1; i++) {
		cin >> sr >> sc >> er >> ec;
		passenger_map[sr - 1][sc - 1] = i;
		passenger_list[i] = { er - 1, ec - 1 };
	}

}


pair<int, int> find_passenger() {
	queue<pair<int, int>> q;	
	q.push({ taxi.r, taxi.c });
	memset(visited, -1, sizeof(visited));
	visited[taxi.r][taxi.c] = 0;
	pair<int, int> return_value = { 21, 21 };
	int dist = 401;

	// 현재 택시 위치에 바로 손님이 있는 경우
	if (passenger_map[taxi.r][taxi.c]) {
		return { taxi.r, taxi.c };
	}

	while (!q.empty()) {
		int r = q.front().first, c = q.front().second;
		q.pop();

		// 손님을 찾은 경우, return값 설정
		if (passenger_map[r][c] && dist >= visited[r][c]) {
			if (dist > visited[r][c]) {
				return_value = { r, c };
				dist = visited[r][c];
			}
			else {
				if (return_value.first > r)
					return_value = { r, c };
				if (return_value.first == r && return_value.second > c)
					return_value = { r, c };
			}
		}

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && visited[nr][nc] == -1 && !grid[nr][nc]) {
				// 연료가 남아있는 경우에만 이동 가능함
				if (taxi.fuel < visited[r][c] + 1)
					continue;
				visited[nr][nc] = visited[r][c] + 1;
				q.push({ nr, nc });
			}
		}
	}
	return return_value;
}


int move_taxi(int sr, int sc) {
	int passenger_idx = passenger_map[sr][sc];
	int er = passenger_list[passenger_idx].er, ec = passenger_list[passenger_idx].ec;
	memset(visited, -1, sizeof(visited));
	visited[sr][sc] = 0;
	queue<pair<int, int>> q;
	q.push({ sr, sc });

	while (!q.empty()) {
		int r = q.front().first, c = q.front().second;
		q.pop();

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && visited[nr][nc] == -1 && !grid[nr][nc]) {
				// 연료 다 쓴 경우, continue
				if (taxi.fuel < visited[r][c] + 1)
					continue;
				// 도착지에 무사 도착 한 경우
				if (nr == er && nc == ec) {
					taxi.r = er, taxi.c = ec;
					passenger_map[sr][sc] = 0;	// 데려다준 손님은 명단 제외
					// 연료 정산
					taxi.fuel += visited[r][c] + 1;
					return 1;
				}
				q.push({ nr, nc });
				visited[nr][nc] = visited[r][c] + 1;
			}
		}
	}
	return 0;
}


int solution() {
	pair<int, int> cur_passenger;
	int complete;
	int took_passenger = 0;

	while(1) {
		// 1. 택시가 태울 손님을 찾아 떠남
		cur_passenger = find_passenger();
		// 1-2. 연료를 다 썼다면 종료
		if (cur_passenger.first == 21)
			return -1;
		// 1-3. 연료 소모 체크
		taxi.fuel -= visited[cur_passenger.first][cur_passenger.second];

		// 2. 택시가 목적지로 출발
		complete = move_taxi(cur_passenger.first, cur_passenger.second);
		// 2-2. 데려다주는데 실패했다면, 종료
		if (!complete)
			return -1;

		// 3. 손님 체크
		took_passenger++;
		// 3-2. 모든 손님 데려다 준 경우, 종료
		if (took_passenger == m)
			return taxi.fuel;
	}
}


int main() {
	init();

	cout << solution() << '\n';

	return 0;
}