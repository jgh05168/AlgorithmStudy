#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

string input;

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	getline(cin, input);

	vector<string> result;

	string token = "";

	int index = 0;

	while (index < input.size()) {

		//구분자를 만났을때
		if (input[index] == '<' || input[index] == '>' || input[index] == '(' || input[index] == ')' || input[index] == ' ') {
			if (token.size() > 0) {
				result.push_back(token);
				token = "";
			}
			if (input[index] != ' ') {
				token += input[index];
				result.push_back(token);
				token = "";
			}

			index++;
		}
		else if (input[index] == '&' && (index + 1 < input.size() && input[index + 1] == '&')) {

			if (token.size() > 0) {
				result.push_back(token);
				token = "";
			}
			result.push_back("&&");

			index += 2;
		}
		else if (input[index] == '|' && (index + 1 < input.size() && input[index + 1] == '|')) {

			if (token.size() > 0) {
				result.push_back(token);
				token = "";
			}
			result.push_back("||");

			index += 2;
		}

		else { //구분자가 아닐때
			token += input[index];
			index++;
		}

	}

	//마지막 토큰이 있을때
	if (token.size() > 0) {
		result.push_back(token);
	}

	for (int i = 0; i < result.size(); i++) {
		cout << result[i] << " ";
	}

	return 0;
}