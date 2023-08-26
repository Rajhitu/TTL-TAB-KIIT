#include<bits/stdc++.h>
using namespace std;\

	void ans(string s,int low,int high)
	{
	    if(low>=high)
	    {
	        return ;
	    }
	    
	    swap(s[low],s[high]);
       
         
	    ans(s,low+1,high-1);
	   
	}
	
	int isPalindrome(string s)
	{   string st=s;
	    string temp=s;
        cout<<"temp-->"<<temp<<endl;
	    ans(s,0,s.size()-1);
	    cout<<"s-->"<<s;
	    if(st==temp)
	    {
	        return 1;
	    }
	    else
	    {
	        return 0;
	    }
	}
int main()
{
    cout<<isPalindrome("abc");
    return 0;
}