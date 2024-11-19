/*
세 가지 경우로 나누어서 dp 식 세우기
마지막은 무조건 1임
1. 위에 삼각형이 있는 경우 
    t = nt * 3 + n_attack_t * 2
2. 위에 삼각형이 없는 경우
    t = 2 * nt + n_attack_t
이후 새로운 점화식
    n_attack_t = attack_t, nt = t;
*/

#include <string>
#include <vector>
using namespace std;

int solution(int n, vector<int> tops) {
	int attack_t, t, n_attack_t, nt;
	n_attack_t = 0, nt = 1;
	for (int i = 0; i < tops.size(); i++)
	{
		attack_t = n_attack_t + nt;
		if (tops[i] == 1)
		{
			t = nt * 3 + n_attack_t * 2;
		}
		else
		{
			t = 2 * nt + n_attack_t;
		}
		n_attack_t = attack_t, nt = t;
		n_attack_t %= 10007, nt %= 10007;
	}
	return (t + attack_t) % 10007;
}