/*
각 보석은 무게 m과 가격 v를 갖고 있다.
상근이는 가방을 k개 갖고있다.
각 가방에 담을 수 있는 최대 무게는 c이다.
가방에는 최대 한 개의 보석만 넣을 수 있다.
훔칠 수 있는 보석의 최대 가격은 ?

풀이 : 
2중 for문을 돌아야 하기 때문에 시간초과 -> 냅색 불가능
그렇다면 ,, n개 줄 안에 무조건 끝내야한다.

heapq로 가방을 관리하자 ?
heapq로는 무조건 가방을 넣을 수 있도록 해야하기 때문에, 들어갈 자리가 있는지 확인하기

*/

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define lli long long int

using namespace std;

lli n, k;
lli c;

int main() {
	INIT;
	cin >> n >> k;
	vector<pair<lli, lli>> jewelry(n);
	vector<lli> bagpack(k);
	for (int i = 0; i < n; i++)
		cin >> jewelry[i].first >> jewelry[i].second;
	for (int i = 0; i < k; i++)
		cin >> bagpack[i];
	priority_queue<lli, vector<lli>> pq;

	sort(bagpack.begin(), bagpack.end());
	sort(jewelry.begin(), jewelry.end());

	lli ans = 0, idx = 0;
	// 용량이 작은 가방부터 우선적으로 채운다.
	// 가방에 담을 수 있는 보석들 중 가격이 가장 높은 것을 담는다.

	// 우선순위 큐는 현재 가방에 넣을 수 있는 보석들 정보만 저장한다. -> 값이 큰 순서대로 pop

	/*
	1. 가방의 개수로 순회
	2. 현재 가방에 들어갈 수 있는 보석들만큼 우선순위큐에 저장
	3. 우선순위큐 top pop
	*/
	
	// 1. 
	for (int i = 0; i < k; i++) {
		// 2. 
		while (idx < n) {
			if (bagpack[i] >= jewelry[idx].first)
				pq.push(jewelry[idx++].second);
			else
				break;
		}
		// 3. 
		if (!pq.empty()) {
			ans += pq.top();
			pq.pop();
		}
	}

	cout << ans << '\n';

	return 0;
}