#include <iostream>
using namespace std;
int main()
{
string str1="a";

for(int i=0;i<str1.size();i++)
{
    int temp=str1[i]-'0';
    if(temp>=0&&temp<=9)
    {

    }
    else
    {
        cout<<"fasle";
             break;
    }
}
cout<<"true";

}