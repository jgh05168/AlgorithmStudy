/*
하노이탑
1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있음
2. 항상 위의 것이 아래 것보다 작아야 한다.

이동횟수 최소로 하는 path 생성

풀이 : 백트래킹

#include <cstdio>
using namespace std;
void move(int from, int to) {
	 cout << from << " -> " << to << '\n';
}

void hanoi(int n, int from, int by, int to) {
	 if(n == 0) return;
	 hanoi(n - 1, from, to, by);
	 move(from, to);
	 hanoi(n - 1, by, from, to);
}

출처 : 위키피디아 - https://ko.wikipedia.org/wiki/%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98_%ED%83%91
*/

#include <iostream>
using namespace std;

void go(int n, int start, int mid, int end) {
	if (n == 1) {
		cout << start << " " << end << "\n";
		return;
	}
	go(n - 1, start, end, mid);
	cout << start << " " << end << "\n";
	go(n - 1, mid, start, end);
}

int main() {
	int n;
	cin >> n;
	cout << (1 << n) - 1 << "\n";
	go(n, 1, 2, 3);
	return 0;
}