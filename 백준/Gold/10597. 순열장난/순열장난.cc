/*
모든 수는 10진수, 공백으로 분리됨
순열을 복구하자

풀이: 
중복된 값이 없는건가 ? 흠

입력 - 최대 50개의 수로 이루어짐 == n <= 50
먼저 s의 길이를 구한 뒤 순열 구하기

dfs
*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string s;
int n;
int input_length[51] = { 0, };
int dat[51] = { 0, };
vector<int> answer;

void get_tensor() {
	int l = 0;
	for (int i = 1; i < 51; i++) {
		if (i < 10)
			l += 1;
		else
			l += 2;
		input_length[i] = l;
	}
}

int dfs(int idx) {
	if (idx == s.size())
		return 1;

	int num = 0;
	for (int len = 1; len <= 2; len++) {
		if (idx + len > s.size())
			break;
		if (s[idx] == '0')
			break;

		num = num * 10 + (s[idx + len - 1] - '0');

		if (num > n)
			break;

		if (!dat[num]) {
			dat[num] = 1;
			answer.push_back(num);
			if (dfs(idx + len))
				return 1;
			answer.pop_back();
			dat[num] = 0;
		}
	}
	return 0;
}

int main() {
	get_tensor();
	cin >> s;

	// s의 길이에 맞는 n 찾기
	for (int i = 1; i < 51; i++) {
		if (input_length[i] == s.length()) {
			n = i;
			break;
		}
	}

	dfs(0);

	for (auto v : answer)
		cout << v << ' ';

	return 0;
}
