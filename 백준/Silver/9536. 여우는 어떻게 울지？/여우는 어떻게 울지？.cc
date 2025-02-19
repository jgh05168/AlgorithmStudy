#include <iostream>
#include <string>
#include <set>
#include <vector>
using namespace std;

int T;
string s;
int slen;
vector<string> vec;
set<string> st;
int idx;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	getline(cin, s);
	T = stoi(s);
	while (T--) {
		vec.clear(), st.clear();
		getline(cin, s);
		s += " ";
		slen = s.length();
		idx = 0;
		for (int i = 0; i < slen; i++) {
			if (s[i] == ' ') {
				vec.emplace_back(s.substr(idx, i - idx));
				idx = i + 1;
			}
		}

		getline(cin, s);
		while (s != "what does the fox say?") {
			s += " ";
			slen = s.length();
			idx = 0;
			vector<string> tmp;
			for (int i = 0; i < slen; i++) {
				if (s[i] == ' ') {
					tmp.emplace_back(s.substr(idx, i - idx));
					idx = i + 1;
				}
			}
			st.insert(tmp.back());

			getline(cin, s);
		}

		for (auto& ss : vec) {
			if (!st.count(ss)) cout << ss << ' ';
		}
		cout << '\n';
	}
    
    return 0;
}