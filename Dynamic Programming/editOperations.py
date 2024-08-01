def editOperations(str1,str2,m,n):
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],min(dp[i-1][j-1], dp[i][j-1]))
    return dp[m][n]
    
str1 = input("String 1 : ")
str2 = input("String 2 : ")
print("No. of Operations : ",editOperations(str1, str2, len(str1), len(str2)))
