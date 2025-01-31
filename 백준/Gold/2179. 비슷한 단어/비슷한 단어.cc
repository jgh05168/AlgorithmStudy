/*
N개의 영단어들이 주어졌을 때, 가장 비슷한 두 단어를 구하자
접두사 길이 : 두 단어의 앞부분에서 공통적으로 나타나는 부분문자열의 길이
여러개인 경우, 입력되는 순서대로 제일 앞쪽에 있는 단어를 답으로 하기
S -> T

 N <= 20000
 완전탐색 : N^2 = 시간초과

*/
#include<iostream>
#include<vector>
#include<algorithm>
#include <string>

using namespace std;

int n;
vector<pair<string, int>>v;
int cnt, maxCnt;
string s, t;
string tmp;
vector<pair<int, string>>ans; //인덱스와 겹치는 것 
vector<pair<int, string>>ans2; //인덱스와 겹치는 것 


int main() {
	cin >> n;
	v.resize(n);
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		v[i] = { tmp,i };
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < n - 1; i++) {
		cnt = 0;
		for (int j = 0; j < v[i].first.size(); j++) {
			//같지않으면
			if (v[i].first[j] != v[i + 1].first[j]) {
				break;
			}
			cnt++;
		}

		//두 문자열이 완벽히 똑같으면 답이 될 수 없음
		if (v[i].first == v[i + 1].first || cnt < maxCnt)
			continue;
		//cnt 가 maxCnt 보다 크면 ans 벡터 초기화 
		//cnt가 maxCnt 랑 크거나 같으면 
		if (cnt > maxCnt) {
			ans = ans2;
			maxCnt = cnt;
		}

		ans.push_back({ v[i].second,v[i].first });
		ans.push_back({ v[i + 1].second,v[i + 1].first });

	}
	sort(ans.begin(), ans.end());
	string s = ans[0].second;
	for (int i = 1; i <= ans.size(); i++) {
		if (ans[i].second == s)
			continue;
		if (s.substr(0, maxCnt) != ans[i].second.substr(0, maxCnt))
			continue;
		t = ans[i].second;
		break;
	}
	cout << s << "\n" << t;

}