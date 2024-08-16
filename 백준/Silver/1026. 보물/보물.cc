/*
뒤집기

더 작은 영역을 뒤집어주면 된다.
-> 0과 1 카운트를 센 다음, 더 작은 녀석을 출력
*/

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int a[51], b[51];

int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}
	
	sort(a, a + n);
	sort(b, b + n, greater<>());
	int ans = 0;
	for (int i = 0; i < n; i++) {
		ans += (a[i] * b[i]);
	}

	cout << ans;

	return 0;
}