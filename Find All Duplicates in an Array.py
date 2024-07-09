# Approach
# As we know that all elements are in the range from 1..n and our array length is also n.

# So can we represent each number with index. but here index would be from 0 to n-1. So our resepective index would be (element-1).

# So now our aim is to somehow do something at that index so that we can say it is visited.

# So we will make that index element negative which means that element is present.

# Complexity
# Time complexity: O(n)
# Auxiliary Space: O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            ind = abs(num) - 1
            if nums[ind] < 0:
                res.append(ind + 1)
            else:
                nums[ind] = -nums[ind]
        return res
