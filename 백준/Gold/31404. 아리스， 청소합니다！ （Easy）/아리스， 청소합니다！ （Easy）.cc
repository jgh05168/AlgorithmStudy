/*
11:30

h x w 직사각형 격자 모양의 부실을 청소하려고 함

처음에 모든 칸은 먼지
로봇청소기는 바라보는 방향으로 전진 / 제자리 회전 가능

규칙표는 grid와 대응되고, 회전 각도가 적혀있음
이후, 매 단위시간마다 다음 이동을 반복한다.

- 현재 칸에 먼지가 있다면 먼지 제거
- 방금 먼지를 제거했다면 규칙표 A를, 먼지 제거를 안했다면 B 참고
	- 규칙표에서 현재 좌표에 적힌 만큼 시계방향으로 회전
- 바라보는 방향으로 한 칸 전진

로봇이 청소기 영역 밖으로 벗어나면 작동 중지
더이상 먼지를 제거할 수 없는 경우 작동 중지

풀이 : h, w <= 64
문제 풀이 관건 : 먼지가 없는 칸만 반복하는 경우를 어떻게 판별할까
-> 4방향 visited 배열 + Rule A / B에 맞는 visited 또 생성
먼지가 있다 ? [0][방향][h][w]
이동중에 한 번이라도 먼지가 있는 배열을 마주한다면, 먼지있는 배열은 초기화 진행해줘야함

굳이 dfs로 안하고 while문 돌려도 될 듯 하다.
어차피 모든 방향에 대해 파악하는 문제가 아님
*/

#include <iostream>
#include <cstring>
#include <string>
#define A 0
#define B 1
using namespace std;

struct robot {
	int r, c, d;
};

int n, m;
robot aris;
int grid[65][65];
int board[2][65][65];
int visited[2][4][65][65];

int dr[4] = { -1, 0, 1, 0 };
int dc[4] = { 0, 1, 0, -1 };

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}


void init() {
	cin >> n >> m;
	cin >> aris.r >> aris.c >> aris.d;
	string s;
	for (int i = 0; i < n; i++) {
		cin >> s;
		for (int j = 0; j < s.size(); j++)
			board[A][i][j] = s[j] - '0';
	}
	for (int i = 0; i < n; i++) {
		cin >> s;
		for (int j = 0; j < s.size(); j++)
			board[B][i][j] = s[j] - '0';
	}
	memset(grid, 1, sizeof(grid));
}


void simulation() {
	int find_dust = 0;
	int ans = 0;
	int move = 1;
	while (1) {
		// 0. 변수 초기화
		find_dust = 0;

		// 1. 현재 칸에 먼지가 있는지 확인
		if (grid[aris.r][aris.c]) {
			grid[aris.r][aris.c] = 0;
			// 먼지 발견했으므로 없이 갔던 영역 초기화
			memset(visited[B], 0, sizeof(visited[B]));
			find_dust = 1;
			move = 1;
		}
		// 2. 시계방향 회전
		if (find_dust) {
			aris.d = (aris.d + board[A][aris.r][aris.c]) % 4;
		}
		else {
			aris.d = (aris.d + board[B][aris.r][aris.c]) % 4;
		}
		// 3. 종료 조건 확인
		int nr = aris.r + dr[aris.d], nc = aris.c + dc[aris.d];
		if (!isValid(nr, nc))
			break;
		int clean = (find_dust + 1) % 2;
		if (clean && visited[clean][aris.d][aris.r][aris.c])
			break;
		// 4. 갔던 방향으로 이동
		visited[clean][aris.d][aris.r][aris.c] = move++;
		ans++;
		aris.r = nr, aris.c = nc;
	}

	cout << ans - move + 2 << '\n';
}


int main() {
	init();

	simulation();
}