#include <iostream>
using namespace std;


int sum(int n){
    if (n == 1){
        return 1;
    }
    else{
        return sum(n-1) + n;
    }
}
int main(){
    int ret;
    ret = sum(1000000);
    // 1,000,000 -> segmentation fault

    cout << ret << endl;
    return 0;
}