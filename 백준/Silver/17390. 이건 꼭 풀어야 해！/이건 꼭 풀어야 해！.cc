/*
n짜리 수열 A, 이를 비내림차순으로 만들어서 B를 출력
and 질문이 Q개나 존재함

풀이 : 
1. 오름차순 진행
2. 구간 별 누적합
구간을 구할 땐 단순이 빼면 된다.
*/

#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n, q;
int s, e;

int main() {
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

	cin >> n >> q;
	vector<int> arr(n);
	vector<int> perfixSum(n);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	// 0. 오름차순 정렬
	sort(arr.begin(), arr.end());

	// 1. 누적합 계산
	perfixSum[0] = arr[0];
	for (int i = 1; i < n; i++) {
		perfixSum[i] = perfixSum[i - 1] + arr[i];
	}

	// 2. 구간합 계산 (시작 위치를 더해줘야함)
	for (int i = 0; i < q; i++) {
		cin >> s >> e;
		cout << perfixSum[e - 1] - perfixSum[s - 1]  + arr[s - 1] << '\n';
	}

	return 0;
}
