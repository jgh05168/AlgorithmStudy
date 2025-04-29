/*
앱의 비활성화 문제를 해결하자
N개의 앱이 활성화되어있다고 가정하고 앱 A는 각각 M바이트의 메모리를 사용한다.
- 새로운 앱 B를 실행하고자 하여 추가로 M바이트 메모리가 필요ㅗ하기 떄문에 몇 개를 비활성화 해야 한다.
비용 c의 합을 최소화하여 필요한 메모리 M바이트를 확보하는 방법을 찾자

풀이 : 바텀업 DP
DP 배열 만들 때, 천만을 넘어가면 안된다.
1부터 순차적으로 dp하는건 불가능하다. 그럼 어떤 방식으로 해야하는가 ???
	-> 앱과 cost를 기준으로 배열에 memory 값을 저장하자. 
    -> 베낭 알고리즘
*/

#include <iostream>
#include <algorithm>

using namespace std;

int memory_table[101];
int cost_table[101];
int dp[101][10001];

int N, M, sum_cost = 0;

void init() {
    // N : 앱의 개수, M : 필요한 메모리 입력
	cin >> N >> M;
    // 현재 활성화 되어 있는 앱이 사용 중인 메모리량 입력
	for (int i = 1; i <= N; i++)
		cin >> memory_table[i];

	// 각 앱을 비활성화 했을 경우의 비용 입력
	for (int i = 1; i <= N; i++) {
		cin >> cost_table[i];
		sum_cost += cost_table[i];	// 모든 cost의 합을 계산 = 마지막 인덱스
	}
}

void solution() {
    /* 배낭 문제(DP 활용)
	* dp[i][j] = i번째 앱까지 탐색했을 때, j 비용을 소모해서 얻을 수 있는 최대 메모리
	* case 1) 현재 j 비용보다 i번째 앱의 cost가 작을 경우
	*  - (i - 1)번째 앱에서 j 비용일 때 최대 메모리 값 기록
	* case 2) 현재 j 비용보다 i번째 앱의 cost가 크거나 같은 경우
	*  - max((i - 1)번째 앱에서 j 비용일 때 최대 메모리 값, (i - 1)번째 앱에서 (j - i번째 앱의 cost)의 최대 메모리 값 + i번째 앱의 메모리량)
	*/ 
	for (int i = 1; i <= N; i++) {
		for (int j = 0; j <= sum_cost; j++) {
			if (j - cost_table[i] >= 0)	// case 2
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost_table[i]] + memory_table[i]);
			else  // case 1
				dp[i][j] = dp[i - 1][j];
		}
	}

	// N번째 앱에서 메모리량이 M 이상 확보가 가능한 순간의 비용을 출력
	for (int i = 0; i <= sum_cost; i++) {
		if (dp[N][i] >= M) {
			cout << i << endl;
			break;
		}
	}
}

int main()
{
    init();
    
    solution();

	return 0;
}