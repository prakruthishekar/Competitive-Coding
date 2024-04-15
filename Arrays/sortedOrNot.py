def sorted(arr): # using sort() function
    
    for i in range(len(arr)-1):
        if(arr[i] > arr[i+1]):
            return False
    return True

arr = [10, 5, 20, 40]   
n = sorted(arr)
if(n == True):
 print("The given array is Sorted in acending order")
else:
 print("The given array is not Sorted in ascending order")