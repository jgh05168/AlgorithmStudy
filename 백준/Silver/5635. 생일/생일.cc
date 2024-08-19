/*
가장 나이가 적은 사람과 가장 나이가 많은 사람 구하기

연도, 월, 일 순으로 정렬
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct Student {
	string name;
	int day;
	int month;
	int year;
};

bool compare(Student x, Student y) {
	if (x.year != y.year) {
		return x.year > y.year;
	}
	else if (x.month != y.month) {
		return x.month > y.month;
	}
	return x.day > y.day;
}


int main() {
	int n;
	cin >> n;
	vector<Student> student_list;

	for (int i = 0; i < n; i++) {
		Student std;
		cin >> std.name >> std.day >> std.month >> std.year;
		student_list.push_back(std);
	}

	// sort 함수 뒤에 정렬 함수(bool 타입)를 통해 python의 lambda 처럼 활용할 수 있음
	// 부호에 따라서 오름차순 / 내림차순 정할 수 있다.
	sort(student_list.begin(), student_list.end(), compare);

	cout << student_list[0].name << "\n" << student_list[n - 1].name << "\n";

	return 0;
}