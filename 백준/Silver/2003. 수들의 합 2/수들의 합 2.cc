#include <iostream>

using namespace std;

int n,m;
int count=0;
int result;

int main() {
    cin >> n >> m;

    int a[n+1];

    for(int i=0;i<n;i++) {
        cin >> a[i];
    }

    for(int i=0;i<n;i++) {
        for(int j=i;j<n;j++) {
            result += a[j];

            if(result==m) {
                count++;
                result==0;
                break;
            }
        }
        if(result!=0) result=0;
    }   

    cout<< count;
}
