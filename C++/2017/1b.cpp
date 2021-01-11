#include <bits/stdc++.h>

using namespace std;

int main() {
    // R <- RR, GB, BG
    // G <- GG, RB, BR
    // B <- BB, RG, GR 

    // #1: Starting with RR
    //  R R G B R G B B
    // R R R B B G G R G
    cout << "RRRBBGGRG" << endl;

    // #2: Starting with GB
    //  R R G B R G B B
    // G B G G R R B B B
    cout << "GBGGRRBBB" << endl;
    
    // #3 Starting with BG
    //  R R G B R G B B
    // B G B R G B R G R
    cout << "BGBRGBRGR" << endl;
}