/*
측정할 수 없는 양의 정수 무게 중 최솟값을 구하자

풀이:
그리디, 정렬, set 
나올 수 있는 숫자를 더해가면서 비교하기
만약 맨 앞 숫자와 현재 숫자를 더한 값이 현재 값보다 크다면, 종료
1000 x 1000 
*/

#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n;
set<int> weights;
vector<int> scales;

int main() {
	cin >> n;
	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		scales.push_back(tmp);
	}

	// 0. 오름차순 정렬
	sort(scales.begin(), scales.end());

	// 1. 첫 녀석은 그냥 넣어주기
	weights.insert(scales[0]);
	int cur_num = scales[0];
	if (cur_num > 1)
		cout << 1 << '\n';
	else {
		// 2. 순회 시작
		for (int i = 1; i < n; i++) {
			// 더 큰 경우에 대해서 판단
			if (cur_num <= scales[i]) {
				if (cur_num + 1 < scales[i])
					break;
			}
			for (int j = 0; j < scales[i]; j++)
				++cur_num;
		}

		cout << cur_num + 1 << '\n';
	}
	

	return 0;
}