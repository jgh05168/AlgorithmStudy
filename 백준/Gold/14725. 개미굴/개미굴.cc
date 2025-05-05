/*
개미굴의 구조를 알아보자.
먹이가 있는 방을 따라 내려가다가 더 이상 내려갈 수 없으면 신호를 보낸다.

풀이 :
최종 depth = 15
n차 트리를 갖고있음 -> ㄹㅇ 트리를 만들어서 출력해야하나 .....
트리만들기 시작 !!

*/

#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct Node {
	string food_item;
	vector<Node*> children;
};

int n;
vector<vector<string>> vec;


Node* findOrAddChild(Node* parent_node, const string& item) {
	for (Node* child : parent_node->children) {
		if (child->food_item == item) {
			return child;
		}
	}

	// 찾지 못했으면 새로운 노드를 수동으로 할당하고 초기화합니다.
	Node* newNode = new Node();
	newNode->food_item = item;

	parent_node->children.push_back(newNode);

	return newNode;
}


void printTree(const Node* node, int depth) {
	if (depth > 0) {
		for (int i = 0; i < depth - 1; ++i) {
			cout << "--";
		}
		cout << node->food_item << '\n';
	}

	for (Node* child : node->children) {
		printTree(child, depth + 1);
	}
}


void init() {
	cin >> n;
	vec.resize(n);
	for (int i = 0; i < n; i++) {
		int k_val;
		cin >> k_val;
		vec[i].resize(k_val);
		for (int j = 0; j < k_val; j++) {
			cin >> vec[i][j];
		}
	}

	sort(vec.begin(), vec.end());
}


void simulation() {

	Node root;

	for (int i = 0; i < n; ++i) {
		Node* currentNode = &root;

		// currentNode에 계속해서 부모 노드를 업데이트 해준다. -> 재귀적으로 접근 ㄱㄴ
		for (const string& food : vec[i]) {
			currentNode = findOrAddChild(currentNode, food);
		}
	}

	printTree(&root, 0);

}


int main() {
	init();

	simulation();

	return 0;
}