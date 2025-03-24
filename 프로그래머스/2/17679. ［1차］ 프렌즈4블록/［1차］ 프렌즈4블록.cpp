/*
10:45
같은 모양의 프렌즈 블록이 2 x 2 형태로 4개 붙어있을 경우 사라지면서 점수를 얻는 게임임
- 같은 블록은 여러 2 x 2에 포함될 수 있다. 
- 지워지는 조건에 만족하는  2 x 2 모양이 여러 개 있다면 한꺼번에 지워진다.

블록이 지워진 후에는 위에 있는 블록이 아래로 떨어진다.
첫 블록의 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하기

풀이 : 구현, 시뮬
n, m <= 30
1. 붙은 블록 체크
 - 필요 조건 : 시작 위치 배열
2. 블록 삭제하기
3. 중력 작용
*/

#include <string>
#include <vector>
#include <queue>
#include <cstring>
#include <iostream>

using namespace std;

int N, M;
queue<pair<int, int>> erase_loc;
int visited[31][31];

void find_block(vector<string> &board){
    // 30 x 30 x 2 x 2
    for (int i=0;i<N - 1;i++){
        for (int j=0;j<M - 1;j++){
            int flag = 1;
            char character = board[i][j];
            
            if (character == '.')
                continue;
            
            for (int r = i;r<i + 2;r++){
                for (int c = j;c<j + 2;c++){
                    if (character != board[r][c]){
                        flag = 0;
                        break;
                    }
                }
                if (!flag)
                    break;
            }
            // 맞으면 시작 위치 큐에 저장
            if (flag)
                erase_loc.push({i, j});
        }
    }
}


int erase_block(vector<string> &board){
    memset(visited, 0, sizeof(visited));
    int tmp = 0;
    
    while (!erase_loc.empty()){
        int i = erase_loc.front().first, j = erase_loc.front().second;
        erase_loc.pop();
        
        for (int r = i;r<i + 2;r++){
            for (int c = j;c<j + 2;c++){
                board[r][c] = '.';
                visited[r][c] = 1;
            }
        }
    }
    
    // 지운 블록 더해주기
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            if (visited[i][j])
                tmp++;
        }
    }
    
    return tmp;
}


void gravity(vector<string> &board){
    for (int j=0;j<M;j++){
        for (int i=N - 1;i>= 0;i--){
            // 빈공간이라면, 위에서 블럭 하나 찾아서 위치바꾸기
            if (board[i][j] == '.'){
                int nr = i - 1;
                while (nr >= 0){
                    if (board[nr][j] != '.'){
                        swap(board[nr][j], board[i][j]);
                        break;
                    }
                    nr--;
                }
            }
        }
    }
}


int solution(int m, int n, vector<string> board) {
    int answer = 0;
    N = m, M = n;
    
    while (1){
        // 1. 블록 찾기
        find_block(board);

        // 2. 블록 삭제하기
        int block_cnt = 0;
        block_cnt = erase_block(board);
        if (!block_cnt)
            break;
        
        answer += block_cnt;

        // 3. 중력 작용
        gravity(board);
    }
    
    
    return answer;
}