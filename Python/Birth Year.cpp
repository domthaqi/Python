//DAMENIK THAQI
//DAMENIK.THAQI50@MYHUNTER.CUNY.EDU

#include <iostream>
using namespace std;

int main()
{
    int year;
    cout << "Enter year born:";
    cin >> year;

    while (year > 2018) {
        cout << "Entered a future year:" << endl;
        cout << "Enter year born:";
        cin >> year;
    }

    cout << "You entered: " << year << endl;






}