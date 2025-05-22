/*
n개의 논에 물을 대려고 함
1. 직접 논에 우물을 파는 것
2. 이미 물을 대고 있는 다른 논으로부터 물을 끌어오는 법

n <= 300
비용 <= 10만
모든 논에 물을 대는 데 필요한 최소비용을 구하는 것이 문제임

풀이 : 
dp보다는 최소비용탐색을 진행해야 할 듯
첫빠따에 물을 대는 데 최소 비용인 곳을 선택한다고 해서 최솟값 보장이 되나 ?
	-> 그래도 그리디하게 가려면 최소인 곳부터 대는 게 맞긴 함
-----------------------------------------------------------------------------
mst 알고리즘 사용해서 푸는 게 맞다.
-> 그래프가 생성이 되는 것을 확인할 수 있음
-> 가장 최소 값을 갖기 위해야함
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int w_table[301][301];
int parents[301];
vector<pair<int, pair<int, int> > > edges;


bool cmp(pair<int, pair<int, int> > a, pair<int, pair<int, int> > b) {
	return a.first < b.first;
}


void init() {
	cin >> n;

	int cost;
	// 가상의 노드 생성
	for (int i = 1; i <= n; i++) {
		cin >> cost;
		edges.push_back({ cost, {0, i} });
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> w_table[i][j];
		}
	}

	for (int i = 1; i <= n; i++) {
		for (int j = i + 1; j <= n; j++) {
			edges.push_back({ w_table[i][j], {i, j} });
		}
	}
}


int get_parent(int a) {
	if (parents[a] == a) 
		return a;
	return parents[a] = get_parent(parents[a]);
}


void union_parents(int a, int b) {
	a = get_parent(a);
	b = get_parent(b);

	if (a > b) 
		parents[a] = b;
	else 
		parents[b] = a;
}


void solution() {
	/* 크루스칼 알고리즘 */

	sort(edges.begin(), edges.end(), cmp);
	for (int i = 0; i <= n; i++) parents[i] = i;

	int answer = 0;
	for (int i = 0; i < edges.size(); i++) {
		int u = edges[i].second.first;
		int v = edges[i].second.second;
		int cost = edges[i].first;

		if (get_parent(u) != get_parent(v)) {
			union_parents(u, v);
			answer += cost;
		}
	}

	cout << answer << '\n';
}


int main(void) {
	init();

	solution();
}