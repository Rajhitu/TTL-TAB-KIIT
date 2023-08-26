#include<bits/stdc++.h>
#include <sstream> 

using namespace std;
int main()
{
//    string  s1="abc";
//    string s2="cbc";
//    int x=s1.find('p');
//    cout<<x;

vector<int> digits ={1,2,3,4,5};
 string ans="";
      for(int i=0;i<digits.size();i++)
      {
         ans.push_back((digits[i]));
      }
      cout<<ans;

        // int no= stoi(ans);
        // // to_string(no);
        // cout<<no;
    // vector<string> grp;
    //    int index=0;
    //    unordered_map<char,int>m;
        //    char a='1';
        //    char b='2';
        //    char c=a+b;
        //    cout<<c;
        // cout<<pow(2,5);
        // cout<<s1/2;
    //    m['a']=2;
    //    m['c']=3;
    //    m['b']=4;
    //    cout<<m.count('z');

        // for(int i=0;i<s1.size();i++)
        // {
        //       if(m.count(s1[i])==-1&&m.count(s2[i])==-1)
        //       {
        //           string temp={s1[i],s2[i]};
        //         grp.push_back(temp);
        //         m[s1[i]]=index;
        //         m[s2[i]]=index;
        //         index++;
                
        //       }
        //       else if(m.count(s1[i])==1)
        //       {

        //         grp[m[s1[i]]].push_back(s2[i]);
        //         m[s2[i]]=m[s1[i]];
               
        //       }
        //       else
        //       {
        //          grp[m[s2[i]]].push_back(s1[i]);
        //         m[s1[i]]=m[s2[i]];

        //       }
        //  }

        //  for(int i=0;i<grp.size();i++)
        //  {
        //    cout<<grp[i]<<"\n";
        //  }

    return 0;
}