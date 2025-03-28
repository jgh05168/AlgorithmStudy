/*
dol 게임
현재 턴에서 1또는 3을 가져가보기
*/

#include <iostream>
#include <algorithm>
using namespace std;

int N;         
int DP[1000];

int main() {
	cin >> N;

	DP[0] = 0;
	DP[1] = 1;
	DP[2] = 2;

	for (int i = 3; i <= N; i++) {
		DP[i] = min(DP[i - 1] + 1, DP[i - 3] + 1);
	}

	// 게임 과정 횟수의 홀짝에 따라 승패 결정
	if (DP[N] % 2 == 1) {
		cout << "SK";
	}
	else {
		cout << "CY";
	}

	return 0;
}
