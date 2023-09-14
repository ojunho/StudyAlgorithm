
#include <iostream>

int main() {
    int n; // 선수 수
    std::cin >> n;

    const int MAX_NAME_LENGTH = 100; // 선수 이름의 최대 길이
    char maxPlayerName[MAX_NAME_LENGTH]; // 가장 비싼 선수의 이름
    int maxPrice = -1; // 가장 비싼 가격

    for (int i = 0; i < n; ++i) {
        char name[MAX_NAME_LENGTH];
        int price;

        std::cin >> name >> price;

        if (price > maxPrice) {
            maxPrice = price;
            strncpy(maxPlayerName, name, MAX_NAME_LENGTH);
        }
    }

    // 결과 출력
    std::cout << "가장 비싼 선수: " << maxPlayerName << " (" << maxPrice << "만 달러)" << std::endl;

    return 0;
}