/*
커서가 위치할 수 있는 곳  : L + 1
L : 왼쪽
D : 오른쪽
B : 커서 왼쪽 문자를 삭제(문장의 맨 앞이라면 무시)
P : $라는 문자를 커서 왼쪽에 추가
커서는 문장의 맨 뒤에 위치하고 있음

풀이 : 중간에 insert 하는게 더 시간 오래걸림 
스택 사용하기 : L이라면 push, D라면 pop, B면 그냥 삭제, P는 추가
*/

#include <iostream>
#include <string>
#include <queue>

using namespace std;

int n, m;
string s;

int main() {
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
	cin >> s >> m;
	n = s.size();

	deque<char> stackIn;
	deque<char> stackOut;
	for (int i = 0; i < n; i++)
		stackIn.push_back(s[i]);

	char order;
	char c;
	while (m--) {
		cin >> order;
		if (order == 'P') {
			cin >> c;
			stackIn.push_back(c);
		}
		else if (order == 'L') {
			if (stackIn.empty())
				continue;
			stackOut.push_front(stackIn.back());
			stackIn.pop_back();
		}
		else if (order == 'D') {
			if (stackOut.empty())
				continue;
			stackIn.push_back(stackOut.front());
			stackOut.pop_front();
		}
		else {
			if (stackIn.empty())
				continue;
			stackIn.pop_back();
		}
	}

	for (auto s : stackIn)
		cout << s;
	for (auto s : stackOut)
		cout << s;

	return 0;
}