/*
트리는 N개의 레벨로 이루어져 있음
빨 파 초 장난감 갖고있음

레벨 K에는 딱 K개의 장난감이 있어야 ㅎㄴ다.
각 레벨에 놓으려고 선택한 색이 있으면 그 색의 장난감 수는 같아야한다.

경우의 수 출력하기

DP
정답은 long long 크기

DP 배열 크기는 ? 흠 .. 몇번째 층에 어떤 조합으로 들어가는지 체크
10 x 100 x 100 x 100
*/
#include <iostream>
#include <cstring>
#define ll long long
using namespace std;

int n, red, green, blue;
ll dp[11][101][101][101];  // dp[depth][r][g][b]
ll factorial[11];

void init() {
	cin >> n >> red >> green >> blue;
	memset(dp, -1, sizeof(dp));

	factorial[0] = 1;
	for (int i = 1; i <= 10; ++i) {
		factorial[i] = factorial[i - 1] * i;
	}
}

ll getComb(int depth, int r, int g, int b) {
	return factorial[depth] / factorial[r] / factorial[g] / factorial[b];
}

ll topDown(int depth, int r, int g, int b) {
	if (depth > n)
		return 1;

	ll &ret = dp[depth][r][g][b];
	if (ret != -1)
		return ret;

	ret = 0;

	// 1색
	if (red - r >= depth)
		ret += topDown(depth + 1, r + depth, g, b);
	if (green - g >= depth)
		ret += topDown(depth + 1, r, g + depth, b);
	if (blue - b >= depth)
		ret += topDown(depth + 1, r, g, b + depth);

	// 2색 (짝수만 가능)
	if (depth % 2 == 0) {
		int half = depth / 2;
		if (red - r >= half && green - g >= half)
			ret += getComb(depth, half, half, 0) * topDown(depth + 1, r + half, g + half, b);
		if (red - r >= half && blue - b >= half)
			ret += getComb(depth, half, 0, half) * topDown(depth + 1, r + half, g, b + half);
		if (green - g >= half && blue - b >= half)
			ret += getComb(depth, 0, half, half) * topDown(depth + 1, r, g + half, b + half);
	}

	// 3색 (3의 배수일 때만 가능)
	if (depth % 3 == 0) {
		int third = depth / 3;
		if (red - r >= third && green - g >= third && blue - b >= third)
			ret += getComb(depth, third, third, third) * topDown(depth + 1, r + third, g + third, b + third);
	}

	return ret;
}

void solution() {
	cout << topDown(1, 0, 0, 0) << '\n';
}

int main() {
	init();
	solution();
}
