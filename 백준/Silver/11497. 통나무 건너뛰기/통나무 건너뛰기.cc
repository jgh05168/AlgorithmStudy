/*
// 통나무 건너뛰기

풀이:
1. 정렬
2. 큰 수 맨 가운데 두기
3. 이후 나오는 수들 처음과 나중에 비교하여 옆에 붙여주기

--- 수정된 아이디어 ---
짝수, 홀수를 각각 번갈아가며 붙여주기
새로 배열을 만들 필요(deque)가 없다. 
-> 단순히 인접한 값을 빼주어 max를 찾자
ex) i, i + 2의 차 = 새로운 배열을 만든 후 인접한 원소의 차
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int t, n;

int main() {
	cin >> t;
	while (t--) {
		cin >> n;
		vector<int> arr(n);

		for (int i = 0; i < n; i++) cin >> arr[i];
		sort(arr.begin(), arr.end());

		int ans = 0;
		// 초기 붙어있는 값들에 대해 계산해준다
		// 우리는 i, i + 2의 차 에 대해서 생각할 것이기 때문
		ans = max(ans, abs(arr[1] - arr[0]));
		ans = max(ans, abs(arr[n - 1] - arr[n - 2]));

		for (int i = 0; i < n - 2; i++) {
			ans = max(ans, abs(arr[i] - arr[i + 2]));
		}

		cout << ans << '\n';
	}
}