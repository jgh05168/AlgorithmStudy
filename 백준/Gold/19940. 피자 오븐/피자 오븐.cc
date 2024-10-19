/*
일단 60분이 넘어간다면, 최대한 ADDH만을 사용해서 60분 단위로 올려줘야 최대한 적은 횟수로 버튼을 누를 수 있다.
따라서 주어진 시간 N을 일단 60으로 나눈다. 그러면 N/60은 ADDH를 누른 횟수가 되는 것이고, 
이제 우리는 N%60분을 5가지의 버튼을 사용해서 맞춰주면 된다.

또한 1분에서 59분까지의 버튼을 누르는 방법을 BFS를 사용해서 미리 구해두었다.

사전 순으로 앞서는 방법을 출력하는 것이기 때문에 BFS 과정에서 큐에 구조체를 push할 때 MINO 버튼이 1 증가했을 때의 데이터부터 push해야 한다.
*/

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define FIRST cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);
#define MAX 65


using namespace std;
struct INFO {
	int ADDH, ADDT, MINT, ADDO, MINO, Time;
};

int T, N;
INFO Minute[MAX];
bool visited[MAX];
queue<INFO> Q;

void BFS() {
	INFO Info = { 0,0,0,0,0,0 };
	Q.push(Info);

	while (!Q.empty()) {
		INFO CurInfo = Q.front();
		Q.pop();

		if ((CurInfo.Time >= 0) && (CurInfo.Time <= 60) && (!visited[CurInfo.Time])) {
			visited[CurInfo.Time] = true;
			Minute[CurInfo.Time] = CurInfo;
			Q.push({ CurInfo.ADDH,CurInfo.ADDT,CurInfo.MINT,CurInfo.ADDO,CurInfo.MINO + 1,CurInfo.Time - 1 });
			Q.push({ CurInfo.ADDH,CurInfo.ADDT,CurInfo.MINT,CurInfo.ADDO + 1,CurInfo.MINO,CurInfo.Time + 1 });
			Q.push({ CurInfo.ADDH,CurInfo.ADDT,CurInfo.MINT + 1,CurInfo.ADDO,CurInfo.MINO,CurInfo.Time - 10 });
			Q.push({ CurInfo.ADDH,CurInfo.ADDT + 1,CurInfo.MINT,CurInfo.ADDO,CurInfo.MINO,CurInfo.Time + 10 });
			Q.push({ CurInfo.ADDH + 1,CurInfo.ADDT,CurInfo.MINT,CurInfo.ADDO,CurInfo.MINO,CurInfo.Time + 60 });
		}
	};
}

int main() {
	FIRST
		BFS();
	cin >> T;
	while (T--) {
		cin >> N;
		int M = N / 60;
		int R = N % 60;
		cout << Minute[R].ADDH + M << " " << Minute[R].ADDT << " " << Minute[R].MINT << " " << Minute[R].ADDO << " " << Minute[R].MINO << "\n";
	};

	return 0;
}