/*
입력받은 영단어의 철자들로 만들 수 있는 모든 단어 출력하기
같은 단어가 나올 수도 있는데, 이런 경우에는 한 번만 출력하기

풀이 : 조합, 정렬
20!
*/

#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int n, len;
string s;
int dat[21] = { 0, };

void make_anagram(int depth, string anagram) {
	if (depth == len) {
		cout << anagram << '\n';
		return;
	}

	char last_used = '\0';  // 직전에 사용한 문자 저장
	for (int i = 0; i < len; i++) {
		if (!dat[i] && (i == 0 || s[i] != s[i - 1] || dat[i - 1])) {
			dat[i] = 1;
			make_anagram(depth + 1, anagram + s[i]);
			dat[i] = 0;
			last_used = s[i];
		}
	}
}


int main() {
	cin.tie(0); ios::sync_with_stdio(false);
	cin >> n;
	while (n--) {
		memset(dat, 0, sizeof(dat));
		cin >> s;
		len = s.length();
		
		// 0. 정렬
		sort(s.begin(), s.end());
		
		// 1. 애너그램 생성
		make_anagram(0, "");

	}
	return 0;
}