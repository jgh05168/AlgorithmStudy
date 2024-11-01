/*
일부 지역이 물에 잠김
물에 잠기지 않은 지역을 통해 학교를 가려고 한다.
우, 하 로만 이동 가능함
물이 잠긴 지역의 좌표는 주어진다.

*/

#include <string>
#include <vector>

using namespace std;

int dp[101][101] = {0, };
int grid[101][101] = {0, };

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    for (int i=0;i<puddles.size();i++){
        grid[puddles[i][1]][puddles[i][0]] = 1;
    }
    
    // dp 시작
    dp[0][1] = 1;
    for (int i=1;i<=n;i++){
        for (int j=1;j<=m;j++){
            if (grid[i][j]) continue;
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007;
            // printf("%d\n", dp[i][j]);
        }
    }
    
    answer = dp[n][m];
    return answer;
}