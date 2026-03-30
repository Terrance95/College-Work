#include<iostream>
using namespace std;
int main(){
    int n,key;
    cout<<"enter n:";
    cin>>n;
    int a[n];
    cout<<"enter array elements:";
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    cout<<"enter search element:";
    cin>>key;
    int low=0,high=n-1;
    while(low<=high){
        int mid=(low+(high-low)/2);
        if(a[mid]==key){
            cout<<"element found at index "<<mid<<endl;
            return 0;
        }
        else if(a[mid]<key){
            low=mid+1;
        }
        else{
            high=mid-1;
        }

    }
    cout<<"element not found"<<endl;
    return 0;
}