def coinChangeGreedy(m, coins):
    coins.sort(reverse = True)
    n = 0
    val = m
    res = []
    for coin in coins:
        if coin <= val:
            c = val//coin
            n+= c
            res.append(c)
            val-= coin*c
        else:
            res.append(0)
    return n, res

n = int(input("Types of Coins : "))
coins = list(map(int, input("Types : ").split()))
m = int(input("Amount : ₹"))
val, res = coinChangeGreedy(m, coins)
print("\nCoin\tCount")
for i in range(n):
    print(f" ₹{coins[i]}\t  {res[i]}")
print("Total =\t ", val)