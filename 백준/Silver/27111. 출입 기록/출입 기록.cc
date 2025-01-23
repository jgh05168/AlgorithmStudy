/*
출입 기록의 일부가 누락됨
n개 출입기록, 출입자가 출입한 시간순으로 기록됨
누락된 출입 기록의 최소 개수를 구하자

풀이 : dat

0 or 1 체크해가면서 확인해가기
- 0은 무조건 1일 때만 가능함
- 1이 두 번 나오면 안됨
*/

#include <iostream>
#define INIT cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

int n, a, b;
int arr[200001] = { 0, };

int main() {
	INIT;
	cin >> n;
	int ans = 0;

	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		if (b) {
			if (arr[a])
				ans++;
			else
				arr[a] = 1;
		}
		else {
			if (arr[a])
				arr[a] = 0;
			else
				ans++;
		}
	}

	for (int i = 0; i < 200001; i++) {
		if (arr[i])
			ans++;
	}

	cout << ans << '\n';
	return 0;
}
