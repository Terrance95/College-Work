#include <iostream>
#include <vector>

using namespace std;

int main() {
    // 1. Force the terminal to handle input correctly
    int n;
    if (!(cin >> n)) return 0;

    vector<long long> b(n + 1);
    vector<long long> final_seats(n + 1, 0);

    // 2. Read the array elements
    for (int i = 1; i <= n; i++) {
        cin >> b[i];
    }

    // 3. Process the "Reboot" logic
    for (int i = 1; i <= n; i++) {
        long long num = b[i] - 1; // Step 1
        int idx = i + 1;

        while (idx <= n && num > 0) {
            // Step 2
            final_seats[idx]++;
            num++;
            idx++;

            // Step 4 boundary check
            if (idx > n) break;

            // Step 3
            final_seats[idx]++;
            num -= 2; 
            idx++;
        }
    }

    // 4. Output results
    for (int i = 1; i <= n; i++) {
        cout << final_seats[i] << (i == n ? "" : " ");
    }
    cout << endl;

    return 0;
}