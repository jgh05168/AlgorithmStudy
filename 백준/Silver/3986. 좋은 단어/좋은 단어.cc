#include <iostream>
#include <string>
#include <stack>

using namespace std;

int n;
string s;


int main() {
	cin >> n;


	int ans = 0;
	while (n--) {
		cin >> s;
		stack<char> arr;
		for (int i = 0; i < s.size(); i++) {
			if (arr.empty())
				arr.push(s[i]);
			else {
				if (arr.top() == s[i])
					arr.pop();
				else
					arr.push(s[i]);
			}
		}
		if (arr.empty())
			ans++;
	}

	cout << ans << '\n';

	return 0;
}