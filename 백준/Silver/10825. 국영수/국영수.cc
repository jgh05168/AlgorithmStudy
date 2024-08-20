/*
1. 국어 점수가 감소하는 순서
2. 국어 점수가 같으면, 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
4. 모두 같으면, 이름의 사전 순으로

sort 함수에 내장함수를 설정해주어 조건을 맞춰주어야 한다.
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

struct Student {
	string name;
	int kor, eng, math;
};

vector<Student> std_list;

bool cmp(Student x, Student y) {
	if (x.kor != y.kor) {
		return x.kor > y.kor;
	}
	else if (x.eng != y.eng) {
		return x.eng < y.eng;
	}
	else if (x.math != y.math) {
		return x.math > y.math;
	}
	else {
		return x.name < y.name;
	}
}


int main() {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		Student std;
		cin >> std.name >> std.kor >> std.eng >> std.math;
		std_list.push_back(std);
	}

	sort(std_list.begin(), std_list.end(), cmp);

	for (int i = 0; i < n; i++) {
		cout << std_list[i].name << "\n";
	}

	return 0;
}