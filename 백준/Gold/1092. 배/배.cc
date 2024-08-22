/*
각 크레인은 무게 제한이 있다.  -> 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다.
	이런 경우 -1 출력

풀이 :
50 x 10000
- max 크레인 무게랑 비교한 뒤 만약 하나라도 무거우면 -1 출력 후 종료
1. 우선 정렬 진행(내림차순)
2. 무거운 순서로 하나씩 집어넣는다.
	크레인에 하나씩 할당하거나, 다 넣는 경우까지 반복
------ 시간초과 ------
selected 배열을 사용하는 것이 아닌, vector의 erase를 사용하자.
vector.erase() : O(n)
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m;
vector<int> cranes;
vector<int> boxes;

int main() {
	cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);
	cin >> n;
	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		cranes.push_back(tmp);
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> tmp;
		boxes.push_back(tmp);
	}

	// 크레인, 컨테이너 정렬
	sort(cranes.begin(), cranes.end(), greater<int>());
	sort(boxes.begin(), boxes.end(), greater<int>());

	int ans = 0;
	int box_idx = 0;
	int box_move = 0;

	// 더 무거운 짐이 있는지 확인
	if (cranes[0] < boxes[0]) {
		cout << -1 << '\n';
	}
	else {
		while (!boxes.empty()) {
			// 크레인 배정 시작
			for (int i = 0; i < n; i++) {
				for (int j = box_idx; j < boxes.size(); j++) {
					if (boxes[j] <= cranes[i]) {
						boxes.erase(boxes.begin() + j);
						box_move++;
						break;
					}
				}
			}
			ans++;
			if (box_move >= m) break;
		}

		cout << ans << '\n';
	}

	return 0;
}
