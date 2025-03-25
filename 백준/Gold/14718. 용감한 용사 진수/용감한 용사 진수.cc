/*
N명의 적 병사, 힘 민 지 3가지 능력치를 가짐

각 병사의 스텟보다 진수의 스텟이 더 높다면 적 병사를 이길 수 있음

진수가 적어도 k명의 병사를 이길 수 있게 하는 최소의 스텟 포인트

풀이 : 브루트포스
- 모든 스탯 조합을 만들어본 뒤, 전체 soldier 돌면서 k명 넘는지 확인
- 이후 넘는다면, answer 업데이트해주기
	- 굳이 힘 덱 인 따로 구해줄 필요 없이 answer와 min 값 비교

100 x 100 x 100 x 100
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define INF 9999999
using namespace std;

struct soldier {
	int s, d, i;
};

int n, k;
int answer = INF;
int a = 0, b = 0, c = 0;
vector<soldier> soldier_list;


void init() {
	soldier tmp;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> tmp.s >> tmp.d >> tmp.i;
		soldier_list.push_back(tmp);
	}
}


void solution() {

	// 힘 덱 인 별 조합을 모두 찾기 = 브루트포스
	for (int s = 0; s < n; s++) {
		for (int d = 0; d < n; d++) {
			for (int i = 0; i < n; i++) {
				int cnt = 0;

				int _str = soldier_list[s].s;
				int _dex = soldier_list[d].d;
				int _int = soldier_list[i].i;

				// 현재 힘 덱 인 조합을 가지고 이길 수 있는 용사 카운트
				for (int l = 0; l < n; l++) {
					if (soldier_list[l].s <= _str && soldier_list[l].d <= _dex && soldier_list[l].i <= _int) 
						cnt++;
				}

				// k명을 넘게 이길 수 있다면, 정답 업데이트
				if (cnt >= k) {
					answer = min(answer, _str + _dex + _int);
				}
			}
		}
	}

}

int main() {
	init();

	solution();

	cout << answer << '\n';

	return 0;
}