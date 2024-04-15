def nextGreaterElement(nums1, nums2):
        f = {}
        for i in range(0, len(nums2)-1):
            if nums2[i] < nums2[i+1]:
                f[nums2[i]] = nums2[i+1]
            else:
                left = i + 1
                right = len(nums2)-1
                
                while(left < right):
                    if (nums2[i] > nums2[left] and left <= len(nums2)-1):
                        left += 1
                    else:
                        f[nums2[i]] = nums2[left]
                        continue
                if nums2[i] > nums2[left]:
                     f[nums2[i]] = -1
                else:
                     f[nums2[i]] = nums2[left]


        
        f[nums2[-1]] = -1
        print(f)
        res = []
        for i in nums1:
            res.append(f[i])
        return res

print(nextGreaterElement(nums1 = [1,3,5,2,4], nums2 = [5,4,3,2,1]))
print(nextGreaterElement(nums1 = [1,3,5,2,4], nums2 = [6,5,4,3,2,1,7]))
