#include<iostream>
#include<cmath>
#include<math.h>
using namespace std;

int main()
{
   int t;
   cin>>t;
   int x1,y1,r1,x2,y2,r2;
   for (int i = 0; i < t; i++)
   {
      cin>>x1>>y1>>r1>>x2>>y2>>r2;
      double distance=sqrt(pow(x1-x2,2)+pow(y1-y2,2));

      //원이 겹칠떄
      if (distance == 0 && r1 == r2)
         cout << -1<<"\n";
      //원이 한점에서 만날때
      else if (distance == r1 + r2 || distance + (r1 > r2 ? r2 : r1) == (r1 > r2 ? r1 : r2))
         cout << 1<<"\n";
      //원이 아예 안만날때
      else if (distance > r1 + r2 || distance + (r1 > r2 ? r2 : r1) < (r1 > r2 ? r1 : r2))
         cout << 0<<"\n";
      //원이 2점에서 만날때
      else
         cout << 2<<"\n";
   }
}