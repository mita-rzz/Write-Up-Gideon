#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int a[3]={14,6,11};
    for (int i =0; i < 3; i++){
      
      for (int j =1; j < 29; j++){
        // cout << ((j*j)%29)  << " " <<   a[i]  << '\n';
        if ( ((j*j)%29)==a[i]){
          cout << j << '\n';
          break;
        }
      }
    }
    return 0;
}
