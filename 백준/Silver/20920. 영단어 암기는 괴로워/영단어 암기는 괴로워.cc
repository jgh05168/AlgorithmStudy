/*
우선순위

1. 자주 나오는 단어일수록 앞에 배치한다.
2. 해당 단어의 길이가 길수록 앞에 배치한다.
3. 알파벳 사전 순으로 배치한다.
길이가 M 이상인 단어들만 외운다


-- map -- 
해시맵은 자주 수정 시 오히려 불필요한 연산을 수행하므로
조회가 많은 경우 사용한다.
& vector는 따로 만들어서 관리한다.
또한, 파이썬의 dictionary처럼 사용이 가능하다.
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;

vector<string> voca;
map<string, int> mp;

bool cmp(string a, string b) {
	if (a.size() == b.size() && mp[a] == mp[b]) {
		return a < b;
	}
	else if (mp[a] == mp[b]) {
		return a.size() > b.size();
	}
	return mp[a] > mp[b];
}

int main() {
	int n, m;
	string word;

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> word;
		if (word.length() < m) {
			continue;
		}
		else {
			if (mp.find(word) == mp.end()) {
				mp[word] = 0;				// 처음 보는 단어는 해시맵에 저장하고,
				voca.push_back(word);		// 단어장에 없으므로 push
			}
			mp[word]++;
		}
	}

	sort(voca.begin(), voca.end(), cmp);

	for (int i = 0; i < voca.size(); i++) {
		cout << voca[i] << "\n";
	}
	
	return 0;
}