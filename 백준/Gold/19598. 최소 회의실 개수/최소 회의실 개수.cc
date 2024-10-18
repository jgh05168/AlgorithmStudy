/*
n개 회의를 모두 진행할 수 있는 최소 회의실 개수를 구하기
시작, 끝나는 시간이 주어짐
한 회의실에는 하나의 회의만 진행된다.

풀이 :
1. 끝나는 시간 기준 오름차순 정렬
2. heap을 사용하여 관리하기
	- 맨 첫번째 친구와 비교하기
		- 맨 첫번째 녀석에 들어갈 수 있다면, pop한 뒤, 새로운 녀석 넣기
*/

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n;


int main() {
	cin >> n;
	vector<pair<int, int>> timetable(n);
	for (int i = 0; i < n; i++) cin >> timetable[i].first >> timetable[i].second;
	priority_queue<int> pq;

	// 끝나는시간 오름차순으로 정렬
	sort(timetable.begin(), timetable.end());

	// 첫번째 녀석은 pq에 저장
	pq.push(-timetable[0].second);

	// 시작
	for (int i = 1; i < n; i++) {
		if (-pq.top() <= timetable[i].first) {
			pq.pop();
			pq.push(-timetable[i].second);
		}
		else {
			pq.push(-timetable[i].second);
		}
	}

	cout << pq.size() << "\n";
	return 0;
}