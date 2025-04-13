/*
12:15

1 ~ n까지 번호가 붙은 방을 지나가야 하는 마법의 미로를 마주침
각 방 안에는 번호가 붙은 문이 있을 수 있음
각 문은 해당하는 번호의 방으로 통함
방 안에는 레프리콘이나 트롤이 있을 수 있음

레프리콘 : 모험가의 소지금이 일정 양 이하로 떨어지지 않게 채워준다
	- 일정량 미만일 떄는 그만큼 값을 채워줌
	- 일정량 이상일 때는 그냥 둔다.
트롤 : 일정량 통행료 지불
	- 1번 방에서 시작할 때도 마찬가지임

풀이 : bfs

갈 수 있는 방 정보를 단방향 그래프에 저장

*/

#include <iostream>
#include <cstring>
#include <queue>
#include <vector>

using namespace std;

int n;
vector<vector<int>> grid(1001);
pair<char, int> room_info[1001];
int visited[1001];


void init() {
	memset(visited, -1, sizeof(visited));

	for (int i = 1; i < n + 1; i++) {
		grid[i].clear();
		cin >> room_info[i].first >> room_info[i].second;
		int tmp;
		while (1) {
			cin >> tmp;
			if (!tmp)
				break;
			grid[i].push_back(tmp);
		}
	}
}


int simulation() {

	// bfs 시작
	queue<pair<int, int>> q;
	q.push({ 1, 0 });		// 노드, 비용
	visited[1] = 0;

	while (!q.empty()) {
		int u = q.front().first;
		int cost = q.front().second;
		q.pop();

		// 정점 도착 시 continue
		if (u == n)
			return 1;

		for (auto v : grid[u]) {
			if (room_info[v].first == 'E' && visited[v] < cost) {
				q.push({ v, cost });
				visited[v] = cost;
			}
			else if (room_info[v].first == 'L') {
				int new_cost = cost < room_info[v].second ? room_info[v].second : cost;
				if (visited[v] < new_cost) {
					q.push({ v, new_cost });
					visited[v] = new_cost;
				}
			}
			else {
				int new_cost = cost - room_info[v].second;
				if (visited[v] < new_cost) {
					q.push({ v, new_cost });
					visited[v] = new_cost;
				}
			}
		}
	}

	return 0;
}


int main() {
	while (1) {
		cin >> n;
		if (!n)
			break;

		init();

		int ans = simulation();

		if (ans)
			cout << "Yes" << '\n';
		else
			cout << "No" << '\n';
	}
}