/*
문은 자물쇠로 잠겨있음 & 특이한 형태의 열쇠와 함께 문 푸는 방법이 있다.

- 자물쇠는 n x n, 열쇠는 m x m 크기
- 열쇠는 회전과 이동이 가능
- 열쇠의 돌기와 자물쇠의 돌기는 만나면 안된다.
- 딱 맞아야함ㅇㅇ

자물쇠를 열 수 있는지 없는지 결과 return

풀이 : 
1. lock에 필요한 빈 칸의 크기가 얼만큼 되는지 체크해보기
2. key 칸의 좌표들을 모두 받은 뒤, 어느정도 이동했는지에 대해 상시 체크하기
    - rotate(4) x 20 x 20
    - 배열 범위 벗어나면 상관없다고 가정하기

*/

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int n, m;
int move_size = 0;
int home_cnt = 0;
vector<vector<pair<int, int>>> key_list(4);


bool isValid(int r, int c){
    return 0 <= r && r < n && 0 <=c && c < n;
}


void rotate(int idx, vector<vector<int>> &key) {
    int grid[21][21] = {0, };
    for (int i=0;i<m;i++){
        for (int j=0;j<m;j++) {
            grid[j][m - i - 1] = key[i][j];
        }
    }
    for (int i=0;i<m;i++){
        for (int j=0;j<m;j++) {
            key[i][j] = grid[i][j];
            if (key[i][j]){
                key_list[idx].push_back({i, j});
            }
        }
    }
}


void init(vector<vector<int>> &key, vector<vector<int>> &lock) {
    // lock 빈공간 사이즈 찾기
    int sr = n, sc = n, er = 0, ec = 0;
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++) {
            if (!lock[i][j])
                home_cnt++;
        }
    }
    
    // 키 홈 찾기
    for (int i=0;i<4;i++){
        rotate(i, key);
    }
}


bool simulation(vector<vector<int>> &lock) {
    // 800
    for (int i=-m + 1;i<n;i++){
        for (int j=-m + 1;j<n;j++){
            // 4
            // cout << "###" << i << ' ' <<j << '\n';
            for (int d=0;d<4;d++){
                // 400
                int tmp_cnt = 0;
                int flag = 0;
                // cout << d << '\n';
                for (auto key_loc : key_list[d]){
                    int nr = key_loc.first + i, nc = key_loc.second + j;
                    // cout << nr << ' ' << nc << '\n';
                    if (!isValid(nr, nc))
                        continue;
                    if (lock[nr][nc]){
                        flag = 1;
                        break;
                    }
                    tmp_cnt++;
                }
                // cout << '\n';
                if (!flag && home_cnt == tmp_cnt)
                    return true;
            }
        }
    }
    
    return false;
}


bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    bool answer = true;
    
    n = lock.size();
    m = key.size();
    
    // 인덱스 어느정도 이동할 것인지, key rotate 정보 전처리
    init(key, lock); 
    
    if (!home_cnt)
        return answer;
    
    answer = simulation(lock);
    
    return answer;
}