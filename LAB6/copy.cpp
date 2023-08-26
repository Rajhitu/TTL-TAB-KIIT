#include <bits/stdc++.h>
using namespace std;
int main()
{
    vector<string> words = {"bella", "label", "roller"};
    string ans = words[0];
    for (int i = 1; i < words.size(); i++)
    {
        for (int j = 0; j < ans.size(); j++)
        {
            if (words[i].find(ans[j]) != string::npos)
            {

                words[i].erase(words[i].find(ans[j]),1);
            }
            else
            {
                ans.erase((ans.find(ans[j])),1);
            }
        }
    }

    cout << ans;
    
    return 0;
}