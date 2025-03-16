/*
substr로 문자열 나눠보면서 체크해나가기
*/

#include <string>
#include <vector>

using namespace std;

string s;

int solution(string t, string p) {
	int answer = 0;

	for (int i = 0; i < t.size() - p.size() + 1; i ++) {
		s = t.substr(i, p.size());

		if (p >= s)
			answer++;
	}

	return answer;
}