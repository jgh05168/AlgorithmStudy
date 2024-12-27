/*
n개의 문제를 풀었을 떄, 컵라면을 제공
문제에 대해 데드라인이 주어짐

문제를 푸는 데는 단위시간 1이 걸린다.

풀이 :
컵라면이 큰 값을 가져가되, 현재 데드라인에 임박한 녀석이 있다면, 먼저 가져가기
-> 이걸 어떻게 알 것인가 ? 
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int main() {
	int n;
	cin >> n;

	vector<pair<int, int>> problems(n); // {데드라인, 컵라면 수}
	for (int i = 0; i < n; i++) {
		cin >> problems[i].first >> problems[i].second;
	}

	// 1. 데드라인 기준으로 오름차순 정렬
	sort(problems.begin(), problems.end());

	// 2. 최소 힙(Min-Heap) 사용
	priority_queue<int, vector<int>, greater<int>> pq; // 컵라면 수를 기준으로 최소값 관리

	for (auto& problem : problems) {
		int deadline = problem.first;
		int noodle = problem.second;

		// 힙에 추가
		pq.push(noodle);

		// 힙 크기가 현재 데드라인 초과하면, 최소값 제거
		if (pq.size() > deadline) {
			pq.pop();
		}
	}

	// 3. 힙에 남아 있는 모든 값 더하기
	int cup_noodles = 0;
	while (!pq.empty()) {
		cup_noodles += pq.top();
		pq.pop();
	}

	cout << cup_noodles << '\n';
	return 0;
}