/*
10:27 시작

k개의 미생물 군집
n x n 개의 동일한 크기의 정사각형 셀들로 이뤄져 있음 & 가장 바깥쪽 가장자리 부분은 못 감

1. 군집 정보 : r, c, 미생물 수, 이동 방향
2. 각 군집들은 한시간마다 다음 셀로 이동
	- 약품이 칠해진 셀에 도착한다면, 미생물 절반이 죽고 방향 반대로 수정
		- 소수점 이하를 버림
	- 살아남은 미생물이 0이라면 군집 소멸
3. 두 개 이상의 군집이 한군데로 모이게 된다면, 군집이 합쳐지게 된다.
	- 이동 방향은 미생물 수가 가장 많은 군집의 이동방향을 따른다.

M 시간 후 남아잇는 미생물 총 합

풀이 : 
군집 정보 : r, c, 미생물 수, 이동 방향, 사라짐 여부
미생물은 동시에 움직임
필요 정보 : 군집 정보 grid, 미생물 정보
1000 x 1000
*/

#include <iostream>
#include <cstring>
#define GRID_SIZE 101
#define MAX_SIZE 1001

using namespace std;

struct association {
	int r, c, cnt, d, isDead;
};

int t, n, m, k;
int grid[GRID_SIZE][GRID_SIZE];
int tmp_grid[GRID_SIZE][GRID_SIZE];
int cnt_grid[GRID_SIZE][GRID_SIZE];
association association_list[MAX_SIZE];

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
int dir_dict[4] = { 1, 0, 3, 2 };

bool isValid(int r, int c) {
	if (!r || r == n - 1 || !c || c == n - 1)
		return false;
	return true;
}


void init() {
	memset(grid, 0, sizeof(grid));
	memset(association_list, 0, sizeof(association_list));

	cin >> n >> m >> k;
	for (int i = 1; i < k + 1; i++) {
		cin >> association_list[i].r >> association_list[i].c >> association_list[i].cnt >> association_list[i].d;
		association_list[i].d--;
		grid[association_list[i].r][association_list[i].c] = i;
	}
}

void move_association() {
	memset(tmp_grid, 0, sizeof(tmp_grid));
	memset(cnt_grid, 0, sizeof(cnt_grid));
	for (int idx = 1; idx < k + 1; idx++) {
		// 사라진 미생물은 continue
		if (association_list[idx].isDead)
			continue;

		// 2. 이동 시작
		int r = association_list[idx].r, c = association_list[idx].c;
		int d = association_list[idx].d;

		int nr = r + dr[d], nc = c + dc[d];
		if (!isValid(nr, nc)) {
			association_list[idx].cnt /= 2;
			// 모든 미생물이 죽은 경우라면, 군집 삭제
			if (!association_list[idx].cnt) {
				association_list[idx].isDead = 1;
				continue;
			}
			association_list[idx].d = dir_dict[d];
		}
		association_list[idx].r = nr;
		association_list[idx].c = nc;

		// 만약 현재 공간에 미생물이 있는 경우
		if (tmp_grid[nr][nc]) {
			// 개수 합치기
			cnt_grid[nr][nc] += association_list[idx].cnt;
			int nidx = tmp_grid[nr][nc];
			// 어떤 군집이 더 큰 지 체크하기
			if (association_list[idx].cnt < association_list[nidx].cnt) {
				association_list[idx].isDead = 1;
			}
			else {
				association_list[nidx].isDead = 1;
				tmp_grid[nr][nc] = idx;
			}
		}
		else {
			tmp_grid[nr][nc] = idx;
			cnt_grid[nr][nc] += association_list[idx].cnt;
		}
	}
	// 모든 이동이 끝난 뒤, grid 새로 업데이트
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			grid[i][j] = tmp_grid[i][j];
			if (tmp_grid[i][j])
				association_list[tmp_grid[i][j]].cnt = cnt_grid[i][j];
		}
	}
}


int simulation() {
	int ans = 0;
	while (m--) {
		// 1. 군집 이동
		move_association();
	}

	// 3. 남은 미생물 수 총 합 세기
	for (int idx = 1; idx < k + 1; idx++) {
		if (association_list[idx].isDead)
			continue;
		ans += association_list[idx].cnt;
	}

	return ans;
}


int main() {
	cin >> t;
	for (int tc = 1; tc < t + 1; tc++) {
		init();

		cout << '#' << tc << ' ' << simulation() << '\n';
	}
	
	return 0;
}