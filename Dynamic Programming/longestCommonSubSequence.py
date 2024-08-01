def LCS(str1,str2,l1,l2):
  dp = [['' for i in range(l2)] for j in range(l1)]

  for i in range(l1):
    if str2[0] in str1[:i+1]:
      dp[i][0] = str2[0]

  for j in range(l2):
    if str1[0] in str2[:j+1]:
      dp[0][j] = str1[0]

  for i in range(1, l1):
    for j in range(1, l2):
      if str1[i] == str2[j]:
        dp[i][j] = dp[i-1][j-1] + str1[i]
      else:
        if len(dp[i-1][j])==0:
          dp[i][j] = dp[i][j-1]
        elif len(dp[i][j-1])==0:
          dp[i][j] = dp[i-1][j]
        else:
          dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
  return dp[l1-1][l2-1]

str1 = input("First String : ")
str2 = input("Second String : ")
l1 = len(str1)
l2 = len(str2)
lcs1 = LCS(str1,str2,l1,l2)
lcs2 = LCS(str2,str1,l2,l1)
print("LCS : ")
lcs = lcs1 if len(lcs1) >= len(lcs2) else lcs2
print(lcs)
if(len(lcs1)==len(lcs2)):
  print(lcs2)