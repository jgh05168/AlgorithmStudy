/*
아~파트 아파트!

게임을 시작한 사람이(첫번째 사람) 아파트 층 수를 정한다
- j번째로 쌓은 손이 j층이 된다

풀이:
H < 10000
1. 배열의 몇번째에 있는지 저장하기
2. while문 돌면서 층 쌓기
*/

#include <iostream>
#include <map>
#include <queue>

using namespace std;

int n, m;
int h1, h2;
int apart[10001] = { 0, };
queue<int> q;

int main() {
	cin >> n >> m;
	for (int p = 1; p < m + 1; p++) {
		cin >> h1 >> h2;
		apart[h1] = p;
		apart[h2] = p;
	}
	
	for (int i = 0; i < 10001; i++) {
		if (apart[i]) q.push(apart[i]);
	}

	while (n--) {
		int tmp = q.front();
		q.pop();
		q.push(tmp);
	}

	cout << q.back() << '\n';

	return 0;
}