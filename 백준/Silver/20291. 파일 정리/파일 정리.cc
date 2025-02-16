#include <iostream>
#include <string>
#include <map>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n;
string s;
map<string, int> ans;

int main() {
    INIT
    cin >> n;
    while (n--) {
        cin >> s;
        string ext = s.substr(s.find('.') + 1);  // 확장자 추출 최적화
        ans[ext]++;
    }

    for (const auto& key : ans)  // 불필요한 복사 방지
        cout << key.first << ' ' << key.second << '\n';

    return 0;
}
