/*

*/

#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int n = 0;
string s, tmp = "";

int main() {
	
	string ans;
	while (1) {
		cin >> s;

		if (s == "E-N-D")
			break;
		tmp = "";
		for (int i = 0; i < s.size(); i++) {
			if ((0 <= s[i] - 'A' && s[i] - 'A' < 26) || (0 <= s[i] - 'a' && s[i] - 'a' < 26) || s[i] == '-') {
				tmp += tolower(s[i]);
			}
			else {
				if (tmp.size() > n) {
					n = tmp.size();
					ans = tmp;
				}
				tmp = "";
			}
		}
		if (tmp.size() > n) {
			n = tmp.size();
			ans = tmp;
		}
	}

	cout << ans << '\n';

	return 0;
}