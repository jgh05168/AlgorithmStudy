/*
구멍에 넣을 두 조각의 길이의 합은 구멍의 너비와 일치해야 함
항상 두 조각으로 막아야 함

구멍을 완벽하게 막을 수 있는 두 조각을 구하자

풀이 : 
두 조각은 합쳐서 x가 되야함
n <= 100만 이므로 O(n) 안에 끝내야함

투포인터 사용. 정렬 후 투포인터로 찾아가면서 값 찾기
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int x, n;
vector<int> lego_list;

int main() {

	while (1) {
		cin >> x;
		if (cin.eof())
			break;
		x *= 10000000;

		lego_list.clear();
		cin >> n;
		int tmp;
		for (int i = 0; i < n; i++) {
			cin >> tmp;
			lego_list.push_back(tmp);
		}

		int ans = -1;
		int a = 0, b = n - 1;
		int ans1, ans2;

		sort(lego_list.begin(), lego_list.end());

		while (a < b) {
			if (lego_list[a] + lego_list[b] > x)
				b--;
			else {
				if (lego_list[a] + lego_list[b] == x) {
					if (ans < abs(lego_list[a] - lego_list[b])) {
						ans1 = lego_list[a], ans2 = lego_list[b];
						ans = abs(lego_list[a] - lego_list[b]);
					}
				}
				a++;
			}
		}

		if (ans == -1)
			cout << "danger" << '\n';
		else
			cout << "yes" << ' ' << ans1 << ' ' << ans2 << '\n';

	}
}
