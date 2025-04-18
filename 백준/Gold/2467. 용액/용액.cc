/*
혼합 용액 : 각 용액의 특성값 합
특성값이 0에 가까운 용액을 만들려고 한다.

풀이 : 투포인터
0에 가까운거 투포인터로 찾아내면 되지 않나 ??
*/

#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;

int n;
ll arr[100001];

int main() {
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	int l = 0, r = n - 1;
	ll total = 9999999999999;
	pair<ll, ll> ans;
	while (l < r) {
		ll new_total = arr[l] + arr[r];
		if (abs(new_total) < total) {
			ans = { arr[l], arr[r] };
			total = abs(new_total);
		}
		if (new_total < 0)
			l++;
		else
			r--;
	}

	cout << ans.first << ' ' << ans.second << '\n';
}