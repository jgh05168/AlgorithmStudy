/*
I LOVE CHICKEN !

치킨거리 : 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리 = 모든 집의 치킨 거리의 합
임의의 두 칸 사이의 거리는 |r1-r2| + |c1-c2|

일부 치킨집은 폐업시키고자 한다. 최대 M개의 치킨집만 남기고 나머지는 폐업시킨다.
도시의 치킨거리가 가장 작아지는 경우를 고르시오

풀이:
주변에 장애물은 없다. 
1. 모든 가능한 경우에 대해 dfs 진행
2. 치킨집을 M개만큼 선택했으면, 계산 진행
	- 장애물이 없기 때문에 굳이 bfs 할 필요 없음
	- 집의 개수 <= 2N이기 떄문에 최대 100 X 13
3. 이전 거리보다 커진다면 continue
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m;
int grid[51][51];
map<int, pair<int, int>> chicken_list;
vector<pair<int, int>> house;
vector<int> selected;
int ans = 50 * 50 * 13;


int distance(int r1, int r2, int c1, int c2) {
	return abs(r1 - r2) + abs(c1 - c2);
}


void dfs(int depth, int idx) {
	if (depth == m) {
		// 계산 시작
		int tmp_ans = 0;
		for (int i = 0; i < house.size(); i++) {
			int r = house[i].first;
			int c = house[i].second;
			int min_dist = 50 * 50 * 13;
			for (int j = 0; j < selected.size(); j++) {
				if (selected[j]) {
					min_dist = min(min_dist, distance(r, chicken_list[j].first, c, chicken_list[j].second));
				}
			}
			tmp_ans += min_dist;
			if (ans <= tmp_ans)
				return;
		}
		ans = tmp_ans;
		return;
	}
	else {
		for (int i = idx; i < selected.size(); i++) {
			if (!selected[i]) {
				selected[i] = 1;
				dfs(depth + 1, i + 1);
				selected[i] = 0;
			}
		}
	}
}

int main() {
	cin >> n >> m;
	int idx = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> grid[i][j];
			if (grid[i][j] == 2) {
				chicken_list.insert({ idx++, {i, j} });
				selected.push_back(0);
			}
			else if (grid[i][j] == 1)
				house.push_back({ i, j });
		}
	}

	dfs(0, 0);

	cout << ans << '\n';

	return 0;
}