/*
2785. 체인

- 정렬
- 정렬 후 낮은 값부터 1씩 뺀 뒤, 뒤에 긴 애들 묶어주기
- 만약 묶은 개수가 1이라면 종료
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;

int main() {
	cin >> n;
	vector<int> arr(n);
	for (int i = 0; i < n; i++) cin >> arr[i];

	sort(arr.begin(), arr.end());

	int idx = 0;
	int ans = 0;
	while (arr.size() - idx >= 2) {
		arr[idx]--;
		if (!arr[idx]) idx++;
		int a = arr.back();
		arr.pop_back();
		int b = arr.back();
		arr.pop_back();

		arr.push_back(a + b);
		ans++;
	}

	cout << ans << '\n';

	return 0;
}