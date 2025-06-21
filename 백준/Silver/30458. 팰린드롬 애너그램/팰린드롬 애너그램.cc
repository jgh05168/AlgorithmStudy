#include <iostream>
#include <string>
using namespace std;

int n, i, cnt[26] = { 0 };


int main() {
	string s;

	cin >> n >> s;
	for (i = 0; i < n; i++)
		cnt[s[i] - 'a']++;
	if (n % 2 == 1) 
		cnt[s[n / 2] - 'a']--;

	for (i = 0; i < 26; i++) {
		if (cnt[i] % 2 == 1) {
			cout << "No";
			return 0;
		}
	}
	cout << "Yes";
}