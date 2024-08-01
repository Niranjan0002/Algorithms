def findMax(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        l_max=findMax(left)
        r_max=findMax(right)
        if(l_max>r_max):
            return l_max
        else:
            return r_max
    else:
        return myList[0]

        
        

myList = [-7,3,9,3,-5,7]
max=findMax(myList)
print("List : ",myList)
print("Max : ",max)