def freqOfSortArray(arr,arr_size):
    count = 0
    for i in range(arr_size-1):
        if(arr[i] == arr[i+1]):
            count += 1
        else:
            print(arr[i]," frequency is ", count + 1)
            count = 0
    print(arr[arr_size-1]," frequency ", count + 1)

# Driver code
arr = [12,35,67,67]
n = len(arr)
freqOfSortArray(arr, n)