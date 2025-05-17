/*
마을은 n x n 행렬
P : 우체국
K : 집
. : 목초지
마을의 모든 집에 우편을 배달해야 한다.
시작은 우체국에서 시작함
상하좌우대각선으로 이동 가능
마지막 편지 배달 후에는 다시 우체국으로 돌아와야함

피로도 : 가장 높은 곳과 낮은 곳의 고도 차이
가장 작은 피로도로 모든 집에 배달하려면 어떻게 해야하는지 구하기

풀이 : 일단 bfs를 해보자. 
생각해야 할 점 - 배달 후 다시 우체국으로 돌아와야함
	-> 우체국에서 배달할 곳을 찾으면, 최대 / 최소 업데이트 해야함
	-> 근데 이것도 배달이 갈 수 있는 경우에 한해서 업데이트 해야돼
-> queue에 node를 저장하는 방식
node : 현재 이동하면서 저장한 최대, 최소값 & 좌표(r, c)
도착했을 때는, 도착지 집까지 걸린 최대 / 최소값을 업데이트해야댐

이렇게 푸는 경우, 모든 경우의수를 다 생각하는 것이다.

마지막에 모든 위치의 최대 / 최소를 계산하여 출력

visited에는 현재 피로도를 저장. 지금까지 오는데 필요한 피로도가 visited보다 큰 경우에는 이동 불가능하게 세팅

---------------------------------------------------
우체국으로 되돌아오는 경우까지 생각해서 풀이해야함 == 결국 높이의 범위를 구해서 줄여나가는 식
 
 => 투포인터 + bfs

*/

#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 52
#define ll long long
#define INF 0x3f3f3f3f
using namespace std;
int N;
vector <int> v;
char maps[MAX][MAX];
int dist[MAX][MAX];
bool visited[MAX][MAX]; // 방문 배열
int dx[8] = { -1,-1,0,1,1,1,0,-1 };
int dy[8] = { 0,1,1,1,0,-1,-1,-1 };
int house;
int starty, startx;
int ans = INF;


void init() {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> maps[i][j];
			if (maps[i][j] == 'K') house++;
			if (maps[i][j] == 'P') {
				starty = i;
				startx = j;
			}
		}
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> dist[i][j];
			v.push_back(dist[i][j]);
		}
	}
}

int cnt;


void dfs(int r, int c, int mx, int mn) {
	visited[r][c] = 1;
	if (maps[r][c] == 'K') {
		cnt++;
	}
	for (int i = 0; i < 8; i++) {
		int nr = r + dy[i];
		int nc = c + dx[i];
		if (nr <= 0 || nc <= 0 || nr > N || nc > N || visited[nr][nc]) continue;
		if (dist[nr][nc] > mx || dist[nr][nc] < mn) continue;
		dfs(nr, nc, mx, mn);
	}
}

void simulation() {
	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.end());
	//고도 범위 
	auto mxit = v.begin();
	auto mnit = v.begin();
	while (true) {
		int mxv = *mxit;
		int mnv = *mnit;

		if (mxv < dist[starty][startx]) {
			mxit++;
			continue; // 최대 값을 시작 점까지 이동 
		}
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				visited[i][j] = 0; // 방문 배열 초기화
			}
		}
		cnt = 0;
		dfs(starty, startx, mxv, mnv);
		//cout << "cnt:" << cnt << "\n";
		if (cnt != house) {
			mxit++;
			if (mxit == v.end()) break;
		}
		else {
			int tmp = *mxit - *mnit;
			ans = min(ans, tmp);
			mnit++; // 최소 값을 높여본다.
			//std::cout << "mxit : " << *mxit << "mnit" << *mnit << "\n";
			//cout << "ans : " << ans << "\n";
			if (*mnit > dist[starty][startx]) break;
			if (mnit == v.end()) break;
		}

	}
	std::cout << ans << "\n";
}
int main() {
	init();
	simulation();

	return 0;
}