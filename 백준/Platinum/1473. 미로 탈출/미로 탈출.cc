/*
A : 네 면 모두 존재		1111 : 15
B : 문 없음				0	 : 0
C : 상 / 하				1010 : 10
D : 좌 / 우				0101 : 5

방끼리 움직이는덴 1초 소요
방 이동 시에는 두 방향 모두 문이 존재해야함
미로 조종 버튼 누를 시 1초 소요
	- 가로세로 모든 문이 90도 회전한다.

풀이 :  bfs, 비트마스킹
visited 설정이 중요한데 .. 너무 메모리 공간 커지므로 unordered_map 사용
n, m < 7이기 때문에 충분히 가능함

*/
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cstring>

using namespace std;

struct State {
	int r, c;
	int row_parity;
	int col_parity;
	int time;         

	bool operator>(const State& other) const {
		return time > other.time;
	}
};

int n, m;
int miro_initial[8][8]; // 초기 미로 방의 문 상태 (비트마스크)

int dr[] = { 0, 1, 0, -1 };
int dc[] = { 1, 0, -1, 0 };

int opposite_door_dir[] = { 2, 3, 0, 1 };

// visited[r][c][row_parity][col_parity] 형태로 사용
// row_parity: N개의 행 각각 1비트 (N<=7 이므로 2^7 = 128)
// col_parity: M개의 열 각각 1비트 (M<=7 이므로 2^7 = 128)
int visited[8][8][1 << 7][1 << 7]; // Max N, M = 7, so 2^7 = 128

// 방의 문 상태를 90도 시계 방향으로 회전시키는 함수
// A (1111) -> 1111, B (0000) -> 0000
// C (1010) -> 0101 (D), D (0101) -> 1010 (C)
// 즉, A/B는 회전 불변, C/D는 2번 회전 시 원상 복구
int rotate_door_once(int door_state) {
	if (door_state == 15 || door_state == 0) return door_state; // A or B
	if (door_state == 10) return 5; // C -> D
	if (door_state == 5) return 10; // D -> C
	return door_state; // 예상치 못한 값
}

// 주어진 행/열 홀짝 회전 정보에 따라 현재 방의 실제 문 상태를 반환하는 함수
int get_current_room_state(int r, int c, int row_parity, int col_parity) {
	int initial_state = miro_initial[r][c];

	// r번째 행의 홀짝성 (1비트)
	int r_par = (row_parity >> r) & 1;
	// c번째 열의 홀짝성 (1비트)
	int c_par = (col_parity >> c) & 1;

	// 이 방의 총 홀짝성 (1: 홀수 번 회전, 0: 짝수 번 회전)
	int total_parity = (r_par + c_par) % 2;

	int current_state = initial_state;
	if (total_parity == 1) { // 홀수 번 회전했다면 (즉, C->D, D->C 변환이 일어남)
		current_state = rotate_door_once(current_state);
	}
	return current_state;
}

// BFS 탐색 함수
int bfs(int sr, int sc) {
	priority_queue<State, vector<State>, greater<State>> pq;

	// visited 배열을 큰 값으로 초기화 (memset 0x3f3f3f3f는 INT_MAX에 가까운 값)
	memset(visited, 0x3f, sizeof(visited));

	// 시작 지점 (sr,sc), 초기 회전 없음 (모든 parity 0), 시간 0
	pq.push({ sr, sc, 0, 0, 0 });
	visited[sr][sc][0][0] = 0;

	while (!pq.empty()) {
		State current = pq.top();
		pq.pop();

		int r = current.r;
		int c = current.c;
		int row_parity = current.row_parity;
		int col_parity = current.col_parity;
		int time = current.time;

		// 목표 지점에 도달했으면 시간 반환
		if (r == n - 1 && c == m - 1) {
			return time;
		}

		// 이미 더 짧은 시간으로 이 상태에 방문한 적이 있다면 스킵
		if (visited[r][c][row_parity][col_parity] < time) {
			continue;
		}

		// 현재 방의 실제 문 상태 가져오기
		int current_room_door_state = get_current_room_state(r, c, row_parity, col_parity);

		// 인접한 방으로 이동 
		for (int d = 0; d < 4; ++d) { 
			int nr = r + dr[d];
			int nc = c + dc[d];

			// 미로 범위 체크
			if (nr < 0 || nr >= n || nc < 0 || nc >= m)
				continue;

			// 현재 방에 이동하려는 방향으로 문이 있는지 확인
			if (!((current_room_door_state >> d) & 1))
				continue;

			// 다음 방의 실제 문 상태 가져오기 (회전 홀짝성은 동일)
			int next_room_door_state = get_current_room_state(nr, nc, row_parity, col_parity);

			// 다음 방에 현재 방에서 들어오는 방향(반대 방향)으로 문이 있는지 확인
			if (!((next_room_door_state >> opposite_door_dir[d]) & 1)) 
				continue;

			// 더 짧은 시간으로 도달할 수 있다면 큐에 추가 및 visited 업데이트
			if (visited[nr][nc][row_parity][col_parity] > time + 1) {
				visited[nr][nc][row_parity][col_parity] = time + 1;
				pq.push({ nr, nc, row_parity, col_parity, time + 1 });
			}
		}

		// 버튼 누르기 (1초 소요)
		// 현재 위치 (r, c)의 행과 열의 모든 방이 회전함
		int new_row_parity = row_parity ^ (1 << r); // r번째 비트 토글
		int new_col_parity = col_parity ^ (1 << c); // c번째 비트 토글

		// 버튼을 누른 후, 현재 위치는 그대로 (r,c)
		// 새로운 행/열 홀짝 상태로 1초가 소요됨
		if (visited[r][c][new_row_parity][new_col_parity] > time + 1) {
			visited[r][c][new_row_parity][new_col_parity] = time + 1;
			pq.push({ r, c, new_row_parity, new_col_parity, time + 1 });
		}
	}

	return -1;
}

// 초기화 함수 (입력 처리)
void init() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		string row_str;
		cin >> row_str;
		for (int j = 0; j < m; ++j) {
			if (row_str[j] == 'A') miro_initial[i][j] = 15;
			else if (row_str[j] == 'B') miro_initial[i][j] = 0;  
			else if (row_str[j] == 'C') miro_initial[i][j] = 10;  
			else if (row_str[j] == 'D') miro_initial[i][j] = 5;  
		}
	}
}

void simulation() {
	int answer = bfs(0, 0);

	cout << answer << '\n';
}

int main() {
	init();

	simulation();

	return 0;
}