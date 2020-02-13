// attempt after 50 submissions and white board flowchart

#include <iostream>
#include <cmath>
using namespace std;

int plusY(int);
int minusY(int);
int degree(int);
int first(int, int);

int main()
{
    // Variables
    int T;
    int N;
    int e, a, x;
    int y;
    int Plus, Minus;

    cin >> T;

    for (int i = 1; i <= T; i++)
    {
        cin >> N;
        e = degree(N);

        if (e == 0)
        {
            y = 1;
        }
        else
        {
            Plus = abs(plusY(N));
            Minus = abs(minusY(N));
            y = min(Plus, Minus);
        }
        cout << "Case:#" << i << ": " << y << endl;
    }
    return 0;
}

int plusY(int n)
{
    int y;
    int e = degree(n);
    int b = n;

    while (e >= 1)
    {
        int e = degree(b);
        int a = first(b, e);
        if (a % 2 == 0)
        {
            b = b - a * pow(10, e);
        }
        else
        {
            y = (a + 1) * pow(10, e) - n;
            return y;
        }
    }
}

int minusY(int n)
{
    int x = 0;
    int y;
    int e = degree(n);
    int a;
    int b = n;

    while (e >= 1)
    {
        e = degree(b);
        a = first(b, e);
        if (a % 2 == 0)
        {
            x += a * pow(10, e);
            b = b - a * pow(10, e);
        }
        else
        {
            x += (a - 1) * pow(10, e);
            int j;
            for (j = 0; e >= 1; e--)
            {
                j = 8 * pow(10, e - 1);
                x += j;
            }
        }
    }
    y = n - x;
    return y;
}

int degree(int n)
{
    for (int e = 16; e >= 1; e--)
    {
        if (n / pow(10, e) >= 1)
            return e;
    }
}

int first(int n, int e)
{
    int a;
    a = n / pow(10, e);
    a = floor(a);
    return a;
}
