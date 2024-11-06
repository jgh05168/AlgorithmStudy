/*
좋다 !

N개의 수 중에서 어떤 수가 다른 두 개의 합으로 나타낼 수 있는 수의 개수
수의 위치가 다르면 값이 같아도 다른 수이다. -> 
풀이:
모든 수를 해시맵에 저장한 뒤,
투포인터를 하용해 매칭시키기
------- 시간초과 ------- : 2중 for문 돌면 시초난다.
문제 이해를 잘못함 
- 문제의 입력이 같은 값이 들어올 수도 있고, 그 중에서도 사용되어진 녀석은 또 카운트되면 안된다.
이분탐색 활용해서 풀기
*/

#include <iostream>
#include <unordered_map>
#include <set>
#include <vector>
#include <algorithm>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, tmp;
unordered_map<int, int> table;

int main() {
	cin >> n;
	vector<int> arr(n);
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		arr[i] = tmp;
		table.insert({ tmp, 1 });
	}

	// 순차적으로 정렬
	sort(arr.begin(), arr.end());

	int ans = 0;
	// 찾고자 하는 녀석은 자기 자신과 다른 수들의 합이여야 한다.
	for (int idx = 0; idx < n; idx++) {
		int target = arr[idx];    // 찾고자 하는 녀석
		int left = 0, right = n - 1;
		// 투포인터 시작
		while (left < right) {
			int good = arr[left] + arr[right];
			if (target == good) {
				// 예외처리 ( 현재 인덱스 녀석들(left, right)이랑 idx랑 달라야한다. )
				if (left != idx && right != idx) {
					ans++;
					break;
				}
				// 현재 idx랑 left가 만나기 전이라면 left + 1
				// 이미 만났다면, rignt - 1
				if (left == idx)
					left++;
				else
					right--;
			}
			// 같은 값을 가지지 않았다면, 이분탐색 범위 조절
			else {
				// target값보다 작다면, left를 키워주어 good 값 올리기
				if (good < target)
					left++;
				else
					right--;
			}
		}
	}
	
	cout << ans << '\n';

	return 0;
}