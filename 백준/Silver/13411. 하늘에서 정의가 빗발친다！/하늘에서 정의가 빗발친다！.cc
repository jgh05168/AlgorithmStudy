/*
멀리있는 적을 가까이 있는 적보다 빨리 맞출 수 있음
미사일에 격추되는 순서를 구하는 프로그래밍

속도가 존재함
거속시 ..!

*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;


int n;
double x, y, v;
vector<pair<double, int>> robot_list;

double dist(double a, double b) {
	return sqrt(pow(a, 2) + pow(b, 2));
}

int main() {
	cin >> n;

	for (int i = 1; i < n + 1; i++) {
		cin >> x >> y >> v;
		robot_list.push_back({ dist(x, y) / v, i });
	}

	sort(robot_list.begin(), robot_list.end());

	for (auto robot : robot_list)
		cout << robot.second << '\n';

	return 0;
}