/*
장소들 중 서로 다른 두 곳을 골라서 벌을 한 마리씩 둔다. 
또 다른 장소 하나를 골라 벌통을 둔다.

두마리 벌은 벌통으로 날아가면서, 지나가는 모든 칸에서 꿀을 딴다.
1. 두 마리가 모두 지나간 장소에서는 두마리 모두 표시된 양 만큼 꿀을 딴다. 
2. 벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.

풀이:
다른 블로그를 참고해서 품
1. 벌1 --- 벌2 --- 꿀통
	: (총합 - 벌1꿀 - 벌2꿀) + (총합 - 벌2누적합)
2. 꿀통 --- 벌2 --- 벌1
	: (총합 - 벌1꿀 - 벌2꿀) + (총합 - 벌2누적합)
3. 벌1 --- 꿀통 --- 벌2
	: (벌통누적 - 벌1) + (총합 - 벌2 - (벌통누적 - 1))
*/

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int honey[100001] = { 0, };
int sum_honey[100001] = { 0, };

int main() {
	cin >> n;
	cin >> honey[0];
	sum_honey[0] = honey[0];
	for (int i = 1; i < n; i++) {
		cin >> honey[i];
		sum_honey[i] = sum_honey[i - 1] + honey[i];
	}

	int ans = 0;
	// 1번. 벌1 --- 벌2 --- 꿀통
	for (int i = 1; i < n; i++) {
		ans = max(ans, (sum_honey[n - 1] - honey[0] - honey[i]) + (sum_honey[n - 1] - sum_honey[i]));
	}

	// 2번. 꿀통 --- 벌2 --- 벌1
	for (int i = n - 2; i >= 0; i--) {
		ans = max(ans, (sum_honey[n - 1] - honey[n - 1] - honey[i]) + sum_honey[i - 1]);
	}

	// 3번. 벌1 --- 꿀통 --- 벌2
	for (int i = 1; i < n - 1; i++) {
		ans = max(ans, (sum_honey[i] - honey[0]) + (sum_honey[n - 1] - honey[n - 1] - sum_honey[i - 1]));
	}

	cout << ans << '\n';

	return 0;
}