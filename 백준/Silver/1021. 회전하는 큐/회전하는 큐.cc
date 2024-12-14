/*
큐의 원소는 n개 있다.
뽑아내고자 하는 수는 m개 있다.

모듈러 연산을 사용해서 뽑아내기
*/

#include <iostream>
#include <algorithm>
#include <deque>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
	int n;
	int find;
	int num;
	int index;
	int count = 0;
	deque<int> d;

	cin >> n;
	cin >> find;

	for (int i = 1; i <= n; ++i) {
		d.push_back(i);
	}

	while (find--) {
		cin >> num;

		for (int i = 0; i < d.size(); ++i) {
			if (d[i] == num) {
				index = i;
				break;
			}
		}

		if (index < d.size() - index) {
			while (1) {
				if (d.front() == num) {
					d.pop_front();
					break;
				}
				++count;
				d.push_back(d.front());
				d.pop_front();
			}
		}
		else {
			while (1) {
				if (d.front() == num) {
					d.pop_front();
					break;
				}
				++count;
				d.push_front(d.back());
				d.pop_back();
			}
		}
	}
	cout << count << endl;

	return 0;
}