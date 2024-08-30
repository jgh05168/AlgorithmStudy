/*
2141 우체국

풀이:
1. pair 사용해서 배열에 저장
1-2. 전체 사람 수 더해주기
2. 마을을 idx 기준 오름차순으로 정렬
3. 앞에서부터 차례대로 인원수를 더해준다.
	- 전체 인구수의 절반을 넘어가는 시점이 가장 최적의 idx
- 범위가 10억이라 long long을 사용하기
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

struct village {
	int idx, people;
};

int n;

bool cmp(village a, village b) {
	return a.idx < b.idx;
}

int main() {
	cin >> n;
	vector<village> country;

	long long total_ppl = 0;
	for (int i = 1; i < n + 1; i++) {
		village v;
		cin >> v.idx >> v.people;
		country.push_back(v);
		total_ppl += v.people;
	}

	// idx 기준 오름차순 정렬
	sort(country.begin(), country.end(), cmp);

	// 홀수일 때, 짝수일 때 중앙값이 다르다. 따라서 이를 한번에 처리해주어야 함
	total_ppl = (total_ppl + 1) / 2;

	
	// 덧셈 시작
	long long tmp_ppl = 0;
	for (int i = 0; i < country.size(); i++) {
		tmp_ppl += country[i].people;
		if (tmp_ppl >= total_ppl) {	   
			cout << country[i].idx << '\n';
			break;
		}
	}
	return 0;
}