#include <bits/stdc++.h>

using namespace std;

typedef unsigned int uint;
typedef long long ll;

#define F first
#define S second

const int INF = INT_MAX;

int main() {
    string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char d1[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M',
                   'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    char d2[26];

    int n; cin >> n;
    int pos = -1;
    for (int i = 0; i < 26; i++){
        pos = (pos + n) % letters.size();
        d2[i] = letters[pos]; 
        letters = letters.substr(0, pos) + letters.substr(pos+1, letters.size()-pos);
        pos--;
    }
    
    for (int i = 0; i < 6; i++){
        cout << d2[i];
    }
    cout << "\n";

    string pt; cin >> pt;
    int offset = 0;
    for (auto c: pt){
        int i = distance(d1, find(d1, d1 + 26, c));
        cout << d2[(i+offset)%26];
        offset++;
    }
}