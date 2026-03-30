#include <iostream>
using namespace std;

// The "Pre-Processor" for your Search Engine
void insertionSort(int a[], int n) {
    int j;
    for (int i = 1; i < n; i++) {
        j=i;
        while(j>=1){
            if(a[j]<a[j-1]){
                swap(a[j],a[j-1]);
            }
            j--;
        }
    }
}

int main() {
    int n, key;
    cout << "Enter n: ";
    cin >> n;
    int a[n];

    cout << "Enter array elements: ";
    for(int i = 0; i < n; i++) cin >> a[i];

    // CRITICAL SYSTEM STEP: Sort the data first
    insertionSort(a, n);
    
    cout << "Sorted array for searching: ";
    for(int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;

    cout << "Enter search element: ";
    cin >> key;

    int low = 0, high = n - 1;
    while(low <= high) {
        int mid = low + (high - low) / 2;
        if(a[mid] == key) {
            cout << "Element found at index " << mid << " (in sorted array)" << endl;
            return 0;
        }
        else if(a[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    cout << "Element not found" << endl;
    return 0;
}