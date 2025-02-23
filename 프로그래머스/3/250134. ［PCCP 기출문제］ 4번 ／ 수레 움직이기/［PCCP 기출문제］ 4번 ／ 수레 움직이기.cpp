/*
n x m 크기 격자 모양 퍼즐판
각 턴마다 모든 수레를 상하좌우 인접한 칸 중 한 칸으로 움직여야 함
- 자신이 방문했던 칸으로 움직일 수 없음
- 자신의 도착 칸에 위치한 수레는 자리에 고정된다.
- 한 칸에는 한 수레만 이동할 수 있다.
- 수레끼리 교차할 수 없다.

n <= 4

풀이 : 이동할때마다 동시에 같이 움직여야 함
-> 2가지 경우로 나누어서 생각한다. 
    : 이동 횟수마다 파란색이 먼저 움직인다 vs 빨간색이 먼저 움직인다.
visited[2][n][n]
백트래킹 진행

*/

#include <string>
#include <vector>
#include <iostream>

using namespace std;

// 다음 이동 방향
int dir[4][2] = {
    {1, 0}, {-1, 0}, {0, 1}, {0, -1}
};

// 두 수레의 방문 배열
vector<vector<pair<bool, bool>>> visited;
int answer = 100000000;
bool check(vector<vector<int>>& board, int y, int x)
{  // 범위를 벗어나거나 벽이라면 false return
    return y >= 0 && y < board.size() && x >= 0 && x < board[0].size() && board[y][x] != 5;
}

void DFS(vector<vector<int>>& maze, int ry, int rx, int by, int bx, int cnt)
{
	// 두 수레 모두 도착했다면 종료
    if (maze[ry][rx] == 3 && maze[by][bx] == 4)
    {
        answer = min(answer, cnt);
        return;
    }

    for (int i = 0; i < 4; i++)
    {
        int nry = ry;
        int nrx = rx;
        
        // 수레가 도착하지 않았을 때에만 이동
        if (maze[nry][nrx] != 3)
        {
            nry += dir[i][0];
            nrx += dir[i][1];
            
            // 이동 가능한 곳인지 체크, 방문한 노드인지 체크
            if (!check(maze, nry, nrx) || visited[nry][nrx].first)
                continue;
            
            visited[nry][nrx].first = true;
        }
        
        for (int j = 0; j < 4; j++)
        {
            int nby = by;
            int nbx = bx;
            
            // 수레가 도착하지 않았다면 이동
            if (maze[nby][nbx] != 4)
            {
                nby += dir[j][0];
                nbx += dir[j][1];
                
                if (!check(maze, nby, nbx) || visited[nby][nbx].second)
                    continue;
            
            }
   
            // 같은 곳으로 가거나, 위치를 바꾸는건 안됨
            if ((nry == nby && nrx == nbx) || 
                (nry == by && nrx == bx && nby == ry && nbx == rx))
                continue;

			// 방문 체크, 다른 경로로 가기 위한 방문 체크 취소
            visited[nby][nbx].second = true;
            DFS(maze, nry, nrx, nby, nbx, cnt + 1);
            visited[nby][nbx].second = false;
            
        }
        visited[nry][nrx].first = false;   
    }
}


int solution(vector<vector<int>> maze) {
    visited.resize(maze.size(), vector<pair<bool, bool>>(maze[0].size(), make_pair(false, false)));
    
    // 두 수레의 위치 찾기
    int ry, rx, by, bx;
    for (int i = 0; i < maze.size(); i++)
    {
        for (int j = 0; j < maze[i].size(); j++)
        {
            if (maze[i][j] == 1)
            {
                ry = i;
                rx = j;
            }
            else if (maze[i][j] == 2)
            {
                by = i;
                bx = j;
            }
        }
    }
    // 방문 체크
    visited[ry][rx].first = true;
    visited[by][bx].second = true;
    
    DFS(maze, ry, rx, by, bx, 0);
    
    // 찾지 못했다면 0을 반환 그렇지 않다면 answer반환
    return answer == 100000000 ? 0 : answer;
}