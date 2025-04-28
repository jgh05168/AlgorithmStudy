/*
1. at와 gt는 가장 짧은 길이의 KOI 유전자임
2. aXt / gXc 에서 X가 유전자라면 저거도 유전자다. (chain가능)
3. X, Y가 KOI 조건을 만족하면 XY도 유전자다.

길이가 최대가 되는 KOI 유전자를 찾아 길이를 출력하자.

풀이 : dp
슬라이딩 윈도우 방식을 사용하여 문자열들이 조건을 만족하는지 찾기
*/

#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

string s;
int dp[501][501];


int topDown(int l, int r) {
	if (l >= r)
		return 0;
	if (dp[l][r] != -1)
		return dp[l][r];

	// 만약 dna를 찾았다면, 좌표압축 진행해주기
	if ((s[l] == 'a' && s[r] == 't') || (s[l] == 'g' && s[r] == 'c'))
		dp[l][r] = max(dp[l][r], topDown(l + 1, r - 1) + 2);

	// 부분으로 쪼개어서 dna가 있는지 탐색한 뒤, 합친 값을 저장하기
	for (int i = l; i < r; i++) {
		dp[l][r] = max(dp[l][r], topDown(l, i) + topDown(i + 1, r));
	}

	return dp[l][r];
}

int main() {
	cin >> s;
	memset(dp, -1, sizeof(dp));

	cout << topDown(0, s.length()) << '\n';
	

	return 0;
}