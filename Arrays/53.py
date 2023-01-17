class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) space/time 
        # this is using the sliding window technique

        maxSub = nums[0] # initialize to the base value, which could be negative
        curSum = 0 # the smallest the sum can be that we want

        for n in nums:
            if curSum < 0:
                curSum = 0 # reset the sum if it is a negative number
            curSum += n # add the current value onto the current sum of the subarray
            maxSub = max(maxSub, curSum) # take the max of the two

        return maxSub
