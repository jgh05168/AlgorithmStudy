/*
- 파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘
- 보기 편하게 확장자들을 사전 순으로 정렬해줘

풀이 : map

*/

#include <iostream>
#include <string>
#include <map>

using namespace std;

int n;
string s;
map<string, int> ans;

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> s;
		int idx = s.find('.');
		string key = "";
		for (int j = idx + 1; j < s.length(); j++)
			key += s[j];
		ans[key]++;
	}

	for (auto key : ans)
		cout << key.first << ' ' << key.second << '\n';


	return 0;
}