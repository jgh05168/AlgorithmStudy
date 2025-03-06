/*
머리 : 심장 바로 윗 칸

풀이 : 
1. 머리 찾으면 심장 위치 찾기
2. 심장으로부터 팔 허리 찾기
3. 허리 끝나는 지점이라면 다리 찾기

*/

#include <iostream>
#include <string>

using namespace std;

int n;
string s;
char grid[1001][1001];

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < n;
}

int main() {
	cin >> n;
	int flag = 0;
	pair<int, int> heart;

	for (int i = 0; i < n; i++) {
		cin >> s;
		for (int j = 0; j < s.size(); j++) {
			grid[i][j] = s[j];
			if (grid[i][j] == '*' && !flag) {
				heart = { i + 1, j };
				flag = 1;
			}
		}
	}

	// 0. 심장 위치 출력
	cout << heart.first + 1 << ' ' << heart.second + 1 << '\n';
	
	// 1. 팔 위치 출력
	int r = heart.first, c = heart.second;
	int tmp = 0;
	while (isValid(r, c) && grid[r][c] == '*') {
		c--;
		tmp++;
	}
	cout << tmp - 1 << ' ';
	r = heart.first, c = heart.second;
	tmp = 0;
	while (isValid(r, c) && grid[r][c] == '*') {
		c++;
		tmp++;
	}
	cout << tmp - 1 << ' ';

	// 2. 허리 출력
	r = heart.first, c = heart.second;
	tmp = 0;
	while (isValid(r, c) && grid[r][c] == '*') {
		r++;
		tmp++;
	}
	cout << tmp - 1 << ' ';

	// 3. 다리 출력
	int br = r, bc = c;
	tmp = 0;
	bc--;
	while (isValid(br, bc) && grid[br][bc] == '*') {
		br++;
		tmp++;
	}
	cout << tmp << ' ';
	br = r, bc = c;
	tmp = 0;
	bc++;
	while (isValid(br, bc) && grid[br][bc] == '*') {
		br++;
		tmp++;
	}
	cout << tmp << ' ';

	return 0;
}