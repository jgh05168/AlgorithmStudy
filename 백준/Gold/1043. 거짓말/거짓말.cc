/*
거짓말 하고싶은데, 몇몇은 그 이야기의 진실을 안다
-> 진실을 아는 사람이 왔을 땐, 진실을 얘기한다
-> 거짓을 들은 사람이 진실을 아는 사람을 만나면 안된다.

과장된 이야기를 할 수 있는 파티 개수의 최댓값

풀이:
n, m < 50
- 모든 파티는 연괸되어 있음
1. 모든 애들 그래프화 시키기(50C2)
2. 아닌 놈들 기준으로 bfs 돌려 거짓말인 놈 찾아내기
3. 파티 돌면서 거짓말 레이더에 안걸리면 ans++

*/

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, m, party_cnt;
queue<int> lier;
int visited[51] = { 0, };

void bfs(vector<vector<int>> graph) {
	while (!lier.empty()) {
		int u = lier.front();
		lier.pop();

		for (int v : graph[u]) {
			if (!visited[v]) {
				lier.push(v);
				visited[v] = 1;
			}
		}
	}
}

int main() {
	cin.tie(0); ios::sync_with_stdio(false);
	cin >> n >> m;
	cin >> party_cnt;
	int tmp;
	for (int i = 0; i < party_cnt; i++) {
		cin >> tmp;
		lier.push(tmp);
		visited[tmp] = 1;
	}

	vector<vector<int>> graph(n + 1);
	vector<vector<int>> parties(m);
	for (int i = 0; i < m; i++) {
		cin >> tmp;
		vector<int> members(tmp);
		int flag = 0;
		for (int j = 0; j < tmp; j++) {
			cin >> members[j];
			// 파티 목록 만들기
			parties[i].push_back(members[j]);
		}
		// 1. 그래프 만들기
		for (int j = 0; j < members.size(); j++) {
			for (int k = j + 1; k < members.size(); k++) {
				graph[members[j]].push_back(members[k]);
				graph[members[k]].push_back(members[j]);
			}
		}
	}
	
	// 2. 거짓말쟁이 모임 만들기
	bfs(graph);

	// 3. 파티 다시 순회하면서 가능한 파티 찾기
	int ans = 0;
	for (int i = 0; i < m; i++) {
		int flag = 0;
		for (int j = 0; j < parties[i].size(); j++) {
			if (visited[parties[i][j]]) {
				flag = 1;
				break;
			}
		}
		if (!flag) ans++;
	}

	cout << ans << '\n';
	return 0;
}