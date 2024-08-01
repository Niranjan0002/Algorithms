def coinChangeDP(coins, amount):
    n = len(coins)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    used_coins = [[0] * (amount + 1) for _ in range(n)]
    for i in range(1, amount + 1):
        for j, coin in enumerate(coins):
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                for k in range(n):
                    used_coins[k][i] = used_coins[k][i - coin]
                used_coins[j][i] += 1
    coin_counts = [used_coins[i][amount] for i in range(n)]
    return dp[-1], coin_counts

n = int(input("Types of Coins : "))
coins = list(map(int, input("Types : ").split()))
amount = int(input("Amount : ₹"))
min_coins, coin_counts = coinChangeDP(coins, amount)
print("\nCoin\tCount")
for i in range(n):
    print(f" ₹{coins[i]}\t  {coin_counts[i]}")
print("Total =\t ", min_coins)