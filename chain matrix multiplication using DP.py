def matrix_chain_multiplication(p):
    n = len(p) - 1

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]



p = [10, 20, 30, 40, 30]

minimum_cost = matrix_chain_multiplication(p)

print("Minimum number of scalar multiplications:", minimum_cost)
