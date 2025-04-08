/*
9:15

격자 모양의 공간에서 모형 비행기를 조종하며 얻는 비행점수로 순위를 매긴다.
상승비행, 하강비행 : 지나간 칸에 부여된 점수의 총합
- 출발한 칸, 도착한 칸도 지나간 칸으로 간주함
	- 맨 왼쪽 아래 시작
- 상승비행 -> 하강비행 변경 시에는 다른 칸으로 이동할 수 없다.
- 상승비행 중에는 앞, 위로 이동 가능, 하강비행 중에는 앞, 아래로 이동 가능

얻을 수 있는 점수의 최댓값 구하기

풀이 : DP
갈 수 있는 경우를 구분하기
1000 x 1000이기 때문에 bottom-up이 더 나아보임

이동해본 칸에서 상승, 하강 모두 실행하기
시작 위치 : 왼쪽 아래
*/

#include <iostream>
#include <algorithm>
#define MAX_SIZE 1001
#define MIN -1e9

using namespace std;

int n, m, ans = MIN;
int grid[MAX_SIZE][MAX_SIZE];
int dp_up[MAX_SIZE][MAX_SIZE];
int dp_down[MAX_SIZE][MAX_SIZE];

void init() {
	cin >> n >> m;
	for (int i = 1; i <= n; i++){
		for (int j = 1; j <= m; j++)
			cin >> grid[i][j];
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			dp_up[i][j] = MIN;
			dp_down[i][j] = MIN;
		}
	}

	dp_up[n][1] = grid[n][1];
}

void simulation() {
	

	for (int j = 1; j <= m; j++) {
		for (int i = n; i >= 1; i--) {
			if (i < n)
                dp_up[i][j] = max(dp_up[i][j], dp_up[i + 1][j] + grid[i][j]);
			if (j > 1)
                dp_up[i][j] = max(dp_up[i][j], dp_up[i][j - 1] + grid[i][j]);
		}
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (dp_up[i][j] == MIN)
                continue;
			dp_down[i][j] = max(dp_down[i][j], dp_up[i][j] + grid[i][j]);

			if (i < n) 
                dp_down[i + 1][j] = max(dp_down[i + 1][j], dp_down[i][j] + grid[i + 1][j]);
			if (j < m) 
                dp_down[i][j + 1] = max(dp_down[i][j + 1], dp_down[i][j] + grid[i][j + 1]);
		}
	}

	ans = dp_down[n][m];
}

int main() {
	init();

	simulation();

	cout << ans << '\n';

	return 0;
}
