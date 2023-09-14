#include <iostream>
#include <string.h>
using namespace std;
int main(){
    int n;
    cin >> n;

    const int MAX_NAME_LENGTH = 100;

    for(int i=0; i<n; i++){
        int m;
        cin >> m;

        char highPricePlayer[MAX_NAME_LENGTH];
        int highPrice = -1;

        for(int j=0; j<m; j++){

            int price; 
            char name[MAX_NAME_LENGTH];

            cin >> price >> name;
            if(price > highPrice){
                highPrice = price;
                strncpy(highPricePlayer, name, MAX_NAME_LENGTH);
            }
        }
        cout << highPricePlayer << endl;
    }

    return 0;
}

