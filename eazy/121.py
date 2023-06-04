def maxProfit(prices):
    dp = [[] for i in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, len(prices)):
        dp[i][1] = max(dp[i - 1][1], -prices[i])
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    maxval = 0
    for val in range(0, len(prices)):
        maxval = max(maxval, dp[i][0])
    return maxval
