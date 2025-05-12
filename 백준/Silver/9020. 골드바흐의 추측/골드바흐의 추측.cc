/*
9020

풀이 : 에라토스테네스의 체
체를 이용하여 10000 이하의 소수 전처리
이후, for문 돌면서 두 수가 모두 소수인 경우를 출력

시간복잡도 : O(100 * 10000)
*/

#include <iostream>
#include <cstring>
#include <cmath>
#define MAX_V 10001

using namespace std;

int t, n;
int prime_dict[MAX_V];


void init() {
	fill_n(prime_dict, MAX_V, 1);
	cin >> t;
	prime_dict[0] = 0, prime_dict[1] = 0;
	for (int i = 2; i < (int)sqrt(MAX_V) + 1; i++) {
		for (int j = i + i; j < MAX_V; j += i) {
			if (j % i == 0)
				prime_dict[j] = 0;
		}
	}
}


void simulation() {
	while (t--) {
		cin >> n;
		for (int i = n / 2; i > 0; i--) {
			if (prime_dict[i] && prime_dict[n - i]) {
				cout << i << ' ' << n - i << '\n';
				break;
			}
		}
	}
}


int main() {
	init();

	simulation();
}