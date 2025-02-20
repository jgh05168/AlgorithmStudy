/*
위에서 아래로 읽어서 하나의 문자열을 만들 수 있음

풀이 : 
- 중복이 있는지에 대해 체크해봐야함
-> unordered_map 사용하기. 만약 있다면 종료
*/

#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int n, m;
string s;

string arr[1001][1001];
vector<string> new_words;

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> s;
		for (int j = 0; j < m; j++) {
			arr[i][j] = s[j];
		}
	}

	// 문자열 생성
	for (int i = 0; i < m; i++) {
		s = "";
		for (int j = 1; j < n; j++) {
			s += arr[j][i];
		}
		new_words.push_back(s);
	}

	// 중복 찾기 시작
	int answer = 0;
	unordered_map<string, int> word_dict;	// 매 번 초기화 진행(메모리초과 남)
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < new_words.size(); j++) {
			if (word_dict[new_words[j]]) {
				cout << answer << '\n';
				exit(0);
			}
			word_dict[new_words[j]] = 1;
		}
		for (int j = 0; j < new_words.size(); j++) {
			new_words[j].erase(new_words[j].begin());
		}
		answer++;
		word_dict.clear();
	}
	cout << answer << '\n';

	return 0;
}
