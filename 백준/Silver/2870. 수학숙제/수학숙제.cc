/*
숫자와 알파벳 소문자 n줄
숫자를 모두 찾은 뒤, 비내림차순으로 정렬
숫자 앞 0은 정리하면서 생략 ㄱㄴ

숫자가 나오는 경우, 가능한 가장 큰 숫자를 찾아야 한다.
*/

#include <iostream>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<string>
using namespace std;

vector<string> v;

bool cmp(string a, string b) {  //문자열 정렬 기준
	if (a.size() == b.size())
		return a < b;
	else
		return a.size() < b.size();
}

string zero(string str) {
	string num = "";
	int flag = 0;  //0저장해도 되는지 flag
	for (int i = 0; i < str.size(); i++) {
		if (str[i] != '0') {
			num += str[i];
			flag = 1;
		}
		else if (flag && str[i] == '0')
			num += '0';
	}
	if (num == "")  //모든 수가 0이므로 0 반환
		return "0";
	else
		return num;
}

int main() {
	int T;
	string str, num = "";
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> str;

		num = "";
		for (int j = 0; j < str.size(); j++) {
			if (str[j] >= '0' && str[j] <= '9')  //일단 모든 숫자를 다 저장해 준다
				num += str[j];
			else {
				if (num != "")
					v.push_back(zero(num));
				num = "";
			}
		}
		if (num != "")  //남은 문자열도 확인해 준다
			v.push_back(zero(num));

	}
	sort(v.begin(), v.end(), cmp);  //새로운 정렬 기준을 바탕으로 정렬
	for (auto k : v)
		cout << k << "\n";
}