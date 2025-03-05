/*
수학, 경우 나눠서 출력 ?
*/

#include <iostream>

using namespace std;

int n, k, i;
int sum = 0;

int main() {
   cin >> n >> k;
   for (i = 1; i <= k; i++) {
      sum += i;
   }
   n -= sum;
 
   if (n < 0) {
      cout << -1;
   }
   else {
      if (n % k == 0)
         cout << k - 1;
      else if (n % k != 0)
         cout << k;
   }
    
   return 0;
}