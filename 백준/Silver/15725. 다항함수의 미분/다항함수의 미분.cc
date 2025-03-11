/*
파싱문제
x가 들어있는 인덱스 찾고 분기별로 조건문 걸면 될 듯 ?
*/

#include <iostream>
#include <string>

using namespace std;

int idx = -1;
string s; 

int main() {
    cin >> s;
	int slen = s.length();
    
	for (int i = 0; i < slen; i++) {
		if (s[i] == 'x')
            idx = i;
	}
    
	if (idx < 0) 
        cout << 0;
	else {
		if (idx == 0) 
            cout << 1;
		else if (s[idx - 1] == '+') 
            cout << 1;
		else if (s[idx - 1] == '-') 
            cout << -1;
		else 
            cout << stoi(s.substr(0, idx));
	}
    
    return 0;
}