#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int n, m;
map<vector<string>, bool> result_map; // 중복 조합 방지를 위한 맵

bool isMatch(const string &user, const string &banned) {
    if (user.size() != banned.size()) return false;
    for (int i = 0; i < user.size(); i++) {
        if (banned[i] == '*') continue;
        if (user[i] != banned[i]) return false;
    }
    return true;
}

void findBannedCombinations(int depth, vector<string> &user_id, vector<string> &banned_id, vector<string> &current, vector<bool> &visited) {
    if (depth == m) {
        vector<string> sorted_current = current;
        sort(sorted_current.begin(), sorted_current.end()); // 정렬하여 중복 방지
        if (!result_map[sorted_current]) {
            result_map[sorted_current] = true;
        }
        return;
    }

    for (int i = 0; i < n; i++) {
        if (!visited[i] && isMatch(user_id[i], banned_id[depth])) {
            visited[i] = true;
            current.push_back(user_id[i]);
            findBannedCombinations(depth + 1, user_id, banned_id, current, visited);
            current.pop_back();
            visited[i] = false;
        }
    }
}

int solution(vector<string> user_id, vector<string> banned_id) {
    n = user_id.size();
    m = banned_id.size();
    result_map.clear();

    vector<bool> visited(n, false);
    vector<string> current;
    
    findBannedCombinations(0, user_id, banned_id, current, visited);

    return result_map.size();
}
