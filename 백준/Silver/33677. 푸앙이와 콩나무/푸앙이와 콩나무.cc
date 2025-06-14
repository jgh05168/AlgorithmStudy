#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#define MAX 1000001
#define INF 2e9
#define LL long long

using namespace std;
LL N;
int Days[MAX], Waters[MAX];
pair<int, int> Answer;

void init() {
	for (int i = 0; i < MAX; i++) {
		Days[i] = INF;
		Waters[i] = INF;
	}
}

void input() {
	cin >> N;
}

void bfs() {
	queue<pair<LL, pair<int, int> > > Q;
	Q.push(make_pair(0, make_pair(0, 0)));
	Days[0] = 0;
	Waters[0] = 0;

	while (!Q.empty()) {
		LL NowH = Q.front().first;
		int NowD = Q.front().second.first;
		int NowW = Q.front().second.second;
		Q.pop();

		if (NowH + 1 <= N) {
			if (Days[NowH + 1] > NowD + 1) {
				Days[NowH + 1] = NowD + 1;
				Waters[NowH + 1] = NowW + 1;
				Q.push(make_pair(NowH + 1, make_pair(NowD + 1, NowW + 1)));
			}
			else if ((Days[NowH + 1] == NowD + 1) && (Waters[NowH + 1] > NowW + 1)) {
				Days[NowH + 1] = NowD + 1;
				Waters[NowH + 1] = NowW + 1;
				Q.push(make_pair(NowH + 1, make_pair(NowD + 1, NowW + 1)));
			}
		}
		if (NowH * 3 <= N) {
			if (Days[NowH * 3] > NowD + 1) {
				Days[NowH * 3] = NowD + 1;
				Waters[NowH * 3] = NowW + 3;
				Q.push(make_pair(NowH * 3, make_pair(NowD + 1, NowW + 3)));
			}
			else if ((Days[NowH * 3] == NowD + 1) && (Waters[NowH * 3] > NowW + 3)) {
				Days[NowH * 3] = NowD + 1;
				Waters[NowH * 3] = NowW + 3;
				Q.push(make_pair(NowH * 3, make_pair(NowD + 1, NowW + 3)));
			}
		}
		if (NowH * NowH <= N) {
			if (Days[NowH * NowH] > NowD + 1) {
				Days[NowH * NowH] = NowD + 1;
				Waters[NowH * NowH] = NowW + 5;
				Q.push(make_pair(NowH * NowH, make_pair(NowD + 1, NowW + 5)));
			}
			else if ((Days[NowH * NowH] == NowD + 1) && (Waters[NowH * NowH] > NowW + 5)) {
				Days[NowH * NowH] = NowD + 1;
				Waters[NowH * NowH] = NowW + 5;
				Q.push(make_pair(NowH * NowH, make_pair(NowD + 1, NowW + 5)));
			}
		}
	};
}

void settings() {
	bfs();
	Answer = make_pair(Days[N], Waters[N]);
}

void printAnswer() {
	cout << Answer.first << " " << Answer.second << "\n";
}

int main() {
	init();
	input();
	settings();
	printAnswer();

	return 0;
}