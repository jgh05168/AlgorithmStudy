/*
n x n, 빈칸 or 건물
수제폭탄을 건물이 없는 곳에 설치함
충격파는 각 방향에 대해 퍼져나가는데, 닿은 건물은 파괴되어 건물 잔해가 된다.

현장의 재구성

2000 x 2000
400만임
-> 교집합을 찾아야 함

*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n;
vector<int> rows;
vector<int> cols;
char grid[2001][2001];
int check[2001][2001];


void init() {
	cin >> n;
	string tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		for (int j = 0; j < n; j++) {
			grid[i][j] = tmp[j];
		}
	}
}


void simulation() {
	int flag = 0;
	// 열 체크
	for (int i = 0; i < n; i++) {
		flag = 0;
		for (int j = 0; j < n; j++) {
			if (grid[i][j] == 'X')
				flag = 0;
			else if (grid[i][j] == 'O')
				flag = 1;
			else {
				if (!flag)
					check[i][j] += 1;
			}
		}
		flag = 0;
		for (int j = n - 1; j >= 0; j--) {
			if (grid[i][j] == 'X')
				flag = 0;
			else if (grid[i][j] == 'O')
				flag = 1;
			else {
				if (!flag)
					check[i][j] += 1;
			}
		}
	}

	// 행 체크
	for (int j = 0; j < n; j++) {
		flag = 0;
		for (int i = 0; i < n; i++) {
			if (grid[i][j] == 'X')
				flag = 0;
			else if (grid[i][j] == 'O')
				flag = 1;
			else {
				if (!flag)
					check[i][j] += 1;
			}
		}
		flag = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (grid[i][j] == 'X')
				flag = 0;
			else if (grid[i][j] == 'O')
				flag = 1;
			else {
				if (!flag)
					check[i][j] += 1;
			}
		}
	}

	// 확인
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (check[i][j] == 4) {
				grid[i][j] = 'B';
			}
		}
	}


	// 출력
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << grid[i][j];
		}
		cout << '\n';
	}
}


int main() {

	init();

	simulation();

}
