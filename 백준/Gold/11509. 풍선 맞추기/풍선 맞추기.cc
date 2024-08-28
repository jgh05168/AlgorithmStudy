/*
n개의 풍선, 왼쪽부터 오른쪽까지 일렬로 있다.
화살을 왼쪽에서 오른쪽으로 쏜다. 높이는 임의
- 선택된 높이 h에서 풍선을 마주칠 때까지 왼 -> 오로 이동한다.
- 화살은 계속 가던 길을 가지만, 높이 1 줄어든다.
	- h 높이에서 이동중이였다면, 풍선을 터뜨린 뒤에는  h - 1이 된다.

모든 풍선을 터트리되, 가능한한 적은 화살을 사용하는 것이다.

풀이:
정렬하면 안된다.
O(nlogn) 혹은 O(n)으로 풀어야함

h 배열을 따로 만들어서, h + 1 값이 있는지 확인
만약 없다면 ans++, 있다면 현재 위치로(h - 1)로 업데이트
O(n)
*/

#include <iostream>

using namespace std;

int n;
int h[1000002] = { 0, };    // 아래에서 배열의 인덱싱 검사를 h+1로 하고 있다. 
			    // 이 뜻은, h[1000001]이 있는 지를 확인한다는 것이다. 
			    // 따라서 초기화 시 h[1000001] 대신 h[1000002]로 진행해야 한다.

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> n;
	int balloon;
	int ans = 0;

	for (int i = 0; i < n; i++) {
		cin >> balloon;
		// 현재 h를 보고, h + 1이 있는지 체크하기
		// 있다면 h로 내리기
		// 없다면 ans++하고, h에 값 업데이트
		if (h[balloon + 1]) {
			h[balloon + 1]--;
			h[balloon]++;
		}
		else {
			ans++;
			h[balloon]++;
		}
	}

	cout << ans << '\n';

	return 0;
}
