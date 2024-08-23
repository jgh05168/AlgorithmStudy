/*
볼 모으기

1. 바로 옆에 다른 색의 공이 있다면, 뛰어넘을 수 있다. 
2. 옮길 수 있는 볼의 색은 한가지이다. 

풀이 :
< 500000
두가지 볼 모두 옮겨봐야 함

뒤에서부터 옮긴다.
숫자를 세어가면서 옮길 수 있는 횟수를 카운트하기
500000 x 2 면 모두 셀 수 있다.
*/

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int n;
string s;

int main() {
	cin >> n;
	cin >> s;

	int ans = n;
	// 빨간공부터 뒤에서부터 옮겨보기
	int r_red = 0;
	bool cnt = false;
	for (int i = n - 1; i >= 0; i--) {
		if (s[i] == 'R' && cnt) r_red++;
		if (s[i] == 'B') cnt = true;
	}

	// 빨간공 앞에서부터 옮겨보기
	int f_red = 0;
	cnt = false;
	for (int i = 0; i < n; i++) {
		if (s[i] == 'R' && cnt) f_red++;
		if (s[i] == 'B') cnt = true;
	}

	// 파란공 뒤에ㅓㅅ부터 옮기기
	int r_blue = 0;
	cnt = false;
	for (int i = n - 1; i >= 0; i--) {
		if (s[i] == 'B' && cnt) r_blue++;
		if (s[i] == 'R') cnt = true;
	}

	// 파란공 앞에서부터 옮기기
	int f_blue = 0;
	cnt = false;
	for (int i = 0; i < n; i++) {
		if (s[i] == 'B' && cnt) f_blue++;
		if (s[i] == 'R') cnt = true;
	}

	cout << min(ans, min(min(f_red, f_blue), min(r_red, r_blue))) << '\n';
}