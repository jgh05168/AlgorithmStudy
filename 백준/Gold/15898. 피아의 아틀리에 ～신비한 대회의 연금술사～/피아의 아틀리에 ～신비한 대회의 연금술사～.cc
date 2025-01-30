/*
5 x 5 가마에 서로다른 재료 3개를 넣어 최고 품질의 폭탄을 만들어야함
주어진 재료 중 3개를 고른 뒤, 순서를 정해 가마에 넣기
가마의 각 칸 : 품질(숫자), 원소(색)
재료는 4 x 4

재료 : 
- 효능 : -9 ~ 9
- 원소 : 원소를 바꿀 수 있는 색
- 5 x 5 격자를 벗어나면 안된다. 회전은 가능함
	1. 격자의 품질은 재료의 효능이 더해진다.(음수인 경우 0, 초과인 경우 9)
	2. 격자의 색 : 원소가 흰색인 경우 그대로, 아닌 경우 재료의 원소와 같은 색

재료 3개를 넣어야만 폭탄이 만들어짐
(폭탄의 품질) = 7R + 5B + 3G + 2Y
품질의 최댓값을 구하자

풀이 : 브루트포스, 조합, 백트래킹
10^3 * 4 * 4

*/
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int n = 5, m; // 가마 크기 및 재료 개수
pair<int, char> ingredients[11][4][4][4]; // (효능, 원소) 정보를 담은 재료 (회전 포함)
pair<int, char> pot[5][5]; // 가마 상태 (품질, 원소)
int selected[11] = { 0, }; // 선택된 재료 여부
int used[3] = { 0, }; // 선택한 3개 재료의 인덱스 저장
unordered_map<char, int> scoreboard; // 점수 계산용


void rotate(int num, int idx) {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++)
			ingredients[num][idx][4 - 1 - j][i] = ingredients[num][idx - 1][i][j];
	}
}


void rotate_ingredients() {
	for (int i = 0; i < m; i++) {
		for (int d = 1; d < 4; d++) {
			rotate(i, d);
		}
	}
}

void get_ingredients(int depth, int &answer) {
	if (depth == 3) {
		// 최종 점수 계산
		int tmp = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				tmp += (pot[i][j].first * scoreboard[pot[i][j].second]);
			}
		}
		answer = max(answer, tmp);
		return;
	}

	int idx = used[depth]; // 현재 선택한 재료
	pair<int, char> return_pot[5][5]; // 백트래킹을 위한 원본 저장
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			return_pot[i][j] = pot[i][j];
		}
	}

	
	for (int sr = 0; sr <= 1; sr++) { // 2x2 내에서 시작 위치 선택
		for (int sc = 0; sc <= 1; sc++) {
			for (int d = 0; d < 4; d++) { // 회전 상태 탐색
				for (int r = 0; r < 4; r++) {
					for (int c = 0; c < 4; c++) {
						int nr = sr + r, nc = sc + c;
						pot[nr][nc].first += ingredients[idx][d][r][c].first;
						if (pot[nr][nc].first < 0)
							pot[nr][nc].first = 0;
						else if (pot[nr][nc].first > 9)
							pot[nr][nc].first = 9;
						if (ingredients[idx][d][r][c].second != 'W')
							pot[nr][nc].second = ingredients[idx][d][r][c].second;
					}
				}
				get_ingredients(depth + 1, answer);
				// 원상 복구
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						pot[i][j] = return_pot[i][j];
					}
				}
			}
		}
	}
}

void select_ingredients(int depth, int &answer) {
	if (depth == 3) {
		get_ingredients(0, answer);
		return;
	}
	for (int i = 0; i < m; i++) {
		if (!selected[i]) {
			selected[i] = 1;
			used[depth] = i;
			select_ingredients(depth + 1, answer);
			used[depth] = 0;
			selected[i] = 0;
		}
	}
}

void init() {
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
	cin >> m;
	for (int i = 0; i < m; i++) {
		for (int r = 0; r < 4; r++) {
			for (int c = 0; c < 4; c++)
				cin >> ingredients[i][0][r][c].first;
		}
		for (int r = 0; r < 4; r++) {
			for (int c = 0; c < 4; c++)
				cin >> ingredients[i][0][r][c].second;
		}
	}

	// 가마 초기화
	for (int r = 0; r < n; r++) {
		for (int c = 0; c < n; c++)
			pot[r][c] = { 0, 'W' };
	}
	scoreboard = { {'R', 7}, {'B', 5}, {'G', 3}, {'Y', 2} };
}

int main() {
	init();
	rotate_ingredients();
	int answer = 0;
	select_ingredients(0, answer);
	cout << answer << endl;
	return 0;
}
