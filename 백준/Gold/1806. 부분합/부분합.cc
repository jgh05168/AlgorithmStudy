/*
길이 n짜리 수열이 주어진다. 
연속된 수들의 부분합 중, 그 합이 s 이상이 되는 것 중 가장 짧은 것의 길이 구하기

N <= 100000
풀이 : 
수열 정렬은 불가능하다.
1. 투포인터로 처음 위치부터 시작하기 
-> s가 넘어가면 left 줄이기 안넘어가면 right 올리기
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, s;

int main() {
	cin >> n >> s;
	vector<int> arr(n + 1);
	for (int i = 0; i < n; i++)
		cin >> arr[i + 1];
	int left = 0, right = 0;
	int ans = 100000 + 2;
	int total = 0;
	while (left <= right) {
		if (total < s) {
			if (right < n + 1)
				total += arr[right++];
			else
				break;
		}
		else {
			ans = min(ans, right - left);
			total -= arr[left++];
		}
	}

	if (ans == 100002)
		ans = 0;
	cout << ans << '\n';


	return 0;
}