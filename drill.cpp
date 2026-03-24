#include <iostream>
#include <string>
using namespace std;

class Agent {
public:
    string name;
    int energy;

    // Constructor to initialize our NAOS agent
    Agent(string n, int e) {
        name = n;
        energy = e;
    }

    void processTask() {
        if (energy > 10) {
            cout << name << " is processing... Energy: " << energy << endl;
            energy -= 5;
        } else {
            cout << "Low Power. Agent entering sleep mode." << endl;
        }
    }
};

int main() {
    Agent alpha("Neural_01", 100);
    alpha.processTask();
    return 0;
}