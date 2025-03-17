/*
5의 배수일 때를 카운트하기
*/

#include<iostream>

using namespace std;

int cnt = 0;
int n;

int main() {
	cin >> n;
    
	for (int i = 1; i < n + 1; i++) {
		if (i % 5 == 0) {		
			cnt++;
            if (i % 25 == 0)		
                cnt++;
            if (i % 125 == 0)		
                cnt++;
		}
	}
    
	cout << cnt << '\n';
    
    return 0;
}