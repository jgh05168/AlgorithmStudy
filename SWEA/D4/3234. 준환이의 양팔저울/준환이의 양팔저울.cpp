/*
무게추를 올리는 순서 : N!
오른쪽 위에 올라가 있는 무게의 총합이 왼쪽 무게의 총합보다 더 커지면 안된다.

풀이 : 조합, 백트래킹
일단 왼쪽부터 무조건 넣기
-> 이렇게 완전탐색접근 실시하면 시간초과남
-> 최악의 경우 : 1.8억번 계산된다.

특정 case가 존재한다 : 
ex) if 저울추가 6, 3, 2, 1 이 존재한다면,
왼쪽에 6이 올라가 있는 경우라면 나머지 경우의 수를 보지 않더라도 모두 성립된다.
== 3! * 2^3 이 성립하는 것
따라서 추가 탐색을 하지 않고 바로 더해준다.

이런 경우는 left 의 무게가 남은 무게추의 합보다 크거나 같은 경우에 성립한다.

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int t, n, total, ans = 0;
vector<int> arr;
int visited[11];
int factorial[11];
int Exp[11];

void recur(int depth, int left, int right) {
	if (depth == n && left >= right) {
		ans++;
		return;
	}
	// 왼쪽의 무게추 합이 남은 추들을 모두 더한 값보다 크다면 : 즉시계산
	if (left >= total - left) {
		ans += Exp[n - depth] * factorial[n - depth];
		return;
	}
	
	// else
	int tmp = 0;
	// 가지치기 할 수 있는 방법 : 탐색이 필요한 애들에 대해서만 탐색하기
	// n번 돌 필요까지 없다.
	for (int i = 0; i < n; i++) {
		// 왼쪽 먼저 더하기
		if (!visited[i]) {
			visited[i] = 1;
			recur(depth + 1, left + arr[i], right);
			if (left >= right + arr[i])
				recur(depth + 1, left, right + arr[i]);
			visited[i] = 0;
		}
	}

}


int main() {
	cin >> t;
	int fact = 1;
	factorial[1] = 1; Exp[1] = 2;
	for (int i = 2; i < 11; i++) {
		factorial[i] = factorial[i - 1] * i;
		Exp[i] = pow(2, i);
	}
	for (int tc = 1; tc < t + 1; tc++) {
		arr.clear();
		ans = 0; total = 0;
		memset(visited, 0, sizeof(visited));
		cin >> n;
		for (int i = 0; i < n; i++) {
			int tmp; cin >> tmp;
			arr.push_back(tmp);
			total += tmp;
		}
		sort(arr.begin(), arr.end(), greater<>());
		recur(0, 0, 0);	// depth, left, left_cnt, right, right_cnt

		cout << '#' << tc << ' ' << ans << '\n';
	}

	return 0;
}
