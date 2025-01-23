/*
풀이 : 수학적 계산해야함
n번 노드가 가리키는 값부터 나머지는 순환사이클 돈다.
*/

#include <iostream>
#define INIT cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);


using namespace std;

int n, m, v;
int k;
int snale[200001] = { 0, };


int main() {
	INIT;
	cin >> n >> m >> v;
	for (int i = 1; i < n + 1; i++)
		cin >> snale[i];
	int div_v = n - v + 1;

	while (m--) {
		cin >> k;
		if (k < n)
			cout << snale[k + 1] << '\n';
		else {
			cout << snale[((k - v + 1) % div_v) + v] << '\n';
		}
	}


	return 0;
}
