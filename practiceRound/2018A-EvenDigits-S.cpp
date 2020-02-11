// display and 2 buttons (plus, minus)
// plus = x++, minus = x--, 99 won't show as 099
// each char in number has to be even
// 1 <= n <= 10^16

#include <iostream> // includes cin to read from stdin and cout to write to stdout
#include <cmath>
#include <cstdlib>   // absolute value
using namespace std; // since cin and cout are both in namespace std, this saves some text

int main()
{
    /* Get info from input file */
    int t;    // numbers of cases
    int i;    // cased number
    int e;    // pow(10, e), to determine how many digits are there
    int y;    //output
    cin >> t; // read t. cin knows that t is an int

    for (i = 1; i <= t; i++)
    {
    }

    cout << "Case #" << i << ": " << y << endl;

    return 0;
}

/*for (int i = 1; i <= t; i++) // ??? Get other numbers?
{
    cin >> n;
    if (n < 10) // single digit
    {
        y = 1;
    }
    else if (n == 100)
    {
        y = 12;
    }
    else
    {
        int first;
        first = (int)floor(n / 10);
        if (first % 2 == 0) // first digit is even
        {
            if (n % 2 == 0) // second digit is even
            {
                y = 0;
            }
            else //second digit is not even
            {
                y = 1;
            }
        }
        else // first digit is not even
        {
            int second;              //let int a be the second digit
            second = n - first * 10; //a = 3, y = 5, a = 8, y = 2, a = 6, y = 4; a = 4, y = 6; a = 2, y = 4
            // when second < 4, y = second + 2, else y = 10 - second
            if (second < 4)
            {
                y = second + 2;
            }
            else
            {
                y = 10 - second;
            }
        }
    }
    */