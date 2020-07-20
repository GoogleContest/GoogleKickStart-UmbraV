
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std; 

int main()
{
    int t; // the number of test cases
    int m; // the number of troublesome pairs
    string pair; // each pair has 2 elems(names), with '_' in between words, and space between each elem, case sensitive

    cin >> t; // read t. cin knows that t is an int, so it reads it as such. 
    cin >> m;
    getline(cin, pair);
    string first = pair.substr(0, pair.find(' ')); //find first name in the troublesome pair
    string second = pair.substr(pair.find(' ') + 1); //get the second name in the troublesome pair



    for (int i = 1; i <= t; ++i)
    {
        cin >> m; // read n and then m.
        cout << "Case #" << i << ": " << m << " " << m << endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }

    return 0;
}
