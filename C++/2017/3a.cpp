// Thank you to Spookiel for his Python solution, off which this solution is based
// https://github.com/Spookiel/British-Informatics-Olympiad-Solutions/blob/master/Code/2017/Q3%20-%20Mystery%20parcels.py

#include <bits/stdc++.h>

using namespace std;

typedef unsigned int uint;
typedef long long ll;

#define F first
#define S second

const int INF = INT_MAX;

int item_ways(int w, int n, int max_w){
    if (w == 0 && n == 0)
        return 1;
    if (w <= 0 || n <= 0)
        return 0;
    int ways = 0;
    for (int i = 1; i <= max_w; i++)
        ways += item_ways(w-i, n-1, i);
    return ways;
}   

int parcel_ways(int p, int max_w, int n, int w){
    if (p == 0 && n == 0) 
        return 1;
    if (p <= 0 && n <= 0)
        return 0;
    int ways = 0;
    for (int i = 1; i <= n; i++){
        ways += parcel_ways(p-1, max_w, n-i, w) * item_ways(w, i, max_w);
    }
    return ways;
}

int main() {
    int p, i, n, w; cin >> p >> i >> n >> w;
    cout << parcel_ways(p, i, n, w);
}