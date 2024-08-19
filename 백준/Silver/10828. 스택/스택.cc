/*
stack

그냥 스택 구현하기
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> arr;

	for (int i = 0; i < n; i++) {
		string order;
		int tmp;
		cin >> order;

		if (order == "push") {
			cin >> tmp;
			arr.push_back(tmp);
		}
		else if (order == "top") {
			if (arr.size() == 0) {
				cout << -1 << "\n";
			}
			else {
				cout << arr[arr.size() - 1] << "\n";
			}
		}
		else if (order == "size") {
			cout << arr.size() << "\n";
		}
		else if (order == "empty") {
			if (arr.empty()) {
				cout << 1 << "\n";
			}
			else {
				cout << 0 << "\n";
			}
		}
		else if (order == "pop") {
			if (arr.size() == 0) {
				cout << -1 << "\n";
			}
			else {
				cout << arr[arr.size() - 1] << "\n";
				arr.pop_back();
			}
		}
	}
	

	return 0;
}