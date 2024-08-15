/*   Author: Mohammed Sadik
     Language: C++
     Difficulty: Easy    */

#include<iostream>
using namespace std;
int main(){
    int a;
    do{cin >> a;}while (a < 1 || a > 100);
if (a % 2 == 0 && a != 2)
cout << "Yes";
else cout << "No";
return 0;
}
