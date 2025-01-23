/*
풀이 : 스택

*/

#include <iostream>
#include <stack>
#include <string>
#define INIT cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

string s;

int main() {
	INIT;
	cin >> s;

	stack<char> stack;
	int ans = 0;

	for (int i = 0; i < s.size(); i++) {
		if (s[i] == ')') {
			if (stack.empty() || stack.top() != '(')
				ans++;
			else
				stack.pop();
		}
		else
			stack.push(s[i]);
	}
	ans += stack.size();

	cout << ans << '\n';

	return 0;
}
