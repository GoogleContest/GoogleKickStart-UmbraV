#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;

int main()
{
    int t, n, k;
    double chance, sum;
    cin >> t;

    for (int i = 1; i <= t; ++i)
    {
        cin >> n >> k;
        
        vector<double> vec;
        
        string myString;
        getline(cin, myString);
        stringstream iss( myString );
        int number;
        while ( iss >> number )
          vec.push_back( number );

        chance = 1 - pow((n - 1)/n, (k + 1));
        
        for (int j = 0; j <= (n - 1); ++j)
        {
            vec[j] *= chance;
        }
        
        sum = accumulate(vec.begin(), vec.end(), 0);
        
        cout << "Case #" << i << ": " << sum << endl;
    }

    return 0;
}
