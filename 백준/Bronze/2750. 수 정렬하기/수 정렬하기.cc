#include <iostream>
#include <algorithm>

using namespace std;

int num[1000];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
		cin >> num[i];

	sort(num, num + n);	// 입력받은 수만큼만 오름차순 정렬.
	for (int i = 0; i < n; i++)
		cout << num[i] << endl;

	return 0;
}