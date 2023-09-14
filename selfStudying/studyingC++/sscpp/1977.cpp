#include <iostream>
using namespace std;
int main() {
    int small = 10001, M,N, sum = 0, cnt=0;
    cin >> M >> N;
        for (int j = 1; j <= 100; j++)
        {
            if(j*j >= M&&j*j <= N)
            {
                sum += j*j;
                cnt++;
            }
            if (j*j >= M&&j*j <= N&&small > j*j)
            {
                small = j*j;
                
            }
        }
        if (cnt == 0)
        {
            cout << "-1";
            return 0;
        }
    cout << sum << '\n' << small;
}