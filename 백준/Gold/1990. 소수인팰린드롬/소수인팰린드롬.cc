/*
팰린드롬 확인해보기

1. 에라토스테네스의 체 사용해서 거르기
	-> 10000번만 돌리면 된다.
2. 팰린드롬 확인하기
*/
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;


bool check_pel(string str) {
	string x, y;
	x = str;

	reverse(str.begin(), str.end());

	y = str;

	return x == y;
}

bool check_prime(int n) {
	if (2 > n) 
		return false;

	for (int i = 2; i <= sqrt(n); i++) {
		if (n % i == 0)
			return false;
	}

	return true;
}

int main() {
	int a, b;
	cin >> a >> b;

	for (int i = a; i <= 10000000; i++) {
		if (b < i) 
			break;
		if (check_pel(to_string(i)) && check_prime(i)) {
			cout << i << '\n';
		}
	}

	cout << -1;
}