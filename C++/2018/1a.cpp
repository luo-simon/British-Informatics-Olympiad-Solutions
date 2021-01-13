#include <bits/stdc++.h>

using namespace std;

typedef unsigned int uint;
typedef long long ll;

#define F first
#define S second

const int INF = INT_MAX;

float float_fix(float n){
    // Tries to fix any floating-point errors that may occur
    n = (int)(n*100);
    return n/100;
}

int main() {
    float interest, repayment; cin >> interest >> repayment;
    interest /= 100; repayment /= 100;

    int debt = 10000;
    float paid = 0;
    while (debt > 0){
        debt += ceil(float_fix((float)debt * interest));
        int pay = ceil(float_fix((float)debt * repayment));
        if (pay < 5000) pay = 5000;
        if (pay > debt) pay = debt;
        paid += pay; debt -= pay;
    }
   printf("%.2f", paid/100);
}