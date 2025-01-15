/*
임의의 지렁이 두 마리 매칭, 한 지렁이에게 다른 지렁이가 있는곳으로 가도록 하기
가능한 지렁이들이 움직인 벡터 합의 크기가 작기를 바람

지렁이들은 2차원 평면 안에서 이동함. 
a -> b 라면, 그 벡터는 점 a 에서 b를 가리키는 벡터가 된다.
|V| = x * x + y * y

벡터의 합 구하기 : 

풀이 : 조합
- 지렁이는 n / 2마리만 선택해도 된다.
- 벡터의 성질 : 교환법칙, 결합법칙이 성립
- 도착 벡터 - 출발 벡터를 하면 이동거리가 구해진다.

*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#define ll unsigned long long
#define INF 800000000002
using namespace std;

int t, n;
vector<pair<int, int>> worms;
int visited[21];
ll ans;

void recur(int depth, int idx) {
	if (depth == n / 2) {
		// 벡터 크기 계산
		ll x = 0, y = 0;
		for (int i = 0; i < n; i++) {
			if (visited[i]) {
				x += worms[i].first;
				y += worms[i].second;
			}
			else {
				x -= worms[i].first;
				y -= worms[i].second;
			}
		}
		ll tmp = x * x + y * y;
		if (ans > tmp)
			ans = tmp;
	}
	for (int i = idx; i < n; i++) {
		if (!visited[i]) {
			visited[i] = 1;
			recur(depth + 1, i + 1);
			visited[i] = 0;
		}
	}
}

int main() {
	cin >> t;
	for (int tc = 1; tc < t + 1; tc++) {
		worms.clear();
		memset(visited, 0, sizeof(visited));
		ans = INF;
		cin >> n;
		for (int i = 0; i < n; i++) {
			int a, b;
			cin >> a >> b;
			worms.push_back(make_pair(a, b));
		}

		recur(0, 0);

		cout << '#' << tc << ' ' << ans << '\n';
	}

	return 0;
}