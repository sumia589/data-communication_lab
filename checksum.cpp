#include<bits/stdc++.h>
using namespace std;
int main(){
    string data,checksum;
    cout<<"Enter data: ";
    cin>>data;
    cout<<"Enter checksum: ";
    cin>>checksum;
    string result="";
    int carry=0;
    //binary addition
    for(int i=data.length()-1;i>=0;i--){
        int sum=(data[i]-'0')+(checksum[i]-'0')+carry;
        if(sum==0){
            result='0'+result;
            carry=0;
        }
        else if(sum==1){
            result='1'+result;
            carry=0;
        }
        else if(sum==2){
            result='0'+result;
            carry=1;
        }
        else{
            result='1'+result;
            carry=1;
        }
    }
    //add carry
    if(carry==0){
        for(int i=result.length()-1;i>=0;i--){
            if(carry==0){
                carry=1;
            }else{
                carry=0;
            }
        }
    }
    cout<<"Result= "<<result<<endl;
    //detection
    if(result=="1111"){
        cout<<"No error detected\n";
    }else{
        cout<<"Error detected\n";
    }
    return 0;
}