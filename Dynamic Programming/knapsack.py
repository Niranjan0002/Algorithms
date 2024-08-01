def knapSackGreedy(items, w):
    for item in items:
        item.append(item[0]/item[1])
    items.sort(key = lambda x : x[2], reverse = True)
    res = []
    total = 0
    for item in items:
        if item[1] <= w:
            res.append(item)
            w-=item[1]
            total += item[0]
        if w==0:
            break
    return res, total

def knapSackDP(items, W):
    n = len(items)
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif items[i-1][1] <= w:
                K[i][w] = max(items[i-1][0] + K[i-1][w-items[i-1][1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    res = []
    w = W
    for i in range(n, 0, -1):
        if K[i][w] != K[i - 1][w]:
            res.append(items[i - 1])
            w -= items[i - 1][1]
    return res, K[n][W]





n = int(input("No. of Items : "))
items = [list(map(int,input("Value and Weight of Item " + str(i+1) + " : ").split()))  for i in range(n)]
w = int(input("\nCapacity of Bag : "))
print("\nGreedy : ")
res, total = knapSackGreedy(items, w)
print("\nValue\tWeight")
for item in res:
    print(f"{item[0]}\t  {item[1]}")
print("\nTotal value =", total)
print("\n\n\nDynamic Programming : ")
res, total = knapSackDP(items, w)
print("\nValue\tWeight")
for item in res:
    print(f"{item[0]}\t  {item[1]}")
print("\nTotal Value =", total)