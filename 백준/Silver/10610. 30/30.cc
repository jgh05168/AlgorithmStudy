#include <iostream>
#include <algorithm>
using namespace std;

string s;

int main() {
	cin >> s;

	int sum = 0;
	int cnt = 0;
	for (int i = 0; i < s.size(); i++) {
		sum += s[i] - '0';
		if (s[i] - '0' == 0) {
			cnt = 1;
		}
	}

	if (sum % 3 != 0 || cnt == 0) {
		cout << "-1" << endl;
		return 0;
	}

	sort(s.begin(), s.end(), greater<>());
	
	cout << s << '\n';
	
	return 0;
}