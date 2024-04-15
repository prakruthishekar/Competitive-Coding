# Elements on right side of an element are smaller then that element is a leader. 
# For an array sorted in ascn order then every element is a leader.
# For an array sorted in desc order then only last element is the leader.


# def leader(arr, n):
#     for i in range(n):
#         flag = True
#         for j in range(i+1,n):
#             if(arr[i] <= arr[j]):
#                 flag = False
#                 break
#         if(flag == True):
#             print(arr[i])   

# arr = [7,10,4,10,6,5,2]
# n = len(arr)
# leader(arr,n)     
# Time complexity : O(n*2) 
# Auxiliary Space : O(n)

#---------------------------------------------------------------------------------------------------------------------------

def leader(arr, n):
    leader = arr[n-1]
    print(leader, end= " ")
    for j in range(n-2,0,-1):
        if(leader < arr[j]):
            leader = arr[j]
            print(leader,  end= " ")

arr = [7,10,4,10,6,5,2]
print("Original Array", arr)
n = len(arr)
print("Leaders of Array in reverse structure ", end= " ")
leader(arr,n)  

# Time complexity : O(n) 
# Auxiliary Space : O(n)
 