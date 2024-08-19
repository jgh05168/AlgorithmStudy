/*
stack

그냥 스택 구현하기
*/

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
	int n;
	cin >> n;
	stack<int> arr;

	for (int i = 0; i < n; i++) {
		string order;
		int tmp;
		cin >> order;

		if (order == "push") {
			cin >> tmp;
			arr.push(tmp);
		}
		else if (order == "top") {
			if (arr.size() == 0) {
				cout << -1 << "\n";
			}
			else {
				cout << arr.top() << "\n";
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
				cout << arr.top() << "\n";
				arr.pop();
			}
		}
	}
	

	return 0;
}