/*
행, 열 나눠서 탐색 진행
*/

#include <vector>
#include <iostream>
#include <string>
using namespace std;

int R, C;

int main() {
	cin >> R >> C;

	string tmp, answer="zzzzzzzzzzz";
	vector<vector<char>> puzzle(R, vector<char>(C));
    
	for (int i = 0; i < R; i++) {
		tmp = "";
		for (int j = 0; j < C; j++) {
			cin >> puzzle[i][j];
			if (puzzle[i][j] == '#') {
				if (tmp.size() > 1 && answer > tmp) 
                    answer = tmp;
				tmp = "";
			}
			else 
                tmp += puzzle[i][j];
		}
		if (tmp.size() > 1 && answer > tmp) 
            answer = tmp;
	}

	for (int j = 0; j < C; j++) {
		tmp = "";
		for (int i = 0; i < R; i++) {
			if (puzzle[i][j] == '#') {
				if (tmp.size() > 1 && answer > tmp) 
                    answer = tmp;
				tmp = "";
			}
			else 
                tmp += puzzle[i][j];
		}
		if (tmp.size() > 1 && answer > tmp) 
            answer = tmp;
	}
	cout << answer << '\n';

	return 0;
}