#include <iostream>
#include <string>
using namespace std; 
int main() {
	int n; cin >> n; 
	string s; cin >> s; 
	int index = s.find('*');//별을 기준으로 파트 나누기, 인덱스 번호 받아오기
	string part1 = s.substr(0, index); //왼쪽 파트 부분 
	string part2 = s.substr(index + 1); //오른쪽 파트 부분
	while (n--) { //n번 동안
		string cmp=""; 
		cin >> cmp; //string 하나 생성
		if (part1.size() + part2.size() > cmp.size())cout << "NE\n";//part1,2 의 사이즈를 합했을때 cmp문자열 보다 크면 NE 출력
		else if (cmp.find(part1) == 0) { //만약 part1 문자열이 cmp문자열안에 있고 첫부분이라면. 
			string ex = cmp.substr(cmp.size() - (part2.size())); // 문자열 ex 에 part2의 사이즈만큼 끝부분을 잘라서 저장
			if (ex == part2)cout << "DA\n"; //자른 문자열이 part2와 동일하냐? 그렇다면 DA출력
			else cout << "NE\n"; //아니라면 NE 출력
		}
		else cout << "NE\n";// part1과 cmp문자열이 일치하지 않으면 NE 바로 출력
	}
}