/*
n개의 팀, 앉은 자리는 다름. 풍선은 A와 B 방에 보관되어있음

입력 정보 : 달아줘야 하는 풍선의 수, A / B 거리 주어짐
이 때, 모든 풍선을 달아주는데 필요한 이동거리의 최솟값 출력

이동 거리 : 팀이 A와 B로부터 떨어진 거리와 같다.
풍선을 달아주는 사람은 매우 많고, 한 번에 하나의 풍선만 들고 이동할 수 있다.

풀이 : 단순히 이동거리가 짧은 순으로 그리디하게 주면 안될 것 같음
- 극명하게 차이가 나는 경우라면 문제가 되기 때문

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct balloon {
	int cnt, a_dist, b_dist;
};

int n, a, b;
vector<balloon> balloon_list;


bool cmp(balloon a, balloon b) {
	return abs(a.a_dist - a.b_dist) > abs(b.a_dist - b.b_dist);
}


void init() {
	balloon_list.clear();
	int c, ad, bd;
	for (int i = 0; i < n; i++) {
		cin >> c >> ad >> bd;
		balloon_list.push_back({ c, ad, bd });
	}

	sort(balloon_list.begin(), balloon_list.end(), cmp);
}


void simulation() {
	while (1) {
		cin >> n >> a >> b;
		if (!n)
			break;

		/* 입력받고 시작하기 */
		init();

		int ans = 0;
		for (int i = 0; i < balloon_list.size(); i++) {
			if (balloon_list[i].a_dist < balloon_list[i].b_dist) {
				if (a < balloon_list[i].cnt) {
					ans += balloon_list[i].a_dist * a;
					ans += balloon_list[i].b_dist * (balloon_list[i].cnt - a);
					b -= (balloon_list[i].cnt - a);
					a = 0;
				}
				else {
					ans += balloon_list[i].a_dist * balloon_list[i].cnt;
					a -= balloon_list[i].cnt;
				}
			}
			else {
				if (b < balloon_list[i].cnt) {
					ans += balloon_list[i].b_dist * b;
					ans += balloon_list[i].a_dist * (balloon_list[i].cnt - b);
					a -= (balloon_list[i].cnt - b);
					b = 0;
				}
				else {
					ans += balloon_list[i].b_dist * balloon_list[i].cnt;
					b -= balloon_list[i].cnt;
				}
			}
		}

		cout << ans << '\n';
	}
}


int main() {

	simulation();
}
