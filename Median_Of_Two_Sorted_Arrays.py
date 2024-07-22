# Intuition:
# Approach : Conditional Statements
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        a = len(nums)
        if a%2 != 0:
            b = (a / 2) # 3/2 = 1.5
            b = int(b)
            return nums[b] #index of 2
        else:
            c = a//2 #4//2 = 2
            d = c+1 #3
            e = (nums[c-1] + nums[d-1]) / 2
            return e 
        
