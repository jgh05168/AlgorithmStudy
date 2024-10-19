/*
휴게소를 m개 더 세우려고 한다.
- 이미 휴게소가 있는 곳에는 세울 수 없음
- 고속도로의 끝에도 세울 수 없음
- 휴게소 M개를 모두 지어야 한다.
- 휴게소가 없는 구간의 크기를 작게 하고싶음

풀이:
매개변수탐색
1. 현재 존재하는 휴게소 오름차순 정렬
2. 각 구간에서 몇 번 나오는 지 체크한 다음, 구간의 길이 // 체크한 개수 해주기

우선순위큐, selection

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, l;
vector<int> v;

int main() {
	cin >> n >> m >> l;
	v.push_back(0); v.push_back(l);
	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		v.push_back(tmp);
	}

	sort(v.begin(), v.end());

	// 시작과 끝 범위를 1 ~ L - 1로 설정해주어야 한다. (초기 위치에는 휴게소를 지을 수 없음)
	int start = 1;
	int end = l - 1;
	int mid;
	int ans = l;

	while (start <= end) {
		mid = (start + end) / 2;
		int cnt = 0;
		// 구간을 순회하면서 몇 개나 설치할 수 있는지 체크해보기
		for (int i = 1; i < v.size(); i++) {
			int dist = v[i] - v[i - 1];
			int adj_cnt = dist / mid;
			if (adj_cnt) {
				// 딱 맞아떨어진다는 것은 마지막 휴게소와 겹쳤다는 뜻이므로 하나 빼줌
				/*
				예를 들어, (10,50) 사이에 간격이 10인 휴게소를 세운다고 하면,
				계산 상으로는 40/10 = 4이 나와야 한다.

				그런데 이미 50에는 휴게소가 지어져 있다.
				그래서 사실상 (20,30,40) 이렇게 3개가 나와야 하는 것이다.
				*/
				if (dist % mid == 0) cnt += adj_cnt - 1;
				else cnt += adj_cnt;
			}
		}

		// m개 만들 수 있는지 체크
		if (cnt > m) {
			start = mid + 1;
		}
		else {
			// 값으로 판단을 하기 때문에, end = mid - 1로 해주어야 한다. (for문 생각하고 end = mid로 하면 안된다)
			end = mid - 1;
			ans = min(ans, mid);
		}
	}

	cout << ans << '\n';

	return 0;
}