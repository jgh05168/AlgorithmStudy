/*
색종이의 크기는 다섯 종류가 존재함. 각 종류의 색종이는 5개씩 있음

10 x 10 종이 위에 덮을 수 있는 색종이 최소 개수를 구하자

풀이 : 백트래킹
- 작은 색종이부터 사용하기
- 
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n = 10, m;
int grid[11][11];
int visited[11][11];
int papers[6] = { 5, 5, 5, 5, 5, 5 };

int answer = 99999999;

vector<pair<int, int>> ones;


bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < n;
}

void attach(int r, int c, int paper_size) {
	for (int nr = 0; nr < paper_size; nr++) {
		for (int nc = 0; nc < paper_size; nc++) {
			visited[r + nr][c + nc] = 1;
		}
	}
	papers[paper_size]--;
}

void detach(int r, int c, int paper_size) {
	for (int nr = 0; nr < paper_size; nr++) {
		for (int nc = 0; nc < paper_size; nc++) {
			visited[r + nr][c + nc] = 0;
		}
	}
	papers[paper_size]++;
}


// 해당 사이즈 내에 있는 모든 1에 성립해야함
int check_size(int r, int c, int paper_size) {
	for (int nr = 0; nr < paper_size; nr++) {
		for (int nc = 0; nc < paper_size; nc++) {
			// 사이즈 초과하거나, 1이 아니거나, 이미 붙인 자리라면 종료
			if (!isValid(r + nr, c + nc) || !grid[r + nr][c + nc] || visited[r + nr][c + nc])
				return 0;
		}
	}
	return 1;
}


void recur(int depth, int idx, int one_cnt) {
	// 가지치키 : 색종이 answer보다 많이 썼을 때
	if (answer < depth)
		return;
	// 종료 조건 : 모든 색종이 다 붙였을 때
	if (one_cnt == m) {
		answer = min(answer, depth);
		return;
	}
	// 1 있는 부분 모두 체크 : O(100)
	for (int i = idx; i < m; i++) {
		int r = ones[i].first, c = ones[i].second;
		// 색종이 칠 한 부분이 아니라면 하나씩 붙여보기
		if (!visited[r][c]) {
			// 사이즈 별로 붙여보기 : O(5)
			for (int width = 5; width > 0; width--) {
				if (!papers[width])
					continue;
				// 붙일 수 있는 사이즈인지 체크 : O(5 x 5)
				if (check_size(r, c, width)) {
					attach(r, c, width);
					recur(depth + 1, i + 1, one_cnt + width * width);
					detach(r, c, width);
				}
			}
			// 사이즈 다 붙일 수 있는지 체크 다 되었으면 return 해주기(안그러면 1 있는 부분 체크 안하고 넘어간다.)
			return;
		}
	}
}

int main() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> grid[i][j];
			if (grid[i][j])
				ones.push_back({ i, j });
		}
	}
	m = ones.size();

	// 시작
	recur(0, 0, 0);		// depth, idx
	if (answer == 99999999)
		answer = -1;
	cout << answer << '\n';

	return 0;
}