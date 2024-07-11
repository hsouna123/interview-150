# Intuition :
# We have to find the minimum number of jumps required to reach the end of a given array of non-negative integers i.e the shortest number of jumps needed to reach the end of an array of numbers.
# Explanation to Approach :
# We are using a search algorithm that works by moving forward in steps and counting each step as a jump.
# The algorithm keeps track of the farthest reachable position at each step and updates the number of jumps needed to reach that farthest position.
# The algorithm returns the minimum number of jumps needed to reach the end of the array.
# Complexity :
# Time complexity : O(n)
# Space complexity: O(1)
class Solution:
  def jump(self, nums: List[int]) -> int:
    ans = 0
    end = 0
    farthest = 0

    # Implicit BFS
    for i in range(len(nums) - 1):
      farthest = max(farthest, i + nums[i])
      if farthest >= len(nums) - 1:
        ans += 1
        break
      if i == end:      # Visited all the items on the current level
        ans += 1        # Increment the level
        end = farthest  # Make the queue size for the next level

    return ans
