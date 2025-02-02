/*
매일매일 약 반알을 먹는다.
한조각을 꺼낸 날에는 W를, 반조각을 꺼낸 날에는 H를 보낸다. 
총 2N일이 지나면 길이가 2N인 문자열이 만들어진다. 이 때, 가능한 서로다른 문자열의 개수는 총 몇 개일까 ?

풀이 : DP

top-down 2차원 배열로 경우의수 찾기
한알짜리 먹는건 행 증가, 반알짜리 먹는건 열 증가
*/

#include <iostream>
#include <cstring>
#define lli long long int

using namespace std;

int t, n;
lli dp[31][31];

lli top_down(int w, int h) {
	if (h > w || w > n)
		return 0;
	if (w + h == 2 * n)
		return 1;
	if (dp[w][h] != -1)
		return dp[w][h];
	dp[w][h] = top_down(w + 1, h) + top_down(w, h + 1);

	return dp[w][h];
}

int main() {
	while (1) {
		cin >> n;
		if (!n)
			break;
		memset(dp, -1, sizeof(dp));

		cout << top_down(0, 0) << '\n';
	}
	return 0;
}