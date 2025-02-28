/*
원형큐
deque
*/

#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int n;
deque<pair<int, int>> deck;

int main() {
	cin >> n;
	int tmp;
	for (int i = 1; i < n + 1; i++) {
		cin >> tmp;
		deck.push_back({ i, tmp });
	}

	int move;
	pair<int, int> node;
	while (n--) {
		cout << deck.front().first << ' ';
		move = deck.front().second;
		deck.pop_front();

		if (deck.empty())
			break;
		
		if (move < 0) {
			move = abs(move);
			while (move--) {
				node = deck.back();
				deck.pop_back();
				deck.push_front(node);
			}
		}
		else {
			move--;
			while (move--) {
				node = deck.front();
				deck.pop_front();
				deck.push_back(node);
			}
		}
	}

	return 0;
}