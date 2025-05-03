/*
top-down dp로 가능할 듯 함
dp : 학생x높이

*/

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int n, m, h;
int dp[51][1001] = { 0, };
vector<vector<int>> students(51);


void init() {
	cin >> n >> m >> h;
	int tmp;
	for (int i = 0; i < n; i++) {
		while (cin >> tmp) {
			students[i].push_back(tmp);
		if (cin.peek() == '\n')
			break;
		}
	}
	memset(dp, -1, sizeof(dp));
}


int topDown(int depth, int value) {
	if (value > h) 
		return 0;
	if (depth == n) 
		return value == h ? 1 : 0;
	if (dp[depth][value] != -1)
		return dp[depth][value];
	
	
	int &cnt = dp[depth][value];
	cnt = 0;
	// 안쌓았을 때
	cnt += topDown(depth + 1, value);
	// 쌓았을 때
	for (int i = 0; i < students[depth].size(); i++) {
		cnt += topDown(depth + 1, value + students[depth][i]);
	}

	cnt %= 10007;

	return cnt;
}


void simulation() {
	cout << topDown(0, 0) << '\n';
}


int main() {
	init();

	simulation();

	return 0;
}