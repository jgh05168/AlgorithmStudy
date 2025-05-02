#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
string V;
int U, D, P, C, M;
string Answer;

void init() {
    cin >> V;
}

void simulation() {
    for (int i = 0; i < (int)V.length(); i++) {
        if (V[i] == 'U') {
            U++;
            C++;
        }
        else if (V[i] == 'C') {
            U++;
            C++;
        }
        else {
            P++;
            D++;
        }
    }
    if (D % 2 == 0) {
        if (U > (D / 2)) {
            Answer += "U";
        }
    }
    else {
        if (U > (D / 2) + 1) {
            Answer += "U";
        }
    }
    if (D > 0) {
        Answer += "D";
        Answer += "P";
    }

    if (Answer == "") {
        Answer += "C";
    }
}


int main() {
    init();
    simulation();
    cout << Answer << "\n";

    return 0;
}