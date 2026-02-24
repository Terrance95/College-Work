#include <iostream>
#include <string>
using namespace std;

// Parent Class
class Electronic {
public:
    string brand = "ASUS";
    void powerOn() {
        cout << "Device is booting up..." << endl;
    }
};

// Child Class inherits from Electronic
class Laptop : public Electronic {
public:
    string model = "Vivobook";
};

int main() {
    Laptop myLaptop;
    myLaptop.powerOn(); // Accessing parent function
    cout << myLaptop.brand << " " << myLaptop.model << endl;
    return 0;
}