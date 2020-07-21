// I want to try to experiment a bit between python3 and c++
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T, R, C;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int L, Righ;
        cin >> L >> Righ;
        int R, C;
        R = min(Righ, L) - 1;
        C = max(Righ, L) - 1;
        int B1, B2;
        long A;
        long r, result;
        B1 = R * C;
        if (R == 1)
        {
            result = B1;
        }
        else
        {
            B2 = (R - 1) * (C - 1) * 2;
            // cout << "B1/B2" << B1 << B2 << endl;
            A = 0;
            int i = 2;
            while (i < R && R > 2 && A >= 0)
            {
                A += (R - i) * (C - i) * (i + 1);
                i += 1;
                // cout << "A: " << A << endl;
            }
            r = B1 + B2 + A;
            result = r % (long(pow(10, 9)) + 7);
        }
        cout << "Case #" << t << ": " << result << endl;
    }
    return 0;
}