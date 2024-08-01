def subsetSum(a,i,sum):
    global target,l
    if(i>=len(a) or sum>target):
        return False
    if(sum==target):
        return True
    if subsetSum(a,i+1,sum):
        return True
    if subsetSum(a,i+1,(sum+a[i])):
        l.append(a[i])
        return True
    
l=[]
a=[3,5,6,23,3,1,47,29,7,8,10]
target=7
print("Original List : ",a)
if subsetSum(a,0,0):
    print("Subset with sum ",target," : ",l)
else:
    print("No subset with given sum")

