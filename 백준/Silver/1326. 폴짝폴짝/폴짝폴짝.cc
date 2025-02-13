/*
징검다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳으로만 갈 수 있음

a에서 최소 몇 번 점프를하여 b까지 갈 수 있는지 구하기

풀이 :  bfs
최소 이동이기 때문에 도착하면 return

O(10000 + 10000)
*/

#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int n, a, b;
int bridge[10001] = { 0, };
int visited[10001] = { 0, };


int bfs(int su) {
	queue<int> q;
	q.push(su);
	memset(visited, -1, sizeof(visited));
	visited[su] = 0;

	while (!q.empty()) {
		int u = q.front();
		q.pop();

		int power = bridge[u];
		for (int i = 1; u + power * i <= n; i++) {
			int v = u + power * i;
			if (visited[v] == -1) {
				if (v == b)
					return visited[u] + 1;
				visited[v] = visited[u] + 1;
				q.push(v);
			}
		}

		for (int i = 1; u - power * i >= 1; i++) {
			int v = u - power * i;
			if (visited[v] == -1) {
				if (v == b)
					return visited[u] + 1;
				visited[v] = visited[u] + 1;
				q.push(v);
			}
		}
	}

	return -1;
}


int main() {
	cin >> n;
	for (int i = 1; i < n + 1; i++)
		cin >> bridge[i];
	cin >> a >> b;

	if (a == b)
		cout << 0 << '\n';
	else
		cout << bfs(a) << '\n';

	return 0;
}