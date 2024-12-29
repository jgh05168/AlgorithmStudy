#include <iostream>
#define fio cin.tie(0)->sync_with_stdio(0)
using namespace std;

#include <map>
#include <sstream>
#include <vector>
#include <iomanip>
int main(){
    fio;
    map<string, int> map_;
    string S;
    double total = 0;
    while(getline(cin, S)){
        stringstream ss(S);
        while(ss >> S){
            map_[S]++;
            total += 1;
        }
    }
    //
    //cout << fixed << setprecision(4);
    vector<string> work ={"Re","Pt","Cc","Ea","Tb","Cm","Ex"};
    for(int i = 0; i < work.size(); i++){
        string s = work[i];
        if(map_.find(s) != map_.end()){
            cout << s <<' ' << map_[s] << ' ';
            cout << fixed << setprecision(2)<< map_[s]/total;
            cout <<'\n';
        }else{
            cout << s <<' ' << 0 << ' ';
            cout << "0.00";
            cout <<'\n';
        }
    }
    cout << "Total " << (int)total << " 1.00";
    return 0;
}