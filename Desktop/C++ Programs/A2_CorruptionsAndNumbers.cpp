#include<iostream>

using namespace std;

int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        //Input_
        long int l,n,r;
        cin>>n>>l>>r;
        bool attend;

        //Process
        if(n/l >n/r ||n%r==0||n%l==0)
            attend=true;
        else attend=false;



        if(n<l)
            attend=false;
        if(n>=l && n<=r)
            attend=true;
        //Output
        if(attend)
            cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}
