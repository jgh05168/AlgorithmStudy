/*
캐릭터는 다각형의 둘레를 따라 이동함
중앙에 빈 공간이 생기는 경우, 다각형의 바깥쪽 테두리가 이동경로가 된다.
아이템을 줍기 위해 이동해야 하는 가장 짧은 거리 return = bfs

풀이 : bfs
50 x 50
1. 입력 직사각형 좌표 찍기
2. bfs 진행하면서 만약 다른 직사각형 만나면 그쪽으로 이동하기
- 중복되는 경우는 어떻게 판단 ? grid를 2개 만들면 되지 = 현재 직사각형 번호보다 값이 크면 중복되는 영역인것임 = 이동불가
- 교차로에서는 교차로와 같은 곳으로는 이동 불가능함 ㅇㅇ
*/

#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cstring>

using namespace std;

int grid[101][101] = {0, };
int square_area[101][101] = {0, };
int visited[101][101] = {0, };
int n = 101;

int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

bool isValid(int r, int c){
    return 0 <= r && r < n && 0 <= c && c < n;
}


int bfs(int sr, int sc, int er, int ec){
    cout << sr << ' '<< sc << ' ' << er << ' ' << ec << '\n';
    queue<pair<int, int>> q;
    q.push({sr, sc});
    memset(visited, -1, sizeof(visited));
    visited[sr][sc] = 0;
    
    while (!q.empty()){
        int r = q.front().first, c = q.front().second;
        q.pop();
        
        for (int d = 0;d < 4;d++){
            int nr = r + dr[d], nc = c + dc[d];
            // cout << nr << ' ' << nc << '\n';
            if (isValid(nr, nc) && visited[nr][nc] == -1 && grid[nr][nc]){
                // 교차로였고, 현재 위치가 교차로랑 값이 같다면 pass
                if (grid[r][c] == 2 && square_area[nr][nc] == square_area[r][c])
                    continue;
                if (nr == er && nc == ec)
                    return (visited[r][c] + 1) / 2;
                q.push({nr, nc});
                visited[nr][nc] = visited[r][c] + 1;
                // cout << nr << ' ' << nc << '\n';
            }
        }
    }
    return -1;
}


void init(vector<vector<int>> &rectangle) {
    for (int i=0;i<rectangle.size();i++){
        int sc = rectangle[i][0] * 2, er = n - rectangle[i][1] * 2 - 1, ec = rectangle[i][2] * 2, sr = n - rectangle[i][3] * 2 - 1;
        // 다각형 공간 채우기
        for (int r=sr;r < er + 1;r++){
            for (int c = sc;c < ec + 1;c++){
                square_area[r][c] += i + 1;
            }
        }
        // 꼭짓점 체크하기(교차로는 1 이상의 값을 갖는다.)
        for (int r = sr;r < er + 1;r++){
            grid[r][sc] += 1;
            grid[r][ec] += 1;
        }
        for (int c = sc;c < ec + 1;c++){
            grid[sr][c] += 1;
            grid[er][c] += 1;
        }
        // 중복 꼭짓점 1씩 빼주기
        grid[sr][sc]--; grid[sr][ec]--; grid[er][sc]--; grid[er][ec]--;
        
    }
    
//     for (int r=0;r < n;r++){
//         for (int c = 0;c < 50;c++){
//             cout << grid[r][c] << ' ';
//         }
//         cout << '\n';
//     }
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    
    init(rectangle);
    
    answer = bfs(n - characterY * 2 - 1, characterX * 2, n - itemY * 2 - 1, itemX * 2);
    
    return answer;
}