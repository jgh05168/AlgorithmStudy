/*
뒤집기

더 작은 영역을 뒤집어주면 된다.
-> 0과 1 카운트를 센 다음, 더 작은 녀석을 출력
*/

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	string s;
	cin >> s;

	int zero = 0;
	int one = 0;

	if (s[0] == '1') one++;
	else zero++;

	for (int i = 1; i < s.length(); i++) {
		if (s[i] != s[i - 1]) {
			if (s[i] == '1') one++;
			else zero++;
		}
	}

	cout << min(zero, one) << "\n";

	return 0;
}