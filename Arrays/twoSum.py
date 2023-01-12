# Problem: https://leetcode.com/problems/two-sum/description/
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, j in enumerate(nums):
            x = target - j
            
            if x in count:
                return [count[x],i]
            
            count[j] = i
