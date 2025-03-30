/*
13:55 시작

칸에는 상어가 최대 한 마리 들어있을 수 있음
상어 정보 : 크기, 속도

낚시왕 초기 위치 : 1번 열의 한 칸 왼 쪽 (-1)
낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

1. 낚시왕이 오른쪽으로 한 칸 이동함
2. 낚시왕의 열에 있는 상어 중 땅과 제일 가까운 상어를 잡는다.
	- 잡으면 격자판에서 상어 사라짐
3. 상어 이동한다.
	- 입력으로 주어진 속도로 이동
	- 경계를 넘는 경우, 방향을 바꿔 반대 방향으로 이동한다.
4. 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 존재할 수 있다. 이 때는 크기가 큰 상어가 나머지 상어를 모두 잡아먹는다.

풀이 : 시뮬레이션
상어 정보 : r, c, 속도, 방향, 크기, 살아있는지 여부
모든 상어는 동시에 이동함 : 새로운 맵에다가 정보를 업데이트 해야함
*/

#include <iostream>
#include <cstring>

using namespace std;

struct shark {
	int r, c, s, d, z, isDead;
};

int R, C, M;
int grid[101][101];
int tmp_grid[101][101];
shark shark_list[10001];

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, 1, -1 };
int dir_dict[4] = { 1, 0, 3, 2 };


bool isValid(int r, int c) {
	return 0 <= r && r < R && 0 <= c && c < C;
}


void init() {
	cin >> R >> C >> M;
	int r, c, s, d, z;
	for (int i = 1; i < M + 1; i++) {
		cin >> r >> c >> s >> d >> z;
		shark_list[i].r = r - 1;
		shark_list[i].c = c - 1;
		shark_list[i].s = s;
		shark_list[i].d = d - 1;
		shark_list[i].z = z;
		grid[shark_list[i].r][shark_list[i].c] = i;
	}
}


int catch_shark(int c) {
	for (int r = 0; r < R; r++) {
		if (grid[r][c]) {
			shark_list[grid[r][c]].isDead = 1;
			int size = shark_list[grid[r][c]].z;
			grid[r][c] = 0;
			return size;
		}
	}
	return 0;
}


void shark_move() {
	memset(tmp_grid, 0, sizeof(tmp_grid));

	for (int idx = 1; idx < M + 1; idx++) {
		if (shark_list[idx].isDead)
			continue;
		// 움직임 시작
		int r = shark_list[idx].r, c = shark_list[idx].c;
		int d = shark_list[idx].d;
		int nr = r, nc = c;
		int s = shark_list[idx].s;
		// 얼만큼 움직여야하는지 구해줘야 함
		if (!d || d == 1) {
			int rotate = (R - 1) * 2;
			if (s >= rotate) 
				s %= rotate;

			for (int j = 0; j < s; j++) {
				nr = r + dr[d];
				nc = c + dc[d];
				if (nr < 0) {
					d = dir_dict[d];
					nr += 2;
				}
				if (nr >= R) {
					d = dir_dict[d];
					nr -= 2;
				}
				r = nr;
				c = nc;
			}
		}
		else {
			int rotate = (C - 1) * 2;
			if (s >= rotate)
				s %= rotate;

			for (int j = 0; j < s; j++) {
				nr = r + dr[d];
				nc = c + dc[d];
				if (nc < 0) {
					d = dir_dict[d];
					nc += 2;
				}
				if (nc >= C) {
					d = dir_dict[d];
					nc -= 2;
				}
				r = nr;
				c = nc;
			}
		}
		// 새로운 그리드에 저장
		if (tmp_grid[nr][nc]) {
			int nidx = tmp_grid[nr][nc];
			if (shark_list[idx].z > shark_list[nidx].z) {
				tmp_grid[nr][nc] = idx;
				shark_list[nidx].isDead = 1;
			}
			else {
				shark_list[idx].isDead = 1;
			}
		}
		if (!shark_list[idx].isDead) {
			tmp_grid[nr][nc] = idx;
			shark_list[idx].r = nr;
			shark_list[idx].c = nc;
			shark_list[idx].d = d;
		}
	}

	// grid 업데이트
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++)
			grid[i][j] = tmp_grid[i][j];
	}
}



void simulation() {
	int fisher = -1;
	int answer = 0;

	while (fisher < C) {
		// 1. 어부 이동
		fisher++;
		// 게임 종료 조건
		if (fisher >= C)
			break;

		// 2. 상어 잡기
		answer += catch_shark(fisher);

		// 3. 상어 이동
		shark_move();

	}

	cout << answer << '\n';
}


int main() {
	init();

	simulation();

	return 0;
}