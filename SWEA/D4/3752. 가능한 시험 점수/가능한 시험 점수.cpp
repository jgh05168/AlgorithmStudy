/*
n개의 문제를 만들기
틀리면 0점, 맞으면 배점만큼의 점수를 받는다.
학생들이 받을 수 있는 경우의 수는 몇 가지일까?

풀이 : 재귀로 모든 경우를 확인한다면 ? 2^100
그렇다면, 현재 생성된 값에다가 더해보자
-> 중복 숫자는 visited로 판단해서 넘기기
*/

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int t, n;
vector<int> scores;
int arr[101], visited[10001];

int main() {
	cin >> t;
	for (int tc=1;tc<t + 1;tc++) {
		cin >> n;
		
		for (int i = 0; i < n; i++)
			cin >> arr[i];
		scores.push_back(0);
		visited[0] = 1;

		for (int i = 0; i < n; i++) {
			int cur_size = scores.size();
			for (int j = 0; j < cur_size; j++) {
				int tmp = arr[i] + scores[j];
				if (!visited[tmp]) {
					visited[tmp] = 1;
					scores.push_back(tmp);
				}
			}
		}
		cout << '#' << tc << ' ' << scores.size() << '\n';
		memset(arr, 0, 101 * sizeof(int));
		memset(visited, 0, 10001 * sizeof(int));
		scores.clear();
	}
}