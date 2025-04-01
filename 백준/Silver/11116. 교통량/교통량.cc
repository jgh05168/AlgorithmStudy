/*
범위가 작기 때문에 완탐 ㄱㄴ
*/

#include <iostream>

using namespace std;

int n;
int r[201];
int l[201];

int main() {
	cin >> n;

	for (int j = 0; j < n; ++j) {
		int left_car = 0;
		int m; 
		cin >> m;

		for (int i = 0; i < m; ++i) 
			cin >> l[i];
		
		for (int i = 0; i < m; ++i) 
			cin >> r[i];
		

		for (int i = 0; i < m-1; ++i) {
			for (int j = i+1; j < m; ++j) {
				if (l[i] + 500 == l[j]) {
					for (int k = 0; k < m; ++k) {
						if (l[j] + 500 == r[k]) {
							left_car += 1;
							break;
						}
					}
				}
			}
		}
		cout << left_car << '\n';
	}
	
	return 0;
}