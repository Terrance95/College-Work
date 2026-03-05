#include <iostream>
#include <string>
#include <algorithm> // For min()

using namespace std;

class Solution {
public:
    int minFlips(string s) {
        int n = s.length();
        int flipsForPattern0 = 0;

        for (int i = 0; i < n; i++) {
            // Pattern A: 0, 1, 0, 1... 
            // At even index (0, 2, 4), we expect '0'
            // At odd index (1, 3, 5), we expect '1'
            if (i % 2 == 0) { // Even index
                if (s[i] != '0') flipsForPattern0++;
            } else { // Odd index
                if (s[i] != '1') flipsForPattern0++;
            }
        }

        // flipsForPattern1 is just the total length minus the other pattern's flips
        int flipsForPattern1 = n - flipsForPattern0;

        return min(flipsForPattern0, flipsForPattern1);
    }
};

int main() {
    string s;
    cin >> s;
    Solution sol;
    cout << sol.minFlips(s) << endl;
    return 0;
}