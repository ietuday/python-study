a = [6,9,5,20,11,12,3,1,2,30,54,27,96,36,48,2,5460,45,21522,75,36,44,85,2552,47,69,78,0]

#repeating loop len(a)(number of elements) number of times
for j in range(len(a)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(a)-1:
        #comparing the adjacent elements
        if a[i]>a[i+1]:
            #swapping
            a[i],a[i+1] = a[i+1],a[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
print (a)