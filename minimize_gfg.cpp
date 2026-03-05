#include <iostream>
#include <vector>
#include <numeric> // For accumulate

using namespace std;

class Solution {
public:
    int minimiseExpression(vector<int> &a, int n) {
        long long sum = 0;
        
        // Step 1: Calculate the total sum of the array
        for (int i = 0; i < n; i++) {
            sum += a[i];
        }
        
        // Step 2: Calculate the average (The problem guarantees it's an integer)
        int x = sum / n;
        
        return x;
    }
};

int main() {
    int n;
    cout << "enter the number of elements:\n";
    cin >> n;
    
    vector<int> a(n);
    cout << "enter the elements in the array:\n";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    Solution s;
    cout << "The value of X is: " << s.minimiseExpression(a, n) << endl;
    
    return 0;
}