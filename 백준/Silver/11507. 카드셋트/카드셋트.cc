#include<iostream>
#include<string>
using namespace std;

string s;
char a;
int b, c, d;
int card_num[4];
int card[4][14];

int main() {
	cin >> s;

	int temp = 0;
	for (int i = 0; i < s.size(); i += 3) {
		a = s[i];
		b = s[i + 1] - '0';
		c = s[i + 2] - '0';
		d = b * 10 + c;
		switch (a) {
		case 'P':
			temp = 0;
			break;
		case 'K':
			temp = 1;
			break;
		case 'H':
			temp = 2;
			break;
		case 'T':
			temp = 3;
			break;
		}
		
		card[temp][d]++;
		card_num[temp]++;
		if (card[temp][d] == 2)  {
			cout << "GRESKA" << endl;
			return 0;
		}
	}
    for (int i = 0; i < 4; i++) 
        cout << 13 - card_num[i] << ' ';

    cout << '\n';
	
	return 0;
}