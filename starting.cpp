#include <iostream>
#include <string>
using namespace std;

int main() {
    string name;
    cout << "Enter your name: ";
    getline(cin, name); // This takes the full name with spaces
    cout << "Welcome to Engineering, " << name << "!" << endl;
    return 0;
}