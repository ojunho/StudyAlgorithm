#include <iostream>
#include <string>
using namespace std;

struct Person{
    string name;
    int year;
    int month;
    int day;
};

int main(){

    const int MAX_NAME_LENGTH = 15;

    int n; // test case
    cin >> n;

    // max 나이가 많은 사람, 모든 변수가 가장 작도록
    Person max_person;
    max_person.year = 2011;
    max_person.month = 13;
    max_person.day = 32;
    
    // min 나이가 적은 사람, 모든 변수가 가장 크도록
    Person min_person;
    min_person.year = 1989;
    min_person.month = 0;
    min_person.day = 0;

    for(int i = 0; i < n; i++){
        string name;
        int day;
        int month;
        int year;
        cin >> name >> day >> month >> year;
        
        // max 먼저 판별
        for(int j = 0; j < 3; j++){
            if(year < max_person.year){
                max_person.name = name;
                max_person.year = year;
                max_person.month = month;
                max_person.day = day;
                continue;
            }
            else if(year == max_person.year){
                if(month < max_person.month){
                    max_person.name = name;
                    max_person.year = year;
                    max_person.month = month;
                    max_person.day = day;
                    continue;
                }
                else if(month == max_person.month){
                    if(day < max_person.day){
                        max_person.name = name;
                        max_person.year = year;
                        max_person.month = month;
                        max_person.day = day;
                        continue;
                    }
                }
            }
        }
        for(int j = 0; j < 3; j++){
            if(year > min_person.year){
                min_person.name = name;
                min_person.year = year;
                min_person.month = month;
                min_person.day = day;
                continue;
            }
            else if(year == min_person.year){
                if(month > min_person.month){
                    min_person.name = name;
                    min_person.year = year;
                    min_person.month = month;
                    min_person.day = day;
                    continue;
                }
                else if(month == min_person.month){
                    if(day > min_person.day){
                        min_person.name = name;
                        min_person.year = year;
                        min_person.month = month;
                        min_person.day = day;
                        continue;
                    }
                }
            }
        }
        // cout << min_person.name << "\n" << max_person.name << endl;
    }
    cout << min_person.name << "\n" << max_person.name << endl;

    return 0;
}