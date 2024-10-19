/*
정확히 n분동안 동작시키고자 함
동작은 5개 존재한다.
+60
+10
-10
+1
-1
시간을 만들기 위해 눌러야 하는 버튼의 최소 횟수

방법이 여러가지인 경우, 사전순으로 가장 앞서는 방법을 출력
ADDH, ADDT, MINT, ADDO, MINO

한 번씩 순차적으로 계산하며, 가장 정답과 가까울때까지 반복해주기

*/

#include <iostream>

using namespace std;

int t, n;
int oven[5] = { -1, 1, -10, 10, 60 };

int main() {
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		int arr[5] = { 0, };

		int ans = 0;
		int tmp = 0;
		while (1) {

			int idx = 0;
			int min_v = ans + oven[0];
			for (int j = 1; j < 5; j++) {
				tmp = (ans + oven[j] > 0) ? ans + oven[j] : 0;
				if (abs(n - tmp) < abs(n - min_v)) {
					min_v = tmp;
					idx = j;
				}
			}
			arr[idx]++;

			ans = min_v;
			if (ans == n) break;
		}
		for (int j = 4; j >= 0; j--) cout << arr[j] << ' ';
		cout << '\n';
	}
}