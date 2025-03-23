#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

vector<int> v;
map<string, bool> m;
bool visit[11];
int n, k;
string s;

void solve(int cnt){
	if (cnt >= k){
		if (m[s] == false) {
			m[s] = true;
		}
		return;
	}

	for (int i = 0; i < v.size(); i++){
		if (visit[i] == false) {
			visit[i] = true;
			string tmp = s;
			s += to_string(v[i]);
			solve(cnt + 1);
			s = tmp;
			visit[i] = false;
		}
	}
}
int main(void)
{
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		v.push_back(num);
	}
    solve(0);
    cout << m.size();
}