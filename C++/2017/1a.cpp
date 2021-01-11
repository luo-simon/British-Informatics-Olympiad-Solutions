#include <bits/stdc++.h>

using namespace std;

#define PB push_back

int main() {
    string in; cin >> in;
    
    vector<char> row;
    for (auto c: in) row.PB(c);

    while (row.size() > 1){
        vector<char> new_row;
        for (int i = 0; i < row.size()-1; i++){
            if (row[i] == row[i+1]) new_row.PB(row[i]);
            else {
                if ('R' != row[i] && 'R' != row[i+1]) new_row.PB('R');
                if ('G' != row[i] && 'G' != row[i+1]) new_row.PB('G');
                if ('B' != row[i] && 'B' != row[i+1]) new_row.PB('B');
            }
        }
        row = new_row;
    }
    cout << row[0];
}