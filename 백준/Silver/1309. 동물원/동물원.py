def count(n):
    MOD = 9901

    dp = [[0, 0, 0] for _ in range(n+1)]
    
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 1
    
    for i in range(2, n+1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD

    return (dp[n][0] + dp[n][1] + dp[n][2]) % MOD

n = int(input())
print(count(n))