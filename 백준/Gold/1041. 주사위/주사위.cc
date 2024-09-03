/*
1041 주사위

주사위 면의 숫자가 주어진다.
- 선택된 면들의 마주보는 면은 절대 선택될 수 없다.
- 두 면의 합이 5이면 마주보는 면이다.
수식이 주어진다.
- (4 * min_triple) + ((8 * n - 12) * min_double) + (5 * n - 6) * (n - 2) * dice[0];
*/

/*
#### 이 코드가 틀렸던 이유 ####

두 코드의 로직은 매우 유사해 보이지만, 두 번째 코드가 오답이 되는 이유는 변수 초기화의 실수 때문입니다.

변수 타입과 초기화 값 차이:

첫 번째 코드에서 one, two, three는 모두 int 타입으로 선언되었고, 초기값으로 5000이 설정되어 있습니다. 이는 주사위 면의 최대 값이 5000보다 작다는 것을 가정한 것입니다.
두 번째 코드에서는 one, two, three가 ll (long long) 타입으로 선언되어 있고, 초기값으로 INF가 사용되었습니다. INF는 ULONG_MAX로 설정되는데, 이는 매우 큰 값으로, 주사위의 면의 합이 이 값보다 작지 않을 경우 최소값이 제대로 업데이트되지 않을 수 있습니다.

INF의 값과 비교 문제:

첫 번째 코드에서는 초기값 5000과 비교하여 최소값을 갱신하는데, 이 값은 주사위 면의 숫자와 비교할 때 현실적인 범위 내에 있습니다.
반면, 두 번째 코드의 INF 값은 매우 커서, 초기 비교 시 현실적으로 최소값이 제대로 갱신되지 않을 수 있습니다. 특히, INF가 너무 커서 나중에 더 작은 값이 업데이트될 가능성이 낮아지거나 잘못된 값이 남을 수 있습니다.
*/

#include <iostream>
#include <algorithm>
#include <vector>

#define ll long long int 
using namespace std;

ll n; vector<ll> dice(6);
ll min_double = 5000;
int selected_double[6] = { 0, };
ll min_triple = 5000;
int selected_triple[6] = { 0, };
int rev[6] = { 5, 4, 3, 2, 1, 0 };

void get_double(int idx, ll val, int start) {
	if (idx == 2) min_double = min(min_double, val);
	else {
		for (int i = 0; i < 6; i++) {
			if (!idx) {
				selected_double[i] = 1;
				get_double(idx + 1, val + dice[i], i);
				selected_double[i] = 0;
			}
			else {
				if (!selected_double[i] && i != rev[start] && val < min_double) {
					selected_double[i] = 1;
					get_double(idx + 1, val + dice[i], start);
					selected_double[i] = 0;
				}
			}
		}
	}
}

void get_triple(int idx, ll val, int start, int second) {
	if (idx == 3) min_triple = min(min_triple, val);
	else {
		for (int i = 0; i < 6; i++) {
			if (!idx) {
				selected_triple[i] = 1;
				get_triple(idx + 1, val + dice[i], i, second);
				selected_triple[i] = 0;
			}
			else if (idx == 1) {
				if (!selected_triple[i] && i != rev[start] && val < min_triple) {
					selected_triple[i] = 1;
					get_triple(idx + 1, val + dice[i], start, i);
					selected_triple[i] = 0;
				}
			}
			else {
				if (!selected_triple[i] && i != rev[start] && i != rev[second] && val < min_triple) {
					selected_triple[i] = 1;
					get_triple(idx + 1, val + dice[i], start, second);
					selected_triple[i] = 0;
				}
			}
		}
	}
}

ll largest, sum; //가장 큰눈 , 눈의합
ll one = 5000;

int main() {
	cin >> n;
	for (int i = 0; i < 6; i++) {
		cin >> dice[i];
		sum += dice[i];
		one = min(one, dice[i]);
		largest = max(largest, dice[i]);
	}

	ll ans = 0;
	if (n == 1) {
		cout << sum - largest << '\n';
	}
	else {
		get_double(0, 0, -1);
		get_triple(0, 0, -1, -1);

		ans += (4 * min_triple) + ((8 * n - 12) * min_double) + (5 * n - 6) * (n - 2) * one;

		cout << ans << '\n';
	}


	return 0;
}
