/*
크기가 N인 배열 A
배열의 모든 수는 서로 다르다.
연속된 두 개의 원소만 교환할 수 있다.
교환은 많아봐야 S번 할 수 있다.

가장 큰 값을 찾아서 인덱스 체크
이후 처음부터 그 인덱스까지 계속해서 끌고오기 반복
*/

#include <iostream>
#include <vector>

using namespace std;

int n, s;

int main() {
	cin >> n;
	vector<int> arr(n);
	for (int i = 0; i < n; i++) cin >> arr[i];
	cin >> s;

	for (int i = 0; i < n; i++) {
		int cnt = 0;
		// 가장 큰 인덱스 찾기
		int max_v = arr[i];
		int max_idx = i;
		// 새로운사실 ! for문 안에는 조건을 2개 이상 넣을 수 있다 !! ㄷㄷㅌ!
		for (int j = i + 1; j < n && cnt < s; j++, cnt++) {
			if (max_v < arr[j]) {
				max_v = arr[j];
				max_idx = j;
			}
		}
		/*
		// 이렇게도 가능할듯
		for (int j = i + 1; j < n; j++) {
			if (cnt < s){
				if (max_v < arr[j]) {
					max_v = arr[j];
					max_idx = j;
					cnt++;
				}
			}
		}
		*/

		// 소트해서 옮기기
		int flag = 0;
		for (int j = max_idx; j > i; j--) {
			if (arr[j] > arr[j - 1]) {
				swap(arr[j], arr[j - 1]);
				if (!--s) {
					flag = 1;
					break;
				}
			}
		}
		
		if (flag) break;
	}

	for (int i = 0; i < n; i++) cout << arr[i] << ' ';

	return 0;
}
