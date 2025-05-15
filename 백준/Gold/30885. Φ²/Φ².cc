/*
미생물이 한 마리만 남을 때까지 다음 규칙들을 따라 흡수한다는 사실 !
1. 하루에 한 번, 줄의 맨 앞에 있는 미생물부터 각 미생물 중 자신보다 크기가 작거나 같은 것들을 전부 흡수한다.
	- 다른 미생물을 흡수한 경우, 미생물의 크기는 흡수한 미생물의 크기의 합만큼 커진다.
2. 흡수당한 미생물은 사라지며 행동 불가능하다.
	- 하루에 한 번만 흡수가 가능하다.
3. 흡수하는 미생물은 하루에 흡수할 모든 미생물을 한 번에 흡수한다.
	- 크기의 경우, 먹은 뒤 크기가 아닌 현재 크기를 따른다.

풀이 : double linked list
양쪽 방향을 서로 먹을 수 있다.
양쪽 방향 체크하면서 계속 먹어치우는 행위를 반복하면 된다.
근데 시간초과 안나난 ..?
*/

#include <iostream>

using namespace std;


struct node {
	node* prev;
	long long size;
	int idx;
	node* next;
};

int n;
node* head = nullptr;
node* tail = nullptr;


void init() {
	cin >> n;
	
	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		node* new_node = new node;

		new_node->idx = i + 1;
		new_node->size = tmp;
		new_node->prev = nullptr;
		new_node->next = nullptr;

		if (!head) {
			head = tail = new_node;
		}
		else {
			tail->next = new_node;
			new_node->prev = tail;
			tail = new_node;
		}
	}
}

void simulation() {
	while (tail->prev != NULL) {
		node * cur = head;
		while (cur != NULL) {
			// 양쪽 크기 체크
			long long cur_size = cur->size;
			long long new_size = cur_size;

			if (cur->prev != NULL && cur_size >= cur->prev->size) {
				new_size += cur->prev->size;
				cur->prev = cur->prev->prev;
				if (cur->prev != NULL)
					cur->prev->next = cur;
				else
					head = cur;
			}
			if (cur->next != NULL && cur_size >= cur->next->size) {
				new_size += cur->next->size;
				cur->next = cur->next->next;
				if (cur->next != NULL)
					cur->next->prev = cur;
				else
					tail = cur;
			}

			cur->size = new_size;
			cur = cur->next;
		}
	}

	cout << tail->size << '\n';
	cout << tail->idx << '\n';
}

int main() {
	init();

	simulation();
}