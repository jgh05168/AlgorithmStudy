
#include <vector>

using namespace std;

int MOD = 20170805;
int M, N;
int DY[] = { 0, 1 };
int DX[] = { 1, 0 };
vector<vector<vector<int>>> cache;

int dfs(int y, int x, int dir, vector<vector<int>>& city_map)
{
  if (y + 1 == N && x + 1 == M)
  {
    return 1;
  }

  int& ret = cache[y][x][dir];
  if (ret != -1)
  {
    return ret;
  }

  ret = 0;
  for (int i = 0; i < 2; i++)
  {
    int dy = y + DY[i];
    int dx = x + DX[i];
    if (dy < 0 || dy >= N || dx < 0 || dx >= M ||
        city_map[dy][dx] == 1 ||
        (city_map[y][x] == 2 && i != dir))
    {
      continue;
    }
    ret = (ret + dfs(dy, dx, i, city_map)) % MOD;
  }
  return ret;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map)
{
  int answer = 0;

  M = n;
  N = m;
  cache.assign(N, vector<vector<int>>(M, vector<int>(2, -1)));
  answer = dfs(0, 0, 0, city_map);

  return answer;
}
