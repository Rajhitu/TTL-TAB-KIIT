if (words[i].find(ans[j]) != string::npos)
            {

                words[i].erase(words[i].find(ans[j]),1);
            }