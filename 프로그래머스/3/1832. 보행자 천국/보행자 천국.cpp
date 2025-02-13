#include <vector>
#include <algorithm>

using namespace std;

int MOD = 20170805;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
    if ((n|m)==1) return 0;

    int routes[m][n][2];
    fill_n(&routes[0][0][0], m*n*2, 0);

    routes[0][0][0] = 1; // x
    routes[0][0][1] = 1; // y
    for (int x=0;x<m;x++) {
        for (int y=0;y<n;y++) {
            if ((x|y)==0) continue;

            int* route = &routes[x][y][0];
            int map = city_map[x][y];
            if (map == 0) {
                int cnt = 0;
                if (x > 0) cnt = (cnt + routes[x-1][y][0]) % MOD;
                if (y > 0) cnt = (cnt + routes[x][y-1][1]) % MOD;
                route[0] = route[1] = cnt;
            } else if (map == 1) {
                route[0] = route[1] = 0;
            } else if (map == 2) {
                if (x > 0) route[0] = routes[x-1][y][0];
                if (y > 0) route[1] = routes[x][y-1][1];
            }
        }
    }
    return routes[m-1][n-1][0];
}