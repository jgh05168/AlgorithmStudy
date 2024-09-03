/*
1041 주사위

주사위 면의 숫자가 주어진다.
- 선택된 면들의 마주보는 면은 절대 선택될 수 없다.
- 두 면의 합이 5이면 마주보는 면이다.
수식이 주어진다.
- (4 * min_triple) + ((8 * n - 12) * min_double) + (5 * n - 6) * (n - 2) * dice[0];
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long N, result;
vector<int> v(6); //주사위
int one = 5000, two = 5000, three = 5000; //1면,2면,3면 최소조합
int largest, sum; //가장 큰눈 , 눈의합

int main() {
	cin >> N;

	for (int i = 0; i < 6; i++) {
		cin >> v[i];
		sum += v[i];
		largest = max(largest, v[i]);
	}

	//마주보는 조합만 피하기 (0,5) , (1,4) , (2,3) -> 인덱스 합 : 5
	for (int i = 0; i < 6; i++) {
		one = min(one, v[i]);
		for (int j = i + 1; j < 6; j++) {
			if (i + j == 5) continue;
			two = min(v[i] + v[j], two);
			for (int k = j + 1; k < 6; k++) {
				if (i + k == 5 || j + k == 5) continue;
				three = min(three, v[i] + v[j] + v[k]);
			}
		}
	}
	//3면 : 4 , 2면 : 8N-12 , 1면 : (5N-6)(N-2)
	if (N == 1) result = sum - largest;
	else result = (4 * three) + ((8 * N - 12)*two) + (5 * N - 6) * (N - 2) * one;
	cout << result << endl;
}