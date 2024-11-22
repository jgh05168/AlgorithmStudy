/*
n개의 주사위, 확률은 동일, 주사위에 쓰인 수의 구성은 모두 다르다
A는 자신이 승리할 확률이 높아주도록 주사위를 가져가려 함

풀이 : 완전탐색
주사위를 고르는 최대 경우의 수 : 10C5
각 주사위의 값을 비교하여 더해보는 경우 : 6^5
따라서, 완전탐색으로 풀 경우, 252 * 6^5 = 1,959,552 시간복잡도를 갖는다.
== 완탐가능 ㅋ
*/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int max_v = 0;
int selected[11] = { 0, };
vector<int> A;
vector<vector<int>> A_list;
vector<vector<int>> B_list;
vector<int> SumA;
vector<int> SumB;

int sortnum = 0;
int choice = 0;

void dfs(int depth, int idx) {
	if (depth == choice) {
		// B 조합 만들어주기
		vector<int> B;
		for (int i = 0; i < n; i++) {
			if (!selected[i])
				B.push_back(i);
		}
		// 만들 수 있는 게임 리스트에 저장
		A_list.push_back(A);
		B_list.push_back(B);
		return;
	}
	else {
		for (int i = idx; i < n; i++) {
			if (!selected[i]) {
				selected[i] = 1;
				A.push_back(i);
				dfs(depth + 1, i + 1);
				A.pop_back();
				selected[i] = 0;
			}
		}
	}
}


void sumCal(int count, int maxSum, vector<int> List, vector<vector<int>> dice) {

	if (count == 0) {

		if (sortnum == 0) {
			SumA.push_back(maxSum);
		}
		else {
			SumB.push_back(maxSum);
		}

		return;
	}


	for (int i = 0; i < dice[List[count - 1]].size(); i++) {
		sumCal(count - 1, maxSum + dice[List[count - 1]][i], List, dice);
	}
}


// 몇 번째 주사위에서 숫자 몇을 뽑았는지 체크
vector<int> diceCal(vector<vector<int>> dice) { // 현재 골라놓은 주사위들

	int Maxvictory = 0;
	vector<int>MaxList;

	for (int i = 0; i < A_list.size(); i++) {

		sortnum = 0;
		sumCal(choice, 0, A_list[i], dice);

		sortnum = 1;
		sumCal(choice, 0, B_list[i], dice);


		// 서로의 합이 나온 부분

		int maxTemp = 0;



		for (int j = 0; j < SumA.size(); j++) {

			for (int k = 0; k < SumB.size(); k++) {
				if (SumA[j] > SumB[k]) {
					maxTemp += 1;
				}

			}
		}
		if (maxTemp > Maxvictory) { // 승리할 확률 최신화
			Maxvictory = maxTemp;

			sort(A_list[i].begin(), A_list[i].end());
			MaxList = A_list[i];
		}

		SumA.clear();
		SumB.clear();
	}

	return MaxList;

}
vector<int> solution(vector<vector<int>> dice) {
	vector<int> answer;
	n = dice.size();
	choice = n / 2;

	// 0. 조합 찾기
	dfs(0, 0);

    // 1. 이기는 확률 계산
	answer = diceCal(dice);

	for (int i = 0; i < answer.size(); i++) {
		answer[i] += 1;
	}
	
	return answer;
}
