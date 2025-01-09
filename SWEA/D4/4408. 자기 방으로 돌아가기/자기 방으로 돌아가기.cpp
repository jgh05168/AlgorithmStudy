/*
조교들의 눈을 피해 자기방으로 돌아가려고 한다. 
모든 학생들은 현재 위치에서 자신의 방으로 돌아가려고 한다.
복도는 한 학생만 사용된다.

최소 몇 단위시간만에 모든 학생이 이동할 수 있는지 구하기

풀이 : 
방 번호 <= 400 
-> 복도는 하나니까 200으로 설정
방에 들어가기 위해 단위시간이 걸리니까 누적합 사용해서 다 더한 뒤 최댓값 출력하기
-> 최악의 경우, 200 * 200
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int t, n;
int floors[201] = { 0, };

int main() {
	cin >> t;
	for (int tc = 1; tc < t + 1; tc++) {
		memset(floors, 0, sizeof(floors));
		cin >> n;
		vector<pair<int, int>> arr(n);
		for (int i = 0; i < n; i++)
			cin >> arr[i].first >> arr[i].second;
		
		// 순회 시작
		for (int i = 0; i < n; i++) {
			int start, end;

			if (arr[i].first < arr[i].second) {
				// 복도 세팅
				if (arr[i].first % 2)
					start = arr[i].first / 2 + 1;
				else
					start = arr[i].first / 2;
				if (arr[i].second % 2)
					end = arr[i].second / 2 + 1;
				else
					end = arr[i].second / 2;
			}
			else {
				if (arr[i].first % 2)
					end = arr[i].first / 2 + 1;
				else
					end = arr[i].first / 2;
				if (arr[i].second % 2)
					start = arr[i].second / 2 + 1;
				else
					start = arr[i].second / 2;
			}
			for (int i = start; i <= end; i++)
				floors[i]++;
		}

		int ans = 0;
		for (int i = 0; i < 401; i++)
			ans = max(ans, floors[i]);

		cout << '#' << tc << ' ' << ans << '\n';
	}
	return 0;
}