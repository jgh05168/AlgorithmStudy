/*
카드 합체 놀이
n장의 카드
1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다.
2. 계산한 값을 x번 카드와 y번 카드 두 장에 모두 덮어쓴다.

합체는 총 m번
합체 점수를 가장 작게 만들지

풀이 : 
m < 15000
O(2mlogm) = 약 12만 ? 충분할듯

자연수의 최댓값 <= 1000000
총 값이 int형의 최댓값보다 커진다. 
-> 15000000000 > 2147483647
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m;

int main() {
	cin >> n >> m;
	vector<long long> arr(n);

	for (int i = 0; i < n; i++) cin >> arr[i];

	int cnt = 0;
	while (cnt < m) {
		sort(arr.begin(), arr.end());
		long long sum = arr[0] + arr[1];
		arr.erase(arr.begin(), arr.begin() + 2);
		arr.push_back(sum);
		arr.push_back(sum);

		cnt++;
	}

	long long ans = 0;
	for (int i = 0; i < n; i++) {
		ans += arr[i];
	}

	cout << ans << '\n';

	return 0;
}
