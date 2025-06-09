/*
최대공약수 찾아서 나눠주는 방식으로 풀기
*/

#include <iostream>
#include <vector>
using namespace std;

vector<int> A;

int GCD(int a, int b){
    if(b==0){
        return a;
    }else{
        if(a>b){
            return GCD(b,a%b);
        }else{
            return GCD(a,b%a);
        }
    }
}
int divisor(int N){
    A.clear();
    for(int i=1;i<=N;i++){
        if(N%i==0){
            A.push_back(i);
        }
    }
    return A.back();
}

int main(){

    int R,G;
    cin>>R>>G;

    divisor(GCD(R,G));

    for(int i=0;i<A.size();i++){
        cout<<A[i]<<" "<<R/A[i]<<" "<<G/A[i]<<'\n';
    }
    
    return 0;
}