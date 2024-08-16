/*
초콜릿 : 막대모양, 정사각형 n개로 이루어져 있음
초콜릿의 크기는 항상 2의 제곱 형태(2bit)


*/


#include <iostream>

using namespace std;

int a, b, idx = -1;
int tmp, k = 0;
int arr[21];


void solve(int i, int &cnt) {
	if (i < 0 || k == 0) {
		return;
	}
	// k를 줄여주기(0이 될 때까지 돌려주기)
	if (arr[i] <= k) {
		k -= arr[i];
	}
	// 아직 k가 남아있는 경우, 다시 solve로
	if (k) {
		solve(i - 1, ++cnt);
	}
}


int main() {
	cin >> k;
	int n = 1, ans = 0;
	int cnt = 0;

	// 배열 채워주기
	arr[0] = 1;
	for (int i = 1; i < 21; i++) {
		arr[i] = 1 << i;
		if (idx == -1 && arr[i] > k) {
			idx = i;
		}
	}
	for (int i = 0; i < 21; i++) {
		if (arr[i] == k) {
			cout << k << " " << 0 << "\n";
			return 0;
		}
	}
	// 줄여가면서 답 찾기
	solve(idx, cnt);

	cout << arr[idx] << " " << cnt << "\n";

	return 0;
}