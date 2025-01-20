#include <string>
#include <vector>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int n, m;
int selected[8]; // user_id 선택 여부를 관리
int dat[8];      // 제재 아이디 조합을 저장

bool isMatch(const string& user, const string& banned) {
    if (user.size() != banned.size()) return false;
    for (int i = 0; i < user.size(); i++) {
        if (banned[i] != '*' && user[i] != banned[i]) return false;
    }
    return true;
}

int recur(int depth, vector<string>& user_id, vector<string>& banned_id, vector<vector<int>>& uniqueCombinations) {
    if (depth == m) {
        // 현재 조합 확인 및 중복 방지 처리
        vector<int> combination(dat, dat + m); // 현재 조합
        sort(combination.begin(), combination.end()); // 정렬
        
        for (int i = 0; i < uniqueCombinations.size(); i++) {
            if (uniqueCombinations[i] == combination) {
                return 0;
            }
        }

        uniqueCombinations.push_back(combination); // 새로운 조합 추가
        return 1;
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (!selected[i] && isMatch(user_id[i], banned_id[depth])) {
            selected[i] = 1;     // 선택 표시
            dat[depth] = i;      // 현재 depth에 해당하는 user_id의 인덱스를 저장
            count += recur(depth + 1, user_id, banned_id, uniqueCombinations);
            selected[i] = 0;     // 선택 해제
        }
    }
    return count;
}

int solution(vector<string> user_id, vector<string> banned_id) {
    n = user_id.size();
    m = banned_id.size();
    memset(selected, 0, sizeof(selected));
    memset(dat, 0, sizeof(dat));

    vector<vector<int>> uniqueCombinations; // 중복 방지용 컨테이너
    return recur(0, user_id, banned_id, uniqueCombinations);
}
