/*
- r1행부터 r2행까지 차례대로 출력한다
- 각 원소는 공백으로 구분함
- 모든 행은 같은 길이를 갖는다
- 공백의 길이는 최소로 해야한다
- 모든 숫자 길이는 같아야한다
- 수의 길이가 가장 길이가 긴 수보다 작다면 왼쪽부터 공백삽입
	- 오른쪽으로 정렬

풀이:
구현
배열이 10000 x 10000이기 때문에 공간복잡도 생각해야한다
	-> 배열에 먼저 값 넣어두면 멤초남
일단 입력부터 받고, 출발지, 도착지 생각하기
범위 넘어가는 값이면 출력종료하기

*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;


int r1, r2, c1, c2;
int dr[4] = { 0, -1, 0, 1 };
int dc[4] = { 1, 0, -1, 0 };


bool check_(int r, int c) {
	return r1 <= r && r < r2 && c1 <= c && c < c2;
}


int main() {
	cin >> r1 >> c1 >> r2 >> c2;
	// 방향 세 번 틀었으면, 그다음 방향은 한 칸씩 더 가주기
	// 여기서 한 번 더 간 것도 방향에 추가해야된다.

	// 초기 1 위치 잡아주기
	int r = -r1; int c = -c1;
	r2 += -r1 + 1; r1 = 0;
	c2 += -c1 + 1; c1 = 0;
	vector<vector<int>> grid(r2 - r1, vector<int>(c2 - c1));
	int cnt = 0;
	int check_dir = 0; int move = 1;
	int d = 3;	// 무조건 오른쪽부터 이동한다.
	int number = 1;
	int nr, nc;
	if (check_(r, c)) {
		grid[r][c] = 1;
		cnt++;
	}
	// 배열 탐색 시작
	while (cnt < (r2 - r1) * (c2 - c1)) {
		d = (d + 1) % 4;
		check_dir++;
		if (check_dir > 2) {
			check_dir = 1;
			move++;
		}
		for (int i = 0; i < move; i++) {
			number++;
			nr = r + dr[d];
			nc = c + dc[d];
			if (check_(nr, nc)) {
				grid[nr][nc] = number;
				cnt++;
			}
			r = nr;
			c = nc;
			if (cnt >= (r2 - r1) * (c2 - c1))
				break;
		}
	}

	// 자릿수확인
	string last_number = to_string(number);
	for (int i = 0; i < r2; i++) {
		for (int j = 0; j < c2; j++) {
			string tmp = to_string(grid[i][j]);
			while (tmp.size() != last_number.size())
				tmp = ' ' + tmp;
			cout << tmp << ' ';
		}
		cout << '\n';
	}

	return 0;
}