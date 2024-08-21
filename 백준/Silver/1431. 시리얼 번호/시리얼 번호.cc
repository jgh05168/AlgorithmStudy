/*
1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다. 
2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 갖는 것이 먼저 온다
	- 숫자만 비교
3. 사전순으로 비교
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector<string> serial_list;

bool cmp(string x, string y) {
	if (x.length() != y.length()) {
		return x.length() < y.length();
	}
	else {
		int x_n = 0;
		int y_n = 0;
		for (int i = 0; i < x.length(); i++) {
			if (0 <= x[i] - '0' && x[i] - '0' < 10) {
				x_n += x[i] - '0';
			}
		}
		for (int i = 0; i < y.length(); i++) {
			if (0 <= y[i] - '0' && y[i] - '0' < 10) {
				y_n += y[i] - '0';
			}
		}
		if (x_n != y_n) {
			return x_n < y_n;
		}
		else {
			return x < y;
		}
	}
}

int main() {
	cin >> n;
	string tmp;

	for (int i = 0; i < n; i++) {
		cin >> tmp;
		serial_list.push_back(tmp);
	}

	sort(serial_list.begin(), serial_list.end(), cmp);

	for (int i = 0; i < n; i++) {
		cout << serial_list[i] << '\n';
	}

	return 0;
}