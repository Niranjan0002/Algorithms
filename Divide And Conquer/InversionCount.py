def inversionCount(arr):
    global c
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        inversionCount(l)
        inversionCount(r)
        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
              arr[k] = l[i]
              i += 1
            else:
                arr[k] = r[j]
                j += 1
                c += mid-i
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k]=r[j]
            j += 1
            k += 1

arr = [3,2,8,1,5,7,9]
c = 0
print("List : ",arr)
inversionCount(arr)
print("Count : ",c)