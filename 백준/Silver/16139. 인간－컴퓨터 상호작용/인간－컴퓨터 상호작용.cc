/*
문자열에서 특정 알파벳이 몇 번 나타나는지 알아보기
문자열 구간 l ~ r  사이에 a가 몇 번 나타나는지 구하자
질문은 q번 존재함

풀이 : S <= 20만
q <= 20만

=> 전처리 과정이 필요함 
=> 문자열 순서대로 순회하며, 각 알파벳  별로 누적합을 구하자.
O(len(s) + q)
*/

#include <iostream>
#include <string>

using namespace std;

int n, l, r;
char a;
string s;
int prefix_sum[26][200001] = { 0, };


void init() {
	cin >> s;
	cin >> n;

	for (int i = 1; i < s.length() + 1; i++) {
		int idx = s[i - 1] - 'a';
		for (int j = 0; j < 'z' - 'a' + 1; j++) {
			if (j == idx)
				prefix_sum[j][i] = prefix_sum[j][i - 1] + 1;
			else
				prefix_sum[j][i] = prefix_sum[j][i - 1];
		}
	}

}


void simulation() {
	while (n--) {
		cin >> a >> l >> r;
		cout << prefix_sum[a - 'a'][r + 1] - prefix_sum[a - 'a'][l] << '\n';
	}
}

int main() {
	init();

	simulation();
}