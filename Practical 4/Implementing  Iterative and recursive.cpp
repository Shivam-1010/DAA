//Iterative methood 

#include <iostream>
using namespace std;

long long factorialIterative(int n) {
    long long fact = 1;

    for (int i = 1; i <= n; i++) {
        fact = fact * i;
    }

    return fact;
}

int main() {
    int n;

    cout << "Enter a number: ";
    cin >> n;

    cout << "Factorial using Iterative Method = "
         << factorialIterative(n);

    return 0; 
}



//Recursive method

#include <iostream>
using namespace std;

long long factorialRecursive(int n) {
    if (n == 0 || n == 1)
        return 1;

    return n * factorialRecursive(n - 1);
}

int main() {
    int n;

    cout << "Enter a number: ";
    cin >> n;

    cout << "Factorial using Recursive Method = "
         << factorialRecursive(n);

    return 0;
}