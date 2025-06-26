#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int T;
string s;
int slen;
int cnt[128];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	while (T--) {
		memset(cnt, 0, sizeof(cnt));
		cin >> s;
		slen = s.length();
		bool chk = 1;

		for (int i = 0; i < slen; i++) {
			auto& l = s[i];
			cnt[l]++;
			if (cnt[l] == 3) {
				if (i + 1 == slen || s[i + 1] != l) chk = 0;
				else cnt[l] = 0, i++;
			}
		}

		if (chk) cout << "OK\n";
		else cout << "FAKE\n";
	}
}