#include <iostream>
#include <cmath>
#include <cstdlib>
#include <map>
#include <vector>
#include <deque>
#include <string>
#include <algorithm>
using namespace std;

vector<int> Digits;
void test(vector<int>);
bool GoodOdd(int); // 1 3 5 7
bool BadOdd(int);  // 9
bool IsOdd(int);
int Plus(vector<int>, int, int, int);
int Minus(vector<int>, int, int, int);

int main()
{
    int T, Number, n, y, COUNT, P, M;
    cin >> T;

    for (int i = 1; (i <= T) && (T <= 100); i++) // 1st degree, O(n)
    {
        cin >> Number;
        n = Number;
        int c = floor(log10(n) + 1);

        if (c == 1) // single digit
        {
            y = 1;
            cout << "Case #" << i << ": " << y << flush << endl;
            Digits.clear();
        }
        else // not single digit
        {
            for (int j = c; j >= 1; j--) // 2nd degree, O(n^2)
            {
                Digits.push_back(n % 10);
                n /= 10;
            }
            reverse(Digits.begin(), Digits.end());
            // $$$ All above main() has been tested, vector constructed successfully

            // Check to see if there is an odd digit
            vector<int>::iterator it;
            it = find_if(Digits.begin(), Digits.end(), IsOdd);

            // First, check to see if first odd elem is 9 or not
            if (GoodOdd(*it))
            {
                // there is an odd elem, get the index of it
                int index = distance(Digits.begin(), it);
                P = Plus(Digits, index, Number, c);
                M = Minus(Digits, index, Number, c);
                y = min(P, M);
                cout << "Case #" << i << ": " << y << flush << endl;
                Digits.clear();
            }
            //else if (BadOdd(*it)) // if there is an 9
            else
            {
                y = 0;
                cout << "Case #" << i << ": " << y << flush << endl;
                Digits.clear();
            }
        }
    }
}

int Plus(vector<int> Digits, int index, int n, int c)
{
    string sub;
    Digits[index] += 1;
    for (int i = 0; i <= index; i++)
    {
        sub += to_string(Digits[i]);
    }
    sub += string(c - 1 - index, '0');
    int even = stoi(sub);
    int perfect = abs(n - even);
    cout << "plus" << perfect << "!";
    return perfect;
}

int Minus(vector<int> Digits, int index, int n, int c)
{
    string sub;
    Digits[index] -= 1;
    for (int i = 0; i <= index; i++)
    {
        sub += to_string(Digits[i]);
    }
    sub += string(c - 1 - index, '8');
    int even = stoi(sub);
    int perfect = abs(n - even);
    cout << "minus" << perfect << "!";
    return perfect;
}

void test(vector<int> myvector)
{
    cout << "vector contains: ";
    for (vector<int>::iterator it = myvector.begin(); it != myvector.end(); ++it)
        cout << *it;
    cout << '\n';
}

bool GoodOdd(int i)
{
    return (((i % 2) != 0) && (i != 9));
}

bool BadOdd(int i)
{
    return i == 9;
}

bool IsOdd(int i)
{
    return (i % 2 != 0);
}