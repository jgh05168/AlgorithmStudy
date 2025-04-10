/*
10:00

양 플레이어가 캐릭터를 몇 번 움직이게 될 지 예측해보기
1 x 1 크기의 격자, 발판이 있고 없는 부분이 있음
발판이 있는 곳에만 이동이 가능함
밟고있던 발판은 다른 곳으로 이동하면 사라진다.

- 움직일 차례인데, 이동을 못하는 경우, 패배
- 두 캐릭터가 같은 발판 위에 서있는데, 상대 플레이어가 이동해서 현재 발판이 사라지는 경우 패배

항상 A가 먼저 시작함
이기는 녀석 : 최대한 빨리 승리하도록 플레이함
지는 녀석 : 최대한 오래 버티도록 플레이함

풀이 : 백트래킹, minmax 알고리즘
그냥 이길 수 있는 애의 최소 이동 호ㅠㅣㅅ수를 리턴

최단거리 한 번만 이기고 나머지는 다 지는 경우 가 있음
*/

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int n, m;

int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

bool isValid(int r, int c){
    return 0 <= r && r < n && 0 <= c && c < m;
}

int recur(vector<vector<int>> &board, vector<int> cur, vector<int> next) {
    ////// MINMAX 알고리즘 사용해야함
    
    // 게임 종료 조건
    if (!board[cur[0]][cur[1]])
        return 0;
    
    int min_v = 99999999, max_v = 0;
    int isWin = 0;
    
    for (int d=0;d<4;d++){
        int nr = cur[0] + dr[d], nc = cur[1] + dc[d];
        if (isValid(nr, nc) && board[nr][nc]){
            board[cur[0]][cur[1]] = 0;
            int move_cnt = recur(board, next, vector<int>{nr, nc}) + 1;     // 1 더해줘야함 : 움직였기 때문이다.
            board[cur[0]][cur[1]] = 1;
            
            // 이기는 경우 : 최소 거리 업데이트 시켜주기
            if (move_cnt % 2) {
                isWin = 1;
                if (min_v > move_cnt)
                    min_v = move_cnt;
            }
            // 지는 경우에는 도망가야하기 때문에 max값 업데이트
            else {
                if (max_v < move_cnt)
                    max_v = move_cnt;
            }
        }
    }
    // 이겼는지 졌는지 체크해서 값 넘겨주기
    if (isWin)
        return min_v;
    else
        return max_v;
}

int solution(vector<vector<int>> board, vector<int> aloc, vector<int> bloc) {
    int answer = -1;
    n = board.size();
    m = board[0].size();
    
    answer = recur(board, aloc, bloc);
    
    return answer;
}