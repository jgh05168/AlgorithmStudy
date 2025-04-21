#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string name[100];
string temp[100];
string s;


int main() {
	for (int i = 0; i < 100; ++i)
		name[i] = "";
    
	getline(cin, s);
	string type = "";
	bool check = false;
	int start = 0;
	int cnt = 0;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == ';')
			break;

		// 변수형 찾기
		if (!check && s[i] != ' ')
			type += s[i];
		if (s[i] == ' ')
		{
			cnt++;
			check = true;
			// name 찾기
			//name 수 저장을 위한 num
			int num = 0;
			for (int j = i + 1; j < s.size(); ++j) {
				if (s[j] == '*' || s[j] == '[' || s[j] == '&' || s[j] == ',' || s[j] == ';')
					break;
				name[start] += s[j];
				num++;
			}
			//거꾸로 붙힐 문자열 찾기
			for (int j = i + 1 + num; j < s.size(); ++j) {
				if (s[j] == ',' || s[j] ==';')
					break;
				temp[start] += s[j];
			}
			start++;
		}
	}
	for (int i = 0; i < cnt; ++i) {
		reverse(temp[i].begin(), temp[i].end());
		for (int j = 0; j < temp[i].size(); ++j) {
			if (temp[i][j] == '[') {
				temp[i][j] = ']';
			}
			else if (temp[i][j] == ']') {
				temp[i][j] = '[';
			}
		}
		cout << type << temp[i] << " " << name[i] <<  ";" << "\n";
	}
	
	return 0;
}