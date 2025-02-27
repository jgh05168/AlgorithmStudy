/*

모든 부분수열 구한 뒤, 기록하기
이후, 탐색해보며 입력 안 된 애 출력
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int arr[21];
int dat[2000001] = { 0, };

void per(int depth, int idx, int val) {
	dat[val] = 1;
	if (depth == n)
		return;
	for (int i = idx; i < n; i++) {
		per(depth + 1, i + 1, val + arr[i]);
	}
}



int main() {
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	per(0, 0, 0);

	for (int i = 1; i < 2000001; i++) {
		if (!dat[i]) {
			cout << i << '\n';
			break;
		}
	}
	return 0;
}