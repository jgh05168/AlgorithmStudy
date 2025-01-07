/*
지표면에 떨어지는 별똥별의 수를 최소화하자!
네모난 L x L 크기의 트램펄린을 준비. 
별똥별이 어디로 떨어질 지는 이미 알고있다.
최대한 많은 별똥별을 튕겨내도록 트램펄린을 배치했을 때, 지구에는 몇 개의 별똥별이 부딪히게될까
- 별똥별은 트램펄린 모서리에 부딪혀도 튕겨나간다.

n, m <= 500000
풀이 : 만약, n, m이 50만이고 l이 1이라면, 2중 for문 돌 경우 시간초과난다. 50만 x 50만
단순한 브루트포스로는 풀이 불가능

군집을 찾아야한다 ?
두 개의 별똥별은 선택한 다음, 그 두 별똥별의 공통된 좌상단 좌표를 찾기
찾은다음, 별똥별 세기
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m, l, k;

int main() {
	INIT;
	cin >> n >> m >> l >> k;
	vector<pair<int, int>> stars(k);
	for (int i = 0; i < k; i++)
		cin >> stars[i].first >> stars[i].second;

	int ans = k;
	// 두 꼭짓점이 교차하는 좌상단 좌표 먼저 찾기 
	for (int i = 0; i < k; i++) {
		for (int j=0;j<k;j++){
			int r = min(stars[i].first, stars[j].first);
			int c = min(stars[i].second, stars[j].second);
			// 찾은 좌표에서 l만큼 범위 안에 속하는 별똥별 찾기
			int tmp = 0;
			for (auto star : stars) {
				if (r <= star.first && star.first <= r + l && c <= star.second && star.second <= c + l)
					tmp++;
			}
			ans = min(ans, k - tmp);
		}
	}

	cout << ans << '\n';

	return 0;
}