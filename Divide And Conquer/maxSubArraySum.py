def maxSubarraySum (A,low,high):
    if (low==high):
        return A[low]
    else:
        mid = (low+high)//2
        left = maxSubarraySum (A,low,mid)
        right = maxSubarraySum (A,mid+1,high)
        crossing = maxCrossingSubarraySum (A,low,mid,high)
        return max (left, right, crossing)
def maxCrossingSubarraySum (A,low,mid,high):
    sum=0
    max_leftsum, max_rightsum = -100,-100
    for i in range (mid,low-1,-1):
        sum = sum+A[i]
        if (sum>max_leftsum):
            max_leftsum = sum
    sum=0
    for i in range (mid+1,high+1):
        sum = sum+A[i]
        if (sum>max_rightsum):
            max_rightsum = sum
    return (max_leftsum + max_rightsum)

arr = [2,1,-5,4]
max_sum = maxSubarraySum(arr, 0, len(arr)-1)
print("List : ",arr)
print("Maximum contiguous subarray sum = ", max_sum)