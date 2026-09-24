#include <iostream>
#include <climits>
using namespace std;

int matrixChainMultiplication(int p[], int n)
{
    int dp[n][n];

    // Cost is zero when multiplying one matrix
    for (int i = 1; i < n; i++)
    {
        dp[i][i] = 0;
    }

    // length is the chain length
    for (int length = 2; length < n; length++)
    {
        for (int i = 1; i < n - length + 1; i++)
        {
            int j = i + length - 1;
            dp[i][j] = INT_MAX;

            // Try every possible split
            for (int k = i; k < j; k++)
            {
                int cost = dp[i][k]
                         + dp[k + 1][j]
                         + p[i - 1] * p[k] * p[j];

                if (cost < dp[i][j])
                {
                    dp[i][j] = cost;
                }
            }
        }
    }

    return dp[1][n - 1];
}

int main()
{
    int n;

    cout << "Enter number of matrices: ";
    cin >> n;

    int p[n + 1];

    cout << "Enter dimensions of matrices:\n";
    cout << "For example, for A1(10x20), A2(20x30), enter: 10 20 30\n";

    for (int i = 0; i <= n; i++)
    {
        cin >> p[i];
    }

    int result = matrixChainMultiplication(p, n + 1);

    cout << "Minimum number of scalar multiplications = "
         << result << endl;

    return 0;
}