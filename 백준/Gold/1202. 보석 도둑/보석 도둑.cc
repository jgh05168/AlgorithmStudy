/*

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

bool cmp(pair<lli, lli> a, pair<lli, lli> b) {
	if (a.first == b.first)
		return a.second < b.second;
	return a.first < b.first;
}

struct cmp2 {
	bool operator()(pair<lli, lli> a, pair<lli, lli> b) {
		if (a.second == b.second)
			return a.first < b.first;
		return a.second > b.second;
	}
};


int main() {
	INIT;
	cin >> n >> k;
	vector<pair<lli, lli>> jewelry(n);
	vector<lli> bagpack(k);
	for (int i = 0; i < n; i++)
		cin >> jewelry[i].first >> jewelry[i].second;
	for (int i = 0; i < k; i++)
		cin >> bagpack[i];
	priority_queue<pair<lli, lli>, vector<pair<lli, lli>>, cmp2> pq;

	sort(bagpack.begin(), bagpack.end());
	sort(jewelry.begin(), jewelry.end(), cmp);

	lli ans = 0;
	// 일단 다 넣고 시작하기
	// 만약 넣을 자리 없다면, (무게 낮은 순, 가방 큰 순)으로 정렬해서 채워넣기
	for (int i = n - 1; i > -1; i--) {
		if (!bagpack.empty() && bagpack.back() >= jewelry[i].first) {
			ans += jewelry[i].second;
			pq.push({ bagpack.back(), jewelry[i].second });
			bagpack.pop_back();
		}
		// 다 차 있는 경우, pq에서 찾아내기
		else {
			if (!pq.empty() && pq.top().first > jewelry[i].first) {
				if (pq.top().second < jewelry[i].second) {
					int bag = pq.top().first;
					ans += jewelry[i].second - pq.top().second;
					pq.pop();
					pq.push({ bag, jewelry[i].second });
				}
			}
		}
	}

	cout << ans << '\n';

	return 0;
}