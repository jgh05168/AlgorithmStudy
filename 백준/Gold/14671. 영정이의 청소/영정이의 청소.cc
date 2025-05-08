/*
10:30

곰팡이는 시가닝 ㄴ라 떄마다 대각선 방향으로 증식한다.
-> 원래 곰팡이가 있던 자리의 곰팡이는 사라지게 된다.

영정이의 집의 크기와 현재 위치가 주어질 때 청소를 해야되는지 알려주자

풀이 : 조건을 잘 찾아봐야함
: 현재 위치에서 나머지 정점들 사이에 거리를 비교했을 때 홀수번 만에 갈 수 있는 거리가 있다면 
-> 모든 칸 증식 가능함

근데, K <= 10만이다. 어떻게 짝수번 홀수번을 비교하지 ?
1. grid에 입력을 다 받기
2. 대표 지점 한군데만 잡은 뒤, dist로 거리 계산하기 ???

초기 곰팡이 위치가 다음과 같으면 된다.
i+j가 홀수고 i가 홀수
i+j가 홀수고 i가 짝수
i+j가 짝수고 i가 홀수
i+j가 짝수고 i가 짝수
*/
#include <iostream>
#include <vector>

using namespace std;

int n, m, k;
int a, b;
bool chk[2][2];

int main() {
	cin >> n >> m >> k;

	for (int i = 0; i < k; ++i) {
		cin >> a >> b;
		chk[(a + b) % 2][b % 2] = true;
	}

	for (int i = 0; i < 2; ++i) {
		for (int j = 0; j < 2; ++j) {
			if (!chk[i][j]) {
				cout << "NO" << '\n';
				return 0;
			}
		}
	}
	cout << "YES" << '\n';
	return 0;
}