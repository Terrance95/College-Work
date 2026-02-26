#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // For finding/removing items

using namespace std;

// 1. The Parent Class
class Member {
public:
    string name;
    Member(string n) {
        name = n;
        cout << "New Member Registered: " << name << endl;
    }
};

// 2. The Child Class (Inherits using :)
class Hacker : public Member {
public:
    string role;
    vector<string> skills; // A C++ Vector is like a Python List

    // C++ version of super(): We call Member(n) in the initializer list
    Hacker(string n, string r) : Member(n) {
        role = r;
    }

    void add_skill(string s) {
        skills.push_back(s);
        cout << "Added " << s << endl;
    }

    void remove_skill(string s) {
        // C++ doesn't have a simple .remove(). We have to find it first.
        auto it = find(skills.begin(), skills.end(), s);
        
        if (it != skills.end()) {
            skills.erase(it);
            cout << "Removed " << s << endl;
        } else {
            cout << "Error: " << s << " not found!" << endl;
        }
    }

    void show_profile() {
        cout << "\n--- " << name << "'S HACKER PROFILE ---" << endl;
        cout << "Role: " << role << endl;
        for (int i = 0; i < skills.size(); i++) {
            cout << i + 1 << ". " << skills[i] << endl;
        }
    }
};

int main() {
    Hacker user1("Terrance", "Logic Specialist");
    user1.add_skill("C++");
    user1.remove_skill("Java"); // Will show the error message
    user1.show_profile();
    return 0;
}