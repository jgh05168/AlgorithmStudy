/*
코너 A : 5000 코너 B : 1000

N일동안 매일 학식의 두 메뉴 중 정확히 하나를 골라 먹어야 함
모든 날의 각 메뉴가 얼마나 맛있을지 수치화함
N일 간 학식에 X원 이하를 써야함

풀이 : 정렬 후 사먹는것이다

*/


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, x;
int ans = 0;
vector<pair<int, int>> menu;

bool cmp(pair<int, int> a, pair<int, int> b) {
	int x = abs(a.first - a.second);
	int y = abs(b.first - b.second);
	if (x == y) {
		return a.second > b.second;
	}
	return x > y;
}

int main() {
	cin >> n >> x;
	for (int i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;
		menu.push_back({ a, b });
		ans += b;
	}

	sort(menu.begin(), menu.end(), cmp);

	int money = n * 1000;
	x -= money;
	for (int i = 0; i < n; i++) {
		if (x <= 0) {
			break;
		}
		if (menu[i].first > menu[i].second && x >= 4000) {
			ans += menu[i].first - menu[i].second;
			x -= 4000;
		}
	}

	cout << ans << '\n';
	return 0;
}
