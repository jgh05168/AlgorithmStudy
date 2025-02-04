/*
중점을 0, 위를 1, 왼쪽을 2, 아래를 3, 오른쪽을 4

두 발이 동시에 움직이지 않는다 & 두 발이 같은 지점에 있는 것이 허락되지 않는다.

중앙 -> 다른 지점 : 2
인접 지점 (왼쪽 -> 위 / 아래) : 3
반대편 (왼쪽 -> 오른쪽) : 4

최소 힘을 출력하자

풀이 : 2차원 dp를 사용한다 ? (어떤 발을 움직였냐에 따라서 배열에 다르게 저장하기)
bottom-up 사용 가능 ? x, top-down이 더 쉽다.
	-> 발 바뀌는 경우에 동일하기 때문임
고려사항 : 현재 발이 어디에 있는지 어떤 발을 움직이는지에 따라서 달라진다.

*/

#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int n;
int arr[100002] = { 0, };
int dp[100002][5][5];
int idx = 0;

int getVal(int l, int r) {
	if (l == r)
		return 1;
	else if (!l)
		return 2;
	else if (abs(l - r) % 2)
		return 3;
	return 4;
}

int DDR(int depth, int left, int right) {
	if (depth == idx) 
		return 0;	// top-down은 내려가면서 값을 더해주기 때문에 초기값을 도착지에서 0으로 잡는다.
	if (dp[depth][left][right] != -1)
		return dp[depth][left][right];

	// 왼쪽으로 간 경우와 오른쪽으로 간 경우의 값을 비교하여 더해주며 내려가자
	int nleft = DDR(depth + 1, arr[depth], right) + getVal(left, arr[depth]);
	int nright = DDR(depth + 1, left, arr[depth]) + getVal(right, arr[depth]);

	dp[depth][left][right] = min(nleft, nright);
	
	return dp[depth][left][right];
}

int main() {
	
	while (1) {
		cin >> n;
		if (!n)
			break;
		arr[idx++] = n;
	}

	memset(dp, -1, sizeof(dp));
	cout << DDR(0, 0, 0) << '\n';
	return 0;
}