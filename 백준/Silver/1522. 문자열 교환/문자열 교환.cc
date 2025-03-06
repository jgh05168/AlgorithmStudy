/*
문자열을 교환하자

풀이 : 슬라이딩 윈도우 ?
a의 개수를 센 뒤, 윈도우 크기 설정하고
b의 개수가 최소인 부분을 찾아내기
*/

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string s;

int main() {
	cin >> s;
	int cnt = 0;

	for (int i = 0; i < s.size(); i++) {
		if (s[i] == 'a')
			cnt++;
	}

	int ans = s.size();
	for (int i = 0; i < s.size(); i++) {
		int tmp = 0;
		for (int j = 0; j < cnt; j++) {
			if (s[(i + j) % s.size()] == 'b')
				tmp++;
		}
		ans = min(ans, tmp);
	}

	cout << ans << '\n';

	return 0;
}