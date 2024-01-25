#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> c(26);
    
    string S; cin >> S;
    
    while(true) {
        bool chk = false;
        for(int i=0;i<S.length();i++) {
            if ('a'<=S[i]&&S[i]<='z') S[i]-=32;
            if (S[i]=='@') {
                chk = true;
                break;
            }
            else if ('A'<=S[i]&&S[i]<='Z') c[S[i]-'A']++;
        }
        if (chk) break;
        cin >> S;
    }
    
    int mx = 0;
    for(int i=0;i<26;i++) mx = max(mx, c[i]);
    
    for(int i=0;i<mx;i++) {
        for(int j=0;j<26;j++) {
            if(c[j]>=mx-i) cout << char('A'+j);
            else cout << ' ';
        }
        cout << endl;
    }
    
    cout << "--------------------------\nABCDEFGHIJKLMNOPQRSTUVWXYZ";
}