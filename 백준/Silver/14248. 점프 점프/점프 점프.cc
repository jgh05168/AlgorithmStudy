/*
왼 / 오 점프 가능
본인이 방문가능한 돌의 개수

풀이 : 이전 문제에서 visited 개수만 세면 된다.

------------숫자가 적힌 만큼만 점프 가능-------------

... 문제가 다름 ... 문제를 잘 읽자 ..

*/
#include <iostream>
#include <queue>
using namespace std;

int n, a;
int bridge[100001];
int visited[100001];

void bfs(int su) {
	queue<int> q;
	q.push(su);
	visited[su] = 1;

	while (!q.empty()) {
		int u = q.front();
		q.pop();

		int power = bridge[u];

		int v = u + power;
		if (v < n + 1 && !visited[v]) {
			visited[v] = 1;
			q.push(v);
		}

		v = u - power;
		if (v >= 1 && !visited[v]) {
			visited[v] = 1;
			q.push(v);
		}
	}
}

int main() {
	cin >> n;
	for (int i = 1; i < n + 1; i++)
		cin >> bridge[i];
	cin >> a;

	bfs(a);

	int ans = 0;
	for (int i = 1; i < n + 1; i++) {
		if (visited[i])
			ans++;
	}

	cout << ans << '\n';
    
	return 0;
}
