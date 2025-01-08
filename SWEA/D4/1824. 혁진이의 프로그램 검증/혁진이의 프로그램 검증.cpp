/*
자신이 작성한 프로그램이 결국 멈출 수 있는지 확인하자

명령은 문자로 주어짐. 문자들은 2차원 격자 모양
- 현재 위치에 있는 문자가 나타내는 명령을 처리하ㅣ고, 이동 방향에 따라 다음 문자로 이동함
	- 가장 처음 위치는 제일 왼쪽 위, 이동방향은 오른쪽
- 이동 방향이 상하좌우
	- 이동이 격자 바깥이면, 반대방향으로 이동함
- 메모리 단 하나 존재. 0 ~ 15 사이 정수를 하나 저장할 수 있음
- 수행명령 주어짐
	- 숫자 : 메모리에 문자가 나타내는 값을 저장함. 처음에는 0이 저장되어있음

풀이 : 
bfs로 문제를 풀되, 메모리, 방향별 4차원 visited 배열을 생성해야 한다.

*/

#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

int t, n, m;
char grid[21][21];
int visited[16][4][21][21];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

struct node {
	unsigned int r, c, memory, direction;
};

void init() {
	memset(visited, 0, sizeof(visited));

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> grid[i][j];
}


bool bfs(unsigned int sr, unsigned int sc) {
	queue<node> queue;
	unsigned int smem;
	unsigned int sd = 0;
	if ('0' <= grid[sr][sc] && grid[sr][sc] <= '9')
		smem = (unsigned int)grid[sr][sc] - '0';
	else
		smem = 0;
	if (grid[sr][sc] == 'v')
		sd = 1;
	else if (grid[sr][sc] == '<')
		sd = 2;
	else if (grid[sr][sc] == '^')
		sd = 3;
	queue.push({ sr, sc, smem, sd });	// row, col, memory, direction
	visited[smem][sd][sr][sc] = 1;

	while (!queue.empty()) {
		unsigned int r = queue.front().r, c = queue.front().c, d = queue.front().direction;
		unsigned int mem = queue.front().memory;
		queue.pop();
		
		// 이동방향으로 한 칸 이동(범위 신경 안써줘도 된다.

		unsigned int nr = (n + r + dr[d]) % n, nc = (m + c + dc[d]) % m;
		char order = grid[nr][nc];
		unsigned int nd, question_mark = 0;
		unsigned int nmem;
		switch (order) {
		case '>':
			nd = 0;
			nmem = mem;
			break;
		case 'v':
			nd = 1;
			nmem = mem;
			break;
		case '<':
			nd = 2;
			nmem = mem;
			break;
		case '^':
			nd = 3;
			nmem = mem;
			break;
		case '_':
			if (!mem)
				nd = 0;
			else
				nd = 2;
			nmem = mem;
			break;
		case '|':
			if (!mem)
				nd = 1;
			else
				nd = 3;
			nmem = mem;
			break;
		case '?':
			question_mark = 1;
			for (unsigned int i = 0; i < 4; i++) {
				// 사전에 방문했으면 continue
				
				if (visited[mem][i][nr][nc])
					continue;
				queue.push({ nr, nc, mem, i });
				visited[mem][i][nr][nc] = 1;
			}
			break;
		case '.':
			nd = d;
			nmem = mem;
			break;
		case '+':
			nmem = (16 + mem + 1) % 16;
			nd = d;
			break;
		case '-':
			nmem = (16 + mem - 1) % 16;
			nd = d;
			break;
		case '@':
			return true;
			break;
		default:
			nmem = grid[nr][nc] - '0';
			nd = d;
			break;
		}
		
		if (question_mark)
			continue;
		// 사전에 방문했으면 continue
		if (visited[nmem][nd][nr][nc])
			continue;
		visited[nmem][nd][nr][nc] = 1;
		queue.push({ nr, nc, nmem, nd });
	}

	return false;
}


int main() {
	cin >> t;

	for (int tc = 1; tc < t + 1; tc++) {
		cin >> n >> m;
		init();

		// 게임 시작
		if (bfs(0, 0))
			cout << '#' << tc << ' ' << "YES" << '\n';
		else
			cout << '#' << tc << ' ' << "NO" << '\n';

	}
	return 0;
}
