/*
오름차순 정렬

#include <set>을 사용하면 중복 제거 가능
-> python의 set과 같은 역할을 한다..!
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;

	// set을 이용한 방법
	/*set<int> arr;

	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		arr.insert(tmp);
	}

	// set을 참조하는 방법
	for (set<int>::iterator i = arr.begin(); i != arr.end(); i++) {
		cout << *i << ' ';
	}*/

	// vector를 이용한 방법
	vector<int> arr(n);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	sort(arr.begin(), arr.end());
	
	arr.erase(unique(arr.begin(), arr.end()), arr.end());
	for (int i = 0; i < arr.size(); i++) {
		cout << arr[i] << ' ';
	}

	return 0;
}