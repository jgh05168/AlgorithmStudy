#include <iostream>
#include <cmath>
#define ll long long

using namespace std;

ll A, B, C;

long long solve(ll a, ll b, ll c) {
	if (b == 0) return 1;

	ll temp;
	temp = solve(a, b / 2, c);
	temp = temp * temp % c;
	if (b % 2 == 0)
		return temp;
	else
		return temp * a % c;

}


int main() {
	cin >> A >> B >> C;
	cout << solve(A, B, C) << '\n';
}