
#include <iostream>
#include <string>
 
using namespace std;

int test;
int a,b;

int main() {
 
    cin>>test;
 
    for(int i=0; i<test; i++){
        cin>>a>>b;
 
        int cnt=0;
        int sum=0;
 
        for(int i=a; i<=b; i++){
            string str = to_string(i);
            for(int j=0; j<str.length(); j++){
                if(str[j]=='0'){
                    cnt++;
                }
            }
        }
        cout<<cnt<<"\n";
    }
    return 0;
}
