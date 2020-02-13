// display and 2 buttons (plus, minus)
// plus = x++, minus = x--, 99 won't show as 099
// each char in number has to be even
// 1 <= n <= 10^16

#include <iostream>
#include <cmath>
#include <cstdlib> // absolute value
using namespace std;

int main()
{
    /* Get info from input file */
    int t;      // total numbers of test cases
    int i;      // case No.
    unsigned n; // the actual integar displayed
    int e;      // pow(10, e), to determine how many digits are there, e <= 16
    int y;      // output, how many button presses
    int digit;  // first most digit
    cin >> t;   // read t. cin knows that t is an int
    int plus, minus;

    for (i = 1; i <= t; i++) // iterate thru each integar
    {
        cin >> n;                     // get number
        for (int e = 16; e >= 0; e--) // LOOP of each digit
        {
            if (digit < 1)
                continue;
            else
            {
                if (digit % 2 != 0) // make each digit even,
                {
                    plus = ((digit + 1) * pow(10, e) - n);
                    minus = (n - digit * pow(10, e) + 2);
                    y = min(plus, minus);
                    break;
                }
            }
        }
        cout << "Case:#" << i << ": " << y << endl;
    }
    return 0;
}
