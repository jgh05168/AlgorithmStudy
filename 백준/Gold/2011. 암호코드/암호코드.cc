/*
2011 암호코드

경우가 두가지로 나뉜다.
1. 두자리 숫자로 합친 게 26 안에 들어오는가 ?
	-> 그러면 i - 2와 i - 1 값 더한 걸 불러와라
2. 두자리 숫자로 암호를 만들기 불가능하다 ?
	-> 그러면 그냥 i - 1값만 가져와라

----- 0에 대해서 처리를 잘 해주어야 한다. -----
0이 어디에 오느냐에 따라서 값이 많이 달라진다.
1. 0이 맨 앞에 오는 경우
2. 0이 왔을 때, 0 바로 앞자리와 합해서 26을 넘어서는 경우
3. 0앞에 0이 오는 경우
*/

#include <iostream>
#include <string>

using namespace std;

string s;
int dp[5001] = { 0, };

int main() {
	cin >> s;
	
	int n = s.length();
	int tmp;
	if (n == 1) {
		if (s[n - 1] - '0' > 0)	cout << 1 << '\n';
		else cout << 0 << '\n';
	}
	else {
		if (!(s[0] - '0')) cout << 0 << '\n';
		else {
			dp[0] = 1;
			dp[1] = 1;
			for (int i = 1; i < n; i++) {
				tmp = (s[i - 1] - '0') * 10 + (s[i] - '0');
				if (tmp > 26 && !(s[i] - '0')) {
					cout << 0 << '\n';
					exit(0);
				}
				else if (!tmp) {
					cout << 0 << '\n';
					exit(0);
				}
				else if (tmp > 26 || tmp < 10) dp[i + 1] = dp[i] % 1000000;
				else if (!(s[i] - '0')) dp[i + 1] = dp[i - 1] % 1000000;
				else dp[i + 1] = (dp[i] + dp[i - 1]) % 1000000;
			}


			cout << dp[n] << '\n';
		}

	}
	



	return 0;
}