#include <iostream>

using namespace std;

int n;

long long gcd(long long a, long long b) {
    if (a < b)
        swap(a, b);
    while (b != 0) {
        long long ans = a % b;
        a = b;
        b = ans;
    }
    return a;
}

int main() {
    cin >> n;
    for (int x = 0; x < n; x++) {
        long long a, b;
        cin >> a >> b;
        long long ans = gcd(a, b);
        cout << (a * b) / ans << "\n";
    }
}
