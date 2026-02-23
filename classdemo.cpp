#include<iostream>
using namespace std;
class student{
    public:
        string name;
        int roll;
        void display(){
            cout<<"Student:"<<name<<"|Roll number:"<<roll<<endl;

        }
};
int main(){
    student s;
    s.name="Terrance Paul";
    s.roll=95;
    s.display();
    return 0;
}