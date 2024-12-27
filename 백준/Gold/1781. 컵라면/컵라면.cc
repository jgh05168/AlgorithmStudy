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

	vector<pair<int, int>> problems(n);
	for (int i = 0; i < n; i++) {
		cin >> problems[i].first >> problems[i].second; // {데드라인, 컵라면 수}
	}

	// 1. 데드라인 기준 정렬
	sort(problems.begin(), problems.end());

	// 2. 최소 힙 사용
	priority_queue<int, vector<int>, greater<int>> min_heap;
	int total_noodles = 0;

	for (auto& problem : problems) {
		int deadline = problem.first;
		int noodles = problem.second;

		// 현재 문제를 힙에 추가
		min_heap.push(noodles);
		total_noodles += noodles;

		// 힙 크기가 데드라인을 초과하면 최소값 제거
		if (min_heap.size() > deadline) {
			total_noodles -= min_heap.top();
			min_heap.pop();
		}
	}

	// 3. 결과 출력
	cout << total_noodles << '\n';
	return 0;
}
