import heapq




def find_kth_largest(nums, k):
    if k > len(nums):
        return None

    heap = []
# The code utilizes the property of a min-heap where the smallest element 
# is always at the root. By maintaining a heap of size k, it effectively
# keeps track of the k largest elements encountered so far
    for num in nums:
        heapq.heappush(heap, int(num))
        if len(heap) > k:
            heapq.heappop(heap)

    return heapq.heappop(heap)


# The time complexity of this approach is O(n log k),
# where n is the length of the input list. Since inserting and
# removing elements from a heap take O(log k) time complexity,
# and we perform these operations n times, the overall time complexity is O(n log k).

# The space complexity of this approach is O(k) because we only 
# keep a heap of size k to store the k largest numbers.



def find_kth_largest(nums, k):
    def partition(nums, low, high):
        pivot = int(nums[high])
        i = low - 1

        for j in range(low, high):
            if int(nums[j]) >= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quick_select(nums, low, high, k):
        if low == high:
            return nums[low]

        pivot_index = partition(nums, low, high)

        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return quick_select(nums, low, pivot_index - 1, k)
        else:
            return quick_select(nums, pivot_index + 1, high, k)
        
    return quick_select(nums, 0, len(nums) - 1, k - 1)

print(find_kth_largest(["3", "6", "7", "10"], 4))
print(find_kth_largest(["2","21","12","1","13","14"], 3))

